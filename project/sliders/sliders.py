from flask import Blueprint, render_template

sliders_bp = Blueprint('sliders', __name__, 
                          template_folder='templates', 
                          static_folder='static',
                          url_prefix="/sliders")

@sliders_bp.route('/')
def sliders():
    return render_template('sliders/index.html', title="Sliders: one")