from flask import Flask, render_template, request

app = Flask(__name__)

# Helper function to clean dollar-formatted inputs
def clean_currency(value):
    return float(value.replace('$', '').replace(',', '').strip())

@app.route("/", methods=["GET", "POST"])
def calculate():
    if request.method == "POST":
        try:
            price = clean_currency(request.form["price"])
            down_payment = clean_currency(request.form["down_payment"])
            tax_rate = float(request.form["tax_rate"])
            rate = float(request.form["rate"])
            years = int(request.form["years"])

            tax_amount = (price - down_payment) * (tax_rate / 100)
            loan_amount = price - down_payment + tax_amount

            monthly_interest_rate = rate / 100 / 12
            number_of_payments = years * 12
            monthly_payment = (
                loan_amount * monthly_interest_rate /
                (1 - (1 + monthly_interest_rate) ** -number_of_payments)
            )

            return render_template("index.html",
                                   principal=price,
                                   down_payment=down_payment,
                                   tax_rate=tax_rate,
                                   tax_amount=tax_amount,
                                   loan_amount=loan_amount,
                                   rate=rate,
                                   years=years,
                                   monthly_payment=monthly_payment)
        except Exception as e:
            return f"An error occurred: {e}", 400
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
