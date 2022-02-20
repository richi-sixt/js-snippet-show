from flask import Blueprint, render_template

faq_bp = Blueprint('faq', __name__, 
                          template_folder='templates', 
                          static_folder='static',
                          url_prefix="/faq")

@faq_bp.route('/')
def faq():
    return render_template('faq/index.html', title="FAQ")
