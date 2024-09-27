from flask import Blueprint

event_blueprint = Blueprint('events', __name__)

@event_blueprint.route('/events', methods=['GET'])
def get_events():
    return {"events": "List of all events"}

