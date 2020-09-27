import socket

from flask import (
    Blueprint,
    jsonify,
)

host = str(socket.gethostname())
bp = Blueprint('health', __name__)


@bp.route('/', methods=["GET"])
def home():
    return jsonify({"host": host})
