from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/api/data', methods=['GET', 'POST'])
def api_data():
    if request.method == 'GET':
        return {"message": "GET request to /api/data successful."}
    else:
        return {"message": "This method is not allowed."}, 405

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
