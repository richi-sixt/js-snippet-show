from flask import Blueprint, render_template

pagescroller_bp = Blueprint('pagescroller', __name__, 
                          template_folder='templates', 
                          static_folder='static',
                          url_prefix="/pagescroller")

@pagescroller_bp.route('/pagescroller')
def pagescroller():
    return render_template('pagescroller/index.html', title="Page Scroller")