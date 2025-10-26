from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    return '''
    <html>
        <head>
            <title>Mi primera página web</title>
        </head>
        <body>
            <h1>Bienvenidos a mi primera página</h1>
            
            
            <img src="/static/cielo.jpeg" width="300">
            
            <p><b>Autor:</b></p>
            <p>Estefany Portillo</p>
            <p>Ingrid Machuca</p>
            
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
