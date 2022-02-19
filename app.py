from flask import Flask, render_template
from project.colorflipper.color_flipper import colorflipper_bp
from project.counter.counter import counter_bp

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
@app.route("/index", methods=['GET', 'POST'])
def index():
    return render_template('index.html', title="Home")

app.register_blueprint(colorflipper_bp)
app.register_blueprint(counter_bp)