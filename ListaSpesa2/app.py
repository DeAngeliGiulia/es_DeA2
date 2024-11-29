from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from models import db, ListaSpesa

# Inizializza l'app Flask
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lista_spesa.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

lista_spesa = []

# Route principale
@app.route('/')
def home():
    lista_spesa = ListaSpesa.query.all()
    return render_template('index.html', lista_spesa=lista_spesa)

# Route per aggiungere un elemento
@app.route('/aggiungi', methods=['POST'])
def aggiungi():
    elemento = request.form.get('elemento', '').strip()
    if elemento:
        nuovo_elemento = ListaSpesa(elemento=elemento)
        db.session.add(nuovo_elemento)
        db.session.commit()
    return redirect(url_for('home'))

# Route per rimuovere un elemento
@app.route('/rimuovi/<int:indice>', methods=['POST'])
def rimuovi(indice):
    elemento = ListaSpesa.query.get_or_404(indice)
    db.session.delete(elemento)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/svuota', methods=['POST'])
def svuota_lista():
    ListaSpesa.query.delete()
    db.session.commit()
    return redirect(url_for('home'))

# Avvio dell'app Flask
if __name__ == '__main__':
    app.run(debug=True)