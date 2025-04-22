def calculate_monthly_payment(principal, annual_rate, years):
    r = annual_rate / 12 / 100
    n = years * 12
    if r == 0:
        return round(principal / n, 2)
    monthly_payment = principal * r * (1 + r) ** n / ((1 + r) ** n - 1)
    return round(monthly_payment, 2)