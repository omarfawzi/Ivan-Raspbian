from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route("/welcome", methods=['GET'])
def welcome():
    return render_template("index.html")


@app.route("/routes/origin/<origin>/destination/<destination>", methods=['GET'])
def routes(origin, destination):
    response = requests.get('https://mocki.io/v1/345067cf-ed01-49fb-ad1b-537e0d058074')
    return render_template("routes.html", routes=response.json())


@app.route("/success")
def success():
    return render_template("success.html")


@app.route("/test-post", methods= ['POST'])
def postTest():
    return {'data': request.form.get('test_key'), 'success': True}


if __name__ == '__main__':
    app.run()
