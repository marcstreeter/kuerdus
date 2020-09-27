from flask import (
    Blueprint,
    jsonify,
)

bp = Blueprint('calendar', __name__)


@bp.route('/', methods=["GET"])
def home():
    return jsonify({"hello": "war"})
