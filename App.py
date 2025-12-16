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

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
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

@app.route("/adl")
def adl():
    return render_template("adl.html")

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
            flash("Brukernavn finnes allerede.")
        finally:
            con.close()

    return render_template("register.html")

# 🔐 Logout
@app.route("/logout")
def logout():
    session.pop("user_id", None)
    flash("Du er logget ut.")
    return redirect(url_for("home"))

# 🚀 Kjør appen
if __name__ == "__main__":
    init_db()
    app.run(debug=True)
