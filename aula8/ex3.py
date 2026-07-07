from flask import Flask
from datetime import date

app = Flask(__name__)

@app.route("/data")
def data():
    h = date.today()

    datah = h.strftime("%d/%m/%Y")
    return f"Hoje é: {datah}"

if __name__ == "__main__":
    app.run(debug=True)