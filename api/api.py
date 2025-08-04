# Importation du module flask
from flask import Flask, jsonify

app = Flask(__name__)

# Activattion du module debug
app.config['DEBUG'] = True

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        'id': 1,
        'name': 'John Doe',
        'email': 'ngasamah@gmail.com'
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)