from flask import Flask, request, render_template, jsonify

from src.common.database import Database
from src.models.entry import Entry
from src.models.parse import parse_data

app = Flask(__name__)

Database.initialize()

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":

        # Get data from user form.
        data = request.form["text_to_parse"]

        # Parse needed data from text, get Entry() object.
        entry = parse_data(data)

        # Get a JSON version of our entry dict.
        data = jsonify(entry.get_json_dict())

        # TODO: If entry already exists for given request ID then do something other than upload again.
        entry.save_to_mongo()

        # Return result template with post request.
        return render_template("result.html", data=data, entry=entry, method="POST")

    return render_template("parse.html")

@app.route("/result", methods=["POST", "GET"])
def result():
    if request.method == "POST":

        # Get form attributes to update entry object.
        comments = request.form["user_comments"]
        idx = request.form["_id"]
        if request.form["decision_radios"] == "pass":
            decision = "PASS"
        else:
            decision = "FAIL"

        # Get our entry from DB in order to update the values.
        myEntry = Entry.from_mongo(idx)

        # Update values.
        myEntry.final_decision = decision
        myEntry.comments = comments

        # Update DB.
        Database.DATABASE["parseTest"].update_one({"_id": idx},
                                                  {"$set": {"Final Decision": decision,
                                                            "Comments": comments}})

        return jsonify(myEntry.get_json_dict())

    return "This is the page for get request."

if __name__ == "__main__":
    app.run(port=5556, debug=True)

