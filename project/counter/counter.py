from flask import Blueprint, render_template

counter_bp = Blueprint('counter', __name__, 
                          template_folder='templates', 
                          static_folder='static',
                          url_prefix="/counter")

@counter_bp.route('/counter')
def counter():
    return render_template('counter/index.html', title="Counter")
