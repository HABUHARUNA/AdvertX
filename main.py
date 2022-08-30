from flask import Flask, render_template

main = Flask(__name__)


@main.route("/")
@main.route("/home")
def home():
    return render_template("home.html")

@main.route("/services")
def services():
    return render_template("services.html")


@main.route("/about")
def about_us():
    return render_template("about_us.html")


@main.route("/contact")
def contact_us():
    return render_template("contact_us.html")


@main.route("/signup")
def signup():
    return render_template("signup.html")


@main.route("/login", methods = ["GET", "POST"])
def login():
    return render_template("login.html")

if __name__ == "__main__":
    main.run(debug=True)