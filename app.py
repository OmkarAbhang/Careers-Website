from flask import Flask, render_template
from database import engine
from sqlalchemy import text
# creating object of flask
app = Flask(__name__)


def load():
  with engine.connect() as conn:
    result = conn.execute(text("select * from account"))
    result_dicts = []
    for row in result.all():
      result_dicts.append(row._asdict())
  return result_dicts


@app.route("/")
def hello_world():
  return render_template("home.html")


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
