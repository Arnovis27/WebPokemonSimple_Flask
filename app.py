from flask import Flask, render_template,redirect,url_for,request
import requests,urllib

app = Flask(__name__)

@app.route('/')
def index():    
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/buscar',methods=['POST'])
def buscar():
    id= request.form["ID"]
    print(id)
    url="https://pokeapi.co/api/v2/pokemon/"+ str(id)
    print(url)

    response= requests.get(url)
    if response.status_code == 200:
        response2= requests.get(url)
        payload= response2.json()
        sprites= payload.get('sprites', [])
        front_sprite=''

        if sprites:
            #Descargando Imagen
            if sprites:
                other= sprites["other"]
                if other:
                    officialartwork= other["official-artwork"]
                    if officialartwork:
                        front_sprite= officialartwork["front_default"]
            
            ruta="./static/sprite/sprite.png"
            imagen= open(ruta, 'wb')
            imagen.write(urllib.request.urlopen(front_sprite).read())
            imagen.close()
    else:
        return "Id de Pokemon invalido"

    return render_template('buscar.html')

if __name__ == '__main__':
    # Iniciamos la apicación en modo debug
    app.run(debug=True)