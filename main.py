from flask import Flask, render_template
import pandas as pd

app = Flask("__name__")

# When the user visits this url def home() function is called
# "@" means a decorator which connects to that function

# If the user does not enter anything and just clicks the ip address
# "/" just this is given this directs us to the home.html page in templates

stations = pd.read_csv("data_small/stations.txt", skiprows=17)
stations = stations[["STAID", "STANAME                                 "]]
@app.route("/")
def home():
    return render_template("home.html", data=stations.to_html())


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    # zfill("number of zeros you need before a string")
    # makes the string added with zeros infront.
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
    return {"Station": station,
            "Date": date,
            "Temperature": temperature}
#print
@app.route("/api/v1/<station>")
def all_data(station):
    # zfill("number of zeros you need before a string")
    # makes the string added with zeros infront.
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    result = df.to_dict(orient="records")
    return result

@app.route("/api/v1/yearly/<station>/<year>")
def yearly(station, year):
    # zfill("number of zeros you need before a string")
    # makes the string added with zeros infront.
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20)
    df["    DATE"] = df["    DATE"].astype(str)
    result = df[df["    DATE"].str.startswith(str(year))].to_dict(orient="records")
    return result
# This will allow us to see the errors on webpage
app.run(debug=True)