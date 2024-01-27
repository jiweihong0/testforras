# write flask api here

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def api():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        return jsonify(data)
@app.route('/api', methods=['GET'])
def apia():
    if request.method == 'GET':
        data ={
            'message': 'Hello World!'
        }
        return jsonify(data)
    
    
if __name__ == '__main__':
    app.run(debug=True)
