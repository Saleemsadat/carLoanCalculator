from flask import Flask, render_template, request
from calculator import calculate_monthly_payment

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST':
        principal = float(request.form['principal'])
        down_payment = float(request.form['down_payment'])
        rate = float(request.form['rate']) / 100 / 12
        years = int(request.form['years'])
        months = years * 12

        loan_amount = principal - down_payment

        if rate == 0:
            monthly_payment = loan_amount / months
        else:
            monthly_payment = loan_amount * rate * (1 + rate)**months / ((1 + rate)**months - 1)

        return render_template('index.html', result=round(monthly_payment, 2))

    return render_template('index.html')
