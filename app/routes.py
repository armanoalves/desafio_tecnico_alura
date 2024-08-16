from flask import Blueprint
from app.controllers import create_feedback, get_feedbacks, create_sentiment, get_sentiments

bp = Blueprint('bp', __name__)

bp.route('/feedback', methods=['POST'])(create_feedback)
bp.route('/feedbacks', methods=['GET'])(get_feedbacks)
bp.route('/sentiment', methods=['POST'])(create_sentiment)
bp.route('/sentiments', methods=['GET'])(get_sentiments)
