from flask import Flask, render_template, request

app = Flask(__name__)

# Helper function to clean dollar-formatted inputs
def clean_currency(value):
    return float(value.replace('$', '').replace(',', '').strip())

@app.route("/", methods=["GET", "POST"])
def calculate():
    if request.method == "POST":
        try:
            # Clean and parse values
            principal = clean_currency(request.form["principal"])
            down_payment = clean_currency(request.form["down_payment"])
            tax_rate = float(request.form["tax_rate"])
            rate = float(request.form["rate"])
            years = int(request.form["years"])

            # Apply tax to vehicle price
            tax_amount = principal * (tax_rate / 100)
            total_with_tax = principal + tax_amount

            # Subtract down payment
            loan_amount = total_with_tax - down_payment

            # Monthly interest rate
            monthly_rate = rate / 100 / 12
            months = years * 12

            # Monthly payment formula
            if monthly_rate == 0:
                monthly_payment = loan_amount / months
            else:
                monthly_payment = loan_amount * (monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)

            return render_template(
                "index.html",
                monthly_payment=monthly_payment,
                principal=principal,
                down_payment=down_payment,
                tax_rate=tax_rate,
                rate=rate,
                years=years,
                loan_amount=loan_amount,
                tax_amount=tax_amount,
            )
        except Exception as e:
            return f"An error occurred: {str(e)}"

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
