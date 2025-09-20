from flask import Flask, request, jsonify, send_file
import sqlite3
import matplotlib.pyplot as plt
import io

app = Flask(__name__)
DB_NAME = 'dados.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS itens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            valor REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/add_item', methods=['POST'])
def add_item():
    data = request.json
    nome = data.get('nome')
    valor = data.get('valor')

    if not nome or valor is None:
        return jsonify({"error": "Dados incompletos"}), 400

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('INSERT INTO itens (nome, valor) VALUES (?, ?)', (nome, valor))
    conn.commit()
    conn.close()
    return jsonify({"message": "Item adicionado com sucesso!"})

@app.route('/plot.png')
def plot_png():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('SELECT nome, SUM(valor) FROM itens GROUP BY nome')
    data = c.fetchall()
    conn.close()

    if not data:
        return "Nenhum dado para mostrar", 404

    nomes, valores = zip(*data)

    plt.figure(figsize=(8,5))
    plt.bar(nomes, valores, color='skyblue')
    plt.title('Valores por Nome')
    plt.xlabel('Nome')
    plt.ylabel('Valor')
    plt.tight_layout()

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()
    return send_file(img, mimetype='image/png')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
