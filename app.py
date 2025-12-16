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

# Hjemmeside med ikoner
@app.route("/")
def home():
    if "user_id" not in session:
        return redirect(url_for("login"))

    icons = [
        {"name": "ADL", "image": "icons/adl.png", "link": "adl"},
        {"name": "Kalender", "image": "icons/kalender.png", "link": "kalender"},
        {"name": "Lister", "image": "icons/notater.png", "link": "lister"},
        {"name": "Notater", "image": "icons/notater.png", "link": "notater"},
        {"name": "Små oppgaver", "image": "icons/smaoppgaver.png", "link": "smaoppgaver"},
        {"name": "Store oppgaver", "image": "icons/storeoppgaver.png", "link": "storeoppgaver"},
        {"name": "Fullført", "image": "icons/fullfort.png", "link": "fullfort"},
        {"name": "Innstillinger", "image": "icons/innstillinger.png", "link": "innstillinger"},
        {"name": "Rotekassen", "image": "icons/rotekassen.png", "link": "rotekassen"},
        {"name": "Logg ut", "image": "icons/loggut.png", "link": "logout"},
    ]
    return render_template("home.html", icons=icons)

# Ruter for hver side
@app.route("/adl", methods=["GET", "POST"])
def adl():
    if "user_id" not in session:
        flash("Du må være innlogget.")
        return redirect(url_for("login"))

    user_id = session["user_id"]
    con = sqlite3.connect(DB_FILE)
    cur = con.cursor()

    if request.method == "POST":
        task = request.form["task"]
        frequency = request.form["frequency"]
        days = ','.join(request.form.getlist("days")) if frequency == "ukentlig" else "alle"
        cur.execute("INSERT INTO adl_tasks (user_id, task, frequency, days) VALUES (?, ?, ?, ?)",
                    (user_id, task, frequency, days))
        con.commit()

    cur.execute("SELECT * FROM adl_tasks WHERE user_id = ?", (user_id,))
    tasks = cur.fetchall()
    con.close()
    return render_template("adl.html", tasks=tasks)

@app.route("/kalender", methods=["GET", "POST"])
def kalender():
    if "user_id" not in session:
        flash("Du må være innlogget.")
        return redirect(url_for("login"))

    user_id = session["user_id"]
    con = sqlite3.connect(DB_FILE)
    cur = con.cursor()

    if request.method == "POST":
        dato = request.form["dato"]
        tid = request.form["tid"]
        beskrivelse = request.form["beskrivelse"]
        cur.execute("INSERT INTO kalender_avtaler (user_id, dato, tid, beskrivelse) VALUES (?, ?, ?, ?)",
                    (user_id, dato, tid, beskrivelse))
        con.commit()

    cur.execute("SELECT * FROM kalender_avtaler WHERE user_id = ?", (user_id,))
    avtaler = cur.fetchall()
    con.close()
    return render_template("kalender.html", avtaler=avtaler)

@app.route("/lister", methods=["GET", "POST"])
def lister():
    if "user_id" not in session:
        flash("Du må være innlogget.")
        return redirect(url_for("login"))

    user_id = session["user_id"]
    con = sqlite3.connect(DB_FILE)
    cur = con.cursor()

    if request.method == "POST":
        title = request.form["title"]
        items = request.form["items"]
        cur.execute("INSERT INTO lists (user_id, title, items) VALUES (?, ?, ?)", (user_id, title, items))
        con.commit()

    cur.execute("SELECT * FROM lists WHERE user_id = ?", (user_id,))
    lists = cur.fetchall()
    con.close()
    return render_template("lister.html", lists=lists)

@app.route("/notater", methods=["GET", "POST"])
def notater():
    if "user_id" not in session:
        flash("Du må være innlogget.")
        return redirect(url_for("login"))

    user_id = session["user_id"]
    con = sqlite3.connect(DB_FILE)
    cur = con.cursor()

    if request.method == "POST":
        content = request.form["content"]
        cur.execute("INSERT INTO notes (user_id, content) VALUES (?, ?)", (user_id, content))
        con.commit()

    cur.execute("SELECT content FROM notes WHERE user_id = ?", (user_id,))
    notes = cur.fetchall()
    con.close()
    return render_template("notater.html", notes=notes)

@app.route("/smaoppgaver")
def smaoppgaver():
    return render_template("smaoppgaver.html")

@app.route("/storeoppgaver")
def storeoppgaver():
    return render_template("storeoppgaver.html")

@app.route("/fullfort", methods=["GET", "POST"])
def fullfort():
    if "user_id" not in session:
        flash("Du må være innlogget.")
        return redirect(url_for("login"))

    user_id = session["user_id"]
    con = sqlite3.connect(DB_FILE)
    cur = con.cursor()

    if request.method == "POST":
        task = request.form["task"]
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        cur.execute("INSERT INTO completed_tasks (user_id, task, timestamp) VALUES (?, ?, ?)",
                    (user_id, task, timestamp))
        con.commit()

    cur.execute("SELECT task, timestamp FROM completed_tasks WHERE user_id = ? ORDER BY timestamp DESC",
                (user_id,))
    done_tasks = cur.fetchall()
    con.close()
    return render_template("fullfort.html", done_tasks=done_tasks)

@app.route("/innstillinger")
def innstillinger():
    return render_template("innstillinger.html")

@app.route("/rotekassen")
def rotekassen():
    return render_template("rotekassen.html")

@app.route("/logout")
def logout():
    session.pop("user_id", None)
    flash("Du er logget ut.")
    return redirect(url_for("login"))

# Login / Register
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
            flash("Bruker opprettet! Du kan nå logge inn.")
            return redirect(url_for("login"))
        except sqlite3.IntegrityError:
            flash("Brukernavn finnes allerede.")
        finally:
            con.close()
    return render_template("register.html")

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
