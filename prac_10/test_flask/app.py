from flask import Flask

app = Flask(__name__)


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return "Hello {}".format(name)


@app.route('/f_to_c/')
@app.route('/f_to_c/<fahrenheit>')
def f_to_c(fahrenheit=""):
    if fahrenheit == "":
        return "Please provide fahrenheit number."

    fahrenheit = float(fahrenheit)
    result = 5 / 9 * (fahrenheit - 32)
    return "{} fahrenheit is equal to {} celsius".format(fahrenheit, result)


@app.route('/c_to_f/')
@app.route('/c_to_f/<celsius>')
def c_to_f(celsius=""):
    if celsius == "":
        return "Please provide celsius number."
    celsius = float(celsius)
    result = celsius * 9.0 / 5 + 32
    return "{} celsius is equal to {} fahrenheit".format(celsius, result)


if __name__ == '__main__':
    app.run()
