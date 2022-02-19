from flask import Blueprint, render_template

review_bp = Blueprint('review', __name__, 
                          template_folder='templates/',
                          static_folder='static',
                          url_prefix="/review")

@review_bp.route('/')
def review():
    return render_template('review/index.html', title="Review")
