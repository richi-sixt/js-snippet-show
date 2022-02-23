from flask import Flask, render_template
from project.colorflipper.color_flipper import colorflipper_bp
from project.counter.counter import counter_bp
from project.review.review import review_bp
from project.modal.modal import modal_bp
from project.faq.faq import faq_bp
from project.filter.filter import filter_bp
from project.pagescroller.pagescroller import pagescroller_bp
from project.tabs.tabs import tabs_bp
from project.sliders.sliders import sliders_bp

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
@app.route("/index", methods=['GET', 'POST'])
def index():
    return render_template('index.html', title="Home")

app.register_blueprint(colorflipper_bp)
app.register_blueprint(counter_bp)
app.register_blueprint(review_bp)
app.register_blueprint(modal_bp)
app.register_blueprint(faq_bp)
app.register_blueprint(filter_bp)
app.register_blueprint(pagescroller_bp)
app.register_blueprint(tabs_bp)
app.register_blueprint(sliders_bp)