from flask import Flask, jsonify

app = Flask(__name__)

def make_response(status, message, data=None):
    response = {"status": status, "message": message}
    if data is not None:
        response["data"] = data
    return jsonify(response)

@app.route('/')
def hello():
    return make_response(
        "success",
        "Hello, World!",
        {"details": "This is the home page response"}
    )

@app.route('/about')
def about():
    return make_response(
        "success",
        "About Page",
        {
            "details": "This endpoint describes the application",
            "version": "1.0"
        }
    )

@app.route('/info')
def info():
    return make_response(
        "success",
        "App Info",
        {"owner": "Alice"}
    )

# Example error handler
@app.errorhandler(404)
def not_found(e):
    return make_response(
        "error",
        "Endpoint not found",
        None
    ), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
