from flask import Blueprint, render_template

modal_bp = Blueprint('modal', __name__, 
                          template_folder='templates/',
                          static_folder='static',
                          url_prefix="/modal")

@modal_bp.route('/')
def modal():
    return render_template('modal/index.html', title="Modal")
