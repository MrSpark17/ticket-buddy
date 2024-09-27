from flask import Flask, jsonify
from routes.events import event_blueprint
from routes.recommendations import rec_blueprint

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(event_blueprint)
app.register_blueprint(rec_blueprint)

@app.route('/')
def home():
    return jsonify(message="Welcome to Ticket-Buddy API")

if __name__ == '__main__':
    app.run(debug=True)
