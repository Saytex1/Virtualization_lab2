import psycopg2
from flask import Flask, render_template, request

app = Flask(__name__)


# CONFIGURATION DE LA BASE DE DONNEES
def get_db_connection():
    conn = psycopg2.connect(
        host="db_container",
        database="maliste",
        user="postgres",
        password="password",
    )
    return conn


@app.route("/", methods=["GET", "POST"])
def index():
    conn = get_db_connection()
    cur = conn.cursor()

    # 1. Créer la table si elle n'existe pas (Au démarrage)
    cur.execute(
        "CREATE TABLE IF NOT EXISTS courses (id serial PRIMARY KEY, nom varchar(100));"
    )
    conn.commit()

    # 2. Si l'utilisateur a envoyé un formulaire (POST)
    if request.method == "POST":
        item = request.form["item"]
        cur.execute("INSERT INTO courses (nom) VALUES (%s)", (item,))
        conn.commit()

    # 3. Récupérer toute la liste pour l'afficher
    cur.execute("SELECT * FROM courses;")
    ma_liste = cur.fetchall()

    cur.close()
    conn.close()

    # Renvoie le HTML en donnant la liste
    return render_template("index.html", liste_html=ma_liste)


if __name__ == "__main__":
    # host='0.0.0.0' obligatoire pour que Docker laisse passer le trafic
    app.run(debug=True, host="0.0.0.0")