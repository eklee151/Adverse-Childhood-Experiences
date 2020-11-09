from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/abuse')
def abuse():
    return render_template('abuse.html')

@app.route('/household')
def household():
    return render_template('household.html')

@app.route('/neglect')
def neglect():
    return render_template('neglect.html')



if __name__ == '__main__':
    app.run(debug = True)