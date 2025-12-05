from flask import Flask, request, render_template

app = Flask(name)

@app.route("/")
def bmi():
    if "weight" in request.args and "height" in request.args:
        w = float(request.args["weight"])
        h = float(request.args["height"]) / 100
        bmi = w / (h*h)

        # تعیین وضعیت BMI
        if bmi < 18.5:
            status = "کمبود وزن 😐"
        elif 18.5 <= bmi < 24.9:
            status = "وزن نرمال 🙂"
        elif 25 <= bmi < 29.9:
            status = "اضافه وزن 😕"
        else:
            status = "چاقی 😞"

        return render_template

app.run()
