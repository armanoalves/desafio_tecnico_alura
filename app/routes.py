from flask import Blueprint
from app.controllers import get_feedbacks, get_sentiments, openai_analyzer

bp = Blueprint('bp', __name__)

bp.route('/openai_analizer', methods=['POST'])(openai_analyzer)
bp.route('/feedbacks', methods=['GET'])(get_feedbacks)
bp.route('/sentiments', methods=['GET'])(get_sentiments)
