from flask import Flask, render_template, redirect, request, url_for, session, flash
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.secret_key = 'veldig_hemmelig_nøkkel'
DB_FILE = 'database.db'

# 📦 Init database hvis den ikke finnes
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

    con.commit()
    con.close()

# 🏠 Hjem
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/kalender")
def kalender():
    return render_template("kalender.html")

@app.route("/lister")
def lister():
    return render_template("lister.html")

# ✅ ADL-rute med GET og POST
@app.route("/adl", methods=["GET", "POST"])
def adl():
    if "user_id" not in session:
        flash("Du må være innlogget for å bruke ADL-funksjonen.")
        return redirect(url_for("login"))

    user_id = session["user_id"]
    con = sqlite3.connect(DB_FILE)
    cur = con.cursor()

    # Hvis bruker sender inn nytt skjema
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

# ✅ Sletting av ADL-oppgaver
@app.route("/adl/delete/<int:task_id>", methods=["POST"])
def delete_adl(task_id):
    if "user_id" not in session:
        flash("Du må være innlogget for å bruke dette.")
        return redirect(url_for("login"))

    con = sqlite3.connect(DB_FILE)
    cur = con.cursor()
    cur.execute("DELETE FROM adl_tasks WHERE id = ?", (task_id,))
    con.commit()
    con.close()
    flash("Oppgave fjernet.")
    return redirect(url_for("adl"))

@app.route("/smaoppgaver")
def smaoppgaver():
    return render_template("smaoppgaver.html")

@app.route("/storeoppgaver")
def storeoppgaver():
    return render_template("storeoppgaver.html")

@app.route("/fullfort")
def fullfort():
    return render_template("fullfort.html")

# 🔐 Login
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

# 🔐 Registrering
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
            flash("Brukernavn finn
