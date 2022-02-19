from flask import Blueprint, render_template

colorflipper_bp = Blueprint('colorflipper', __name__, 
                          template_folder='templates', 
                          static_folder='static',
                          url_prefix="/colorflipper")

@colorflipper_bp.route('/simple')
def simple():
    return render_template('colorflipper/index.html', title="Color Flipper")

@colorflipper_bp.route('/hex')
def hex():
    return render_template('colorflipper/hex.html', title="Color Flipper")