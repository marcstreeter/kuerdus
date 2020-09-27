import logging

from flask import (
    Blueprint,
    jsonify,
)

logger = logging.getLogger(__name__)
bp = Blueprint('messenger', __name__)


@bp.route('/', methods=["GET"])
def home():
    logger.error("yoo dawg I heard you wanted logging sooo")
    return jsonify({"hello": "world"})
