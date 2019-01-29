from flask import Flask, request, render_template, jsonify, redirect

from src.models.parse import parse_data

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        # Get data from user form.
        data = request.form["text_to_parse"]
        # Parse needed data from text, get Entry() object.
        entry = parse_data(data)

        data = jsonify(entry.get_json_dict())
        # Insert entry into database.
        # Database.insert("test", results.json())
        # Return result template with post request.
        return render_template("result.html", data=data, entry=entry, method="POST")

    return render_template("parse.html")

@app.route("/result", methods=["POST", "GET"])
def result():
    if request.method == "POST":

        # Get form attributes to update entry object.
        comments = request.form["user_comments"]
        idx = request.form["entry_idx"]
        if request.form["decision_radios"] == "pass":
            decision = "PASS"
        else:
            decision = "FAIL"

        # Get our entry from DB in order to update the values.
        # Update values.
        # Update DB.
        return decision

    return "This is the page for get request."

if __name__ == "__main__":
    app.run(port=5556, debug=True)

