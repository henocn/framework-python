from flask import Flask

app = Flask(__name__)

# Activattion du module debug
app.config['DEBUG'] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distance reading of size fiction novels</p>"

if __name__ == 'api':
    app.run(port=5000)