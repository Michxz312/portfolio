from flask import Flask, render_template, request
from scheduling_project import scheduling_bp

app = Flask(__name__)
app.register_blueprint(scheduling_bp)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/project')
def project():
    return render_template('projects/project.html')

if __name__ == '__main__':
    app.run(debug = True)