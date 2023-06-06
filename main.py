from flask import Flask, render_template


app = Flask("__name__")

# When the user visits this url def home() function is called
# "@" means a decorator which connects to that function

# If the user does not enter anything and just clicks the ip address
# "/" just this is given this directs us to the home.html page in templates
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    temperature = 23
    return {"Station" : station,
            "Date" : date,
            "Temperature" : temperature}




# This will allow us to see the errors on webpage
app.run(debug=True)