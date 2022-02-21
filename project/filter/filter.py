from flask import Blueprint, render_template

filter_bp = Blueprint('filter', __name__, 
                          template_folder='templates/',
                          static_folder='static',
                          url_prefix="/filter")

@filter_bp.route('/')
def filter():
    return render_template('filter/index.html', title="Filter")
