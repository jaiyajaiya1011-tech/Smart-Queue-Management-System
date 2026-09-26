from flask import Flask, render_template, request, redirect
from database import create_database
import sqlite3

app = Flask(__name__)

create_database()


def get_db_connection():
    conn = sqlite3.connect("queue.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def home():
    conn = get_db_connection()

    waiting_count = conn.execute(
        "SELECT COUNT(*) FROM tokens WHERE status = 'Waiting'"
    ).fetchone()[0]

    total_tokens = conn.execute(
        "SELECT COUNT(*) FROM tokens"
    ).fetchone()[0]

    serving_count = conn.execute(
        "SELECT COUNT(*) FROM tokens WHERE status = 'Serving'"
    ).fetchone()[0]

    completed_count = conn.execute(
        "SELECT COUNT(*) FROM tokens WHERE status = 'Completed'"
    ).fetchone()[0]

    serving_token = conn.execute(
        "SELECT token_number FROM tokens "
        "WHERE status = 'Serving' ORDER BY id LIMIT 1"
    ).fetchone()

    if serving_token:
        current_token = serving_token["token_number"]
    else:
        current_token = "Not Serving"

    conn.close()

    return render_template(
        "index.html",
        waiting_count=waiting_count,
        total_tokens=total_tokens,
        serving_count=serving_count,
        completed_count=completed_count,
        current_token=current_token
    )


@app.route("/register")
def register_page():
    return render_template("register.html")


@app.route("/register", methods=["POST"])
def register():
    name = request.form["name"]
    email = request.form["email"]
    password = request.form["password"]

    conn = get_db_connection()

    try:
        conn.execute(
            "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
            (name, email, password)
        )
        conn.commit()
    except sqlite3.IntegrityError:
        conn.close()
        return "Email already registered"

    conn.close()

    return redirect("/login")


@app.route("/login")
def login_page():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    email = request.form["email"]
    password = request.form["password"]

    conn = get_db_connection()

    user = conn.execute(
        "SELECT * FROM users WHERE email = ? AND password = ?",
        (email, password)
    ).fetchone()

    conn.close()

    if user:
        return redirect("/")

    return "Invalid email or password"


@app.route("/generate-token", methods=["POST"])
def generate_token():
    service = request.form["service"]

    conn = get_db_connection()

    count = conn.execute(
        "SELECT COUNT(*) FROM tokens"
    ).fetchone()[0]

    token_number = "A" + str(101 + count)

    conn.execute(
        "INSERT INTO tokens (token_number, service, status) "
        "VALUES (?, ?, 'Waiting')",
        (token_number, service)
    )

    conn.commit()
    conn.close()

    return render_template(
        "token.html",
        token_number=token_number,
        service=service
    )


@app.route("/user-dashboard")
def user_dashboard():
    conn = get_db_connection()

    waiting_count = conn.execute(
        "SELECT COUNT(*) FROM tokens WHERE status = 'Waiting'"
    ).fetchone()[0]

    serving_token = conn.execute(
        "SELECT token_number FROM tokens "
        "WHERE status = 'Serving' ORDER BY id LIMIT 1"
    ).fetchone()

    if serving_token:
        current_token = serving_token["token_number"]
    else:
        current_token = "Not Serving"

    user_token = conn.execute(
        "SELECT token_number, status "
        "FROM tokens ORDER BY id DESC LIMIT 1"
    ).fetchone()

    if user_token:
        token = user_token["token_number"]
        status = user_token["status"]
    else:
        token = None
        status = "Waiting"

    estimated_wait = waiting_count * 5

    if estimated_wait == 0:
        estimated_wait_text = "Your turn is next"
    else:
        estimated_wait_text = f"{estimated_wait} min"

    conn.close()

    return render_template(
        "user_dashboard.html",
        token=token,
        current_token=current_token,
        waiting_count=waiting_count,
        estimated_wait=estimated_wait_text,
        status=status
    )


@app.route("/admin-dashboard")
def admin_dashboard():
    conn = get_db_connection()

    total_tokens = conn.execute(
        "SELECT COUNT(*) FROM tokens"
    ).fetchone()[0]

    waiting_count = conn.execute(
        "SELECT COUNT(*) FROM tokens WHERE status = 'Waiting'"
    ).fetchone()[0]

    completed_today = conn.execute(
        "SELECT COUNT(*) FROM tokens WHERE status = 'Completed'"
    ).fetchone()[0]

    serving_token = conn.execute(
        "SELECT token_number FROM tokens "
        "WHERE status = 'Serving' ORDER BY id LIMIT 1"
    ).fetchone()

    if serving_token:
        current_token = serving_token["token_number"]
    else:
        current_token = "Not Serving"

    queue_rows = conn.execute(
        "SELECT token_number, service, status "
        "FROM tokens "
        "WHERE status IN ('Waiting', 'Serving') "
        "ORDER BY id"
    ).fetchall()

    queue = []

    for item in queue_rows:
        queue.append({
            "token": item["token_number"],
            "service": item["service"],
            "status": item["status"]
        })

    conn.close()

    return render_template(
        "admin_dashboard.html",
        total_tokens=total_tokens,
        current_token=current_token,
        waiting_count=waiting_count,
        completed_today=completed_today,
        queue=queue
    )


@app.route("/call-next", methods=["GET", "POST"])
def call_next():
    conn = get_db_connection()

    conn.execute(
        "UPDATE tokens SET status = 'Completed' "
        "WHERE status = 'Serving'"
    )

    next_token = conn.execute(
        "SELECT id FROM tokens "
        "WHERE status = 'Waiting' "
        "ORDER BY id LIMIT 1"
    ).fetchone()

    if next_token:
        conn.execute(
            "UPDATE tokens SET status = 'Serving' "
            "WHERE id = ?",
            (next_token["id"],)
        )

    conn.commit()
    conn.close()

    return redirect("/admin-dashboard")


if __name__ == "__main__":
    app.run(debug=True)