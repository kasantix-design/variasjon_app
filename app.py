from flask import Flask, render_template, redirect, request, url_for, session, flash
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'veldig_hemmelig_nøkkel'
DB_FILE = 'database.db'

def init_db():
    con = sqlite3.connect(DB_FILE)
    cur = con.cursor()

    # Brukere
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    # ADL-oppgaver
    cur.execute("""
        CREATE TABLE IF NOT EXISTS adl_tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            task TEXT,
            frequency TEXT,
            days TEXT,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    # Kalender
    cur.execute("""
        CREATE TABLE IF NOT EXISTS kalender_avtaler (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            dato TEXT,
            tid TEXT,
            beskrivelse TEXT,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    # Notater
    cur.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            content TEXT,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    # Fullførte oppgaver
    cur.execute("""
        CREATE TABLE IF NOT EXISTS completed_tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            task TEXT,
            timestamp TEXT,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    # Lister
    cur.execute("""
        CREATE TABLE IF NOT EXISTS lists (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            title TEXT,
            items TEXT,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    con.commit()
    con.close()

@app.route("/initdb")
def initialize_database():
    init_db()
    return "✅ Database initialized!"

@app.route("/")
def home():
    icons = [
        {"name": "ADL", "image": "icons/adl.png", "link": "adl"},
        {"name": "Kalender", "image": "icons/kalender.png", "link": "kalender"},
        {"name": "Lister", "image": "icons/notater.png", "link": "lister"},
        {"name": "Notater", "image": "icons/notater.png", "link": "notater"},
        {"name": "Små oppgaver", "image": "icons/smaoppgaver.png", "link": "smaoppgaver"},
        {"name": "Store oppgaver", "image": "icons/storeoppgaver.png", "link": "storeoppgaver"},
        {"name": "Fullført", "image": "icons/fullfort.png", "link": "fullfort"},
        {"name": "Innstillinger", "image": "icons/innstillinger.png", "link": "innstillinger"},
    ]
    return render_template("home.html", icons=icons)

# ... resten av rutene du har skrevet (adl, kalender, notater, osv.) beholdes uendret ...

# Login / Register / Logout
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        con = sqlite3.connect(DB_FILE)
        cur = con.cursor()
        cur.execute("SELECT id, password FROM users WHERE username=?", (username,))
        user = cur.fetchone()
        con.close()
        if user and check_password_hash(user[1], password):
            session["user_id"] = user[0]
            flash("Innlogging vellykket!")
            return redirect(url_for("home"))
        else:
            flash("Feil brukernavn eller passord!")
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        hashed_pw = generate_password_hash(password)
        con = sqlite3.connect(DB_FILE)
        cur = con.cursor()
        try:
            cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_pw))
            con.commit()
            flash("Bruker opprettet!")
            return redirect(url_for("login"))
        except sqlite3.IntegrityError:
            flash("Brukernavn finnes allerede.")
        finally:
            con.close()
    return render_template("register.html")

@app.route("/logout")
def logout():
    session.pop("user_id", None)
    flash("Du er logget ut.")
    return redirect(url_for("home"))

if __name__ == "__main__":
    init_db()
    app.run()
