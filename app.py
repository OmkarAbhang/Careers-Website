from flask import Flask, render_template, request
from database import engine
from sqlalchemy import text
# creating object of flask
app = Flask(__name__)


@app.route("/")
def hello_world():
  return render_template("index.html")

@app.route("/SignUp")
def SignUp():
  return render_template("register.html")


@app.route("/SignIn")
def SignIn():
  return render_template("login.html")

@app.route('/register', methods=['POST'])
def register():
  email = request.form['email']
  name = request.form['name']
  password = '+'.join(request.form.getlist('password'))
  password = password[len(password) // 2 + 1:]
  pwd = ""
  for i in range(len(password)):
    if password[i] != ',':
      pwd += password[i]
  with engine.connect() as conn:
    query = "INSERT INTO account (username, password, email) VALUES (:name, :pwd, :email)"
    conn.execute(text(query), {'name': name, 'pwd': pwd, 'email': email})
  return render_template("index.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
  error = None
  if request.method == 'POST':
    email = request.form['email']
    password = '+'.join(request.form.getlist('password'))
    password = password[len(password) // 2 + 1:]
    pwd = ""
    for i in range(len(password)):
      if password[i] != ',':
        pwd += password[i]
    with engine.connect() as conn:
      query = "SELECT username FROM account WHERE email = :email AND password = :password"
      result = conn.execute(text(query), {'email': email, 'password': pwd}).fetchone()
      if result:
          name = result[0]
          return render_template('user.html', name=name)
      else:
          error = 'Invalid email or password'
          return render_template('login.html', error=error)

  
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=False)
