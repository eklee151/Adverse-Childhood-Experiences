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

@app.route('/cdc-kaiser')
def cdc_kaiser():
    return render_template('cdc-kaiser.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')

@app.route('/faqs')
def faqs():
    return render_template('faqs.html')



if __name__ == '__main__':
    app.run(debug = True)