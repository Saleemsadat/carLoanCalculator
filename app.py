from flask import Flask, render_template, request

app = Flask(__name__)

def clean_currency(value):
    """Remove $ and , then convert to float."""
    return float(value.replace("$", "").replace(",", "").strip())

@app.route("/", methods=["GET", "POST"])
def calculate():
    if request.method == "POST":
        try:
            vehicle_price = clean_currency(request.form["vehicle_price"])
            down_payment = clean_currency(request.form["down_payment"])
            tax_rate = float(request.form["tax_rate"])
            interest_rate = float(request.form["interest_rate"])
            loan_term = int(request.form["loan_term"])

            tax_amount = vehicle_price * (tax_rate / 100)
            loan_amount = vehicle_price + tax_amount - down_payment
            monthly_interest_rate = (interest_rate / 100) / 12

            if monthly_interest_rate == 0:
                monthly_payment = loan_amount / loan_term
            else:
                monthly_payment = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate) ** loan_term) / \
                                  ((1 + monthly_interest_rate) ** loan_term - 1)

            return render_template(
                "index.html",
                vehicle_price=vehicle_price,
                down_payment=down_payment,
                tax_rate=tax_rate,
                interest_rate=interest_rate,
                loan_term=loan_term,
                principal=loan_amount,
                monthly_payment=monthly_payment,
            )
        except Exception as e:
            return f"An error occurred: {e}"
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
