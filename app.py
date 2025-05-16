from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# Descubre
@app.route('/el-metodo')
def el_metodo():
    return render_template('el_metodo.html')

@app.route('/filosofia')
def filosofia():
    return render_template('filosofia.html')

@app.route('/acompanantes')
def acompanantes():
    return render_template('acompanantes.html')

@app.route('/lunas')
def lunas():
    return render_template('lunas.html')

# Información práctica
@app.route('/nuevo-en-yoga')
def nuevo_en_yoga():
    return render_template('nuevo_en_yoga.html')

@app.route('/etiqueta')
def etiqueta():
    return render_template('etiqueta.html')

@app.route('/mantras')
def mantras():
    return render_template('mantras.html')

# Otros

@app.route("/horarios-tarifas")
def horarios_tarifas():
    return render_template("horarios_tarifas.html")

@app.route('/eventos')
def eventos():
    return render_template('eventos.html')

@app.route('/galeria')
def galeria():
    return render_template('galeria.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(debug=True)
