from flask import Flask, render_template, request

app = Flask(__name__)

stocks = [
    ["Reliance", 10, 2500],
    ["TCS", 5, 3800],
    ["HDFC Bank", 8, 1700],
    ["Infosys", 12, 1500],
    ["ICICI Bank", 15, 1100],
    ["Axis Bank", 20, 1000],
    ["SBI", 25, 850],
    ["Wipro", 18, 500],
    ["Tata Motors", 10, 900],
    ["Asian Paints", 7, 3000],
    ["Bajaj Finance", 6, 7000],
    ["L&T", 5, 3400],
    ["Maruti Suzuki", 4, 12000],
    ["HCL Tech", 9, 1600],
    ["UltraTech Cement", 3, 11000],
    ["ITC", 30, 450],
    ["Sun Pharma", 15, 1800],
    ["Nestle India", 2, 25000],
    ["Adani Ports", 10, 1400],
    ["Titan", 6, 3500]
]

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        stock_name = request.form["stock_name"]
        shares = request.form["shares"]
        price = request.form["price"]

        stocks.append([stock_name, shares, price])

    total_investment = 52000
    current_value = 58000
    profit = current_value - total_investment

    return render_template(
        "index.html",
        investment=total_investment,
        value=current_value,
        profit=profit,
        stocks=stocks
    )

if __name__ == "__main__":
    app.run(debug=True)