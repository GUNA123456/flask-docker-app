from flask import Flask, jsonify, send_from_directory

app = Flask(__name__, static_folder='static')

def make_response(status, message, data=None):
    response = {"status": status, "message": message}
    if data is not None:
        response["data"] = data
    return jsonify(response)

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/about')
def about_page():
    return send_from_directory('static', 'about.html')

@app.route('/info')
def info_page():
    return send_from_directory('static', 'info.html')

# API endpoints serve JSON
@app.route('/api/about')
def about_api():
    return make_response(
        "success",
        "About Page",
        {
            "details": "This endpoint describes the application",
            "version": "1.0"
        }
    )

@app.route('/api/info')
def info_api():
    return make_response(
        "success",
        "App Info",
        {"owner": "Alice"}
    )

# Error handler, etc...

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)
