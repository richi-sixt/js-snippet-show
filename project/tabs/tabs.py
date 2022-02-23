from flask import Blueprint, render_template

tabs_bp = Blueprint('tabs', __name__, 
                          template_folder='templates', 
                          static_folder='static',
                          url_prefix="/tabs")

@tabs_bp.route('/tabs')
def tabs():
    return render_template('tabs/index.html', title="JS Tabs")