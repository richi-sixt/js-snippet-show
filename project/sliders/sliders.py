from flask import Blueprint, render_template

sliders_bp = Blueprint('sliders', __name__, 
                          template_folder='templates', 
                          static_folder='static',
                          url_prefix="/sliders")


@sliders_bp.route('/static-slider')
def static_slider():
    return render_template('sliders/static.html', title="Sliders: static")

@sliders_bp.route('/dynamic-slider')
def dynamic_slider():
    return render_template('sliders/dynamic.html', title="Sliders: dynamic")

