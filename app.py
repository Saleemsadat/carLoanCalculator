from flask import Flask, render_template, request
from calculator import calculate_monthly_payment

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST':
        principal = float(request.form['principal'])
        down_payment = float(request.form['down_payment'])
        tax_rate = float(request.form.get('tax_rate', 0)) / 100
        rate = float(request.form['rate']) / 100 / 12
        years = int(request.form['years'])
        months = years * 12

        tax = principal * tax_rate
        total_price_with_tax = principal + tax
        loan_amount = total_price_with_tax - down_payment

        if rate == 0:
            monthly_payment = loan_amount / months
        else:
            monthly_payment = loan_amount * rate * (1 + rate) ** months / ((1 + rate) ** months - 1)

        return render_template(
            'index.html',
            result=round(monthly_payment, 2),
            loan_amount=round(loan_amount, 2),
            principal=principal,
            down_payment=down_payment,
            tax_rate=tax_rate * 100,
            rate=round(rate * 12 * 100, 2),
            years=years
        )

    return render_template('index.html')

# 🔥 This is the important part!
if __name__ == '__main__':
    app.run(debug=True)