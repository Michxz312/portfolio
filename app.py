from flask import Flask, render_template, request
from scheduling_project import scheduling_bp
from assignment_project import assignment_bp
from kanji_game import kanji_game_bp
from scheduling_project.seed import seed
from dotenv import load_dotenv

app = Flask(__name__)
app.register_blueprint(scheduling_bp)
app.register_blueprint(assignment_bp)
app.register_blueprint(kanji_game_bp)

load_dotenv()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/project')
def project():
    return render_template('projects/project.html')

@app.route('/project/revenue')
def revenue():
    return render_template('projects/revenue.html')

@app.route('/project/lp')
def lp():
    return render_template('projects/LP/LP.html')

@app.route('/project/meal')
def meal():
    return render_template('projects/meal.html')

if __name__ == '__main__':
    seed()
    app.run(debug = True)