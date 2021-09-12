from flask import Flask, render_template

app = Flask(__name__)






@app.route('/')
@app.route('/home')
def home():
    return render_template("login.html")


#creating a dynamic route
@app.route('/about/<foodtypes>')
def about(foodtypes):
    return f"This the about page of  {foodtypes}"


if __name__ == "__main__":
    app.run(debug=True)
