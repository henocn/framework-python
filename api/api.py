from flask import Flask

app = Flask(__name__)

app.config['DEBUG'] = True


@app.route('/favicon.ico', methods=['GET'])
def favicon():
    return app.send_static_file('favicon.ico')



@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distance reading of size fiction novels</p>"

app.run(port=5000)