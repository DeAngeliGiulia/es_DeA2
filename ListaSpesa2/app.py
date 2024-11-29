from flask import Flask, render_template, request, redirect, url_for

# Inizializza l'app Flask
app = Flask(__name__)

lista_spesa = []

# Route principale
@app.route('/')
def home():
    return render_template('index.html', lista_spesa=lista_spesa)

# Route per aggiungere un elemento
@app.route('/aggiungi', methods=['POST'])
def aggiungi():
    elemento = request.form.get('elemento', '').strip()
    if elemento:
        lista_spesa.append(elemento)
    else:
        print("Errore: Elemento vuoto non aggiunto.")
    return redirect(url_for('home'))

# Route per rimuovere un elemento
@app.route('/rimuovi/<int:indice>', methods=['POST'])
def rimuovi(indice):
    if 0 <= indice < len(lista_spesa):
        lista_spesa.pop(indice) 
    return redirect(url_for('home'))

# Avvio dell'app Flask
if __name__ == '__main__':
    app.run(debug=True)