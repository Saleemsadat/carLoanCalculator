from flask import Flask, render_template, request
from calculator import calculate_monthly_payment

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            principal = float(request.form['principal'])
            rate = float(request.form['rate'])
            years = int(request.form['years'])
            result = calculate_monthly_payment(principal, rate, years)
        except ValueError:
            result = "Invalid input. Please enter numeric values."
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)