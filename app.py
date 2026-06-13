from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/affiliates')
def affiliates():
    return render_template('affiliates.html')

@app.route('/campaigns')
def campaigns():
    return render_template('campaigns.html')

@app.route('/reports')
def reports():
    return render_template('reports.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/support')
def support():
    return render_template('support.html')

@app.route('/members')
def members():
    return render_template('members.html')

if __name__ == '__main__':
    app.run(debug=True)
