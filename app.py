from flask import Flask, render_template, request
import random

app = Flask(__name__)

def generate_troll_text(name, age, github=None, facebook=None, portfolio=None):
    dev_phrases = [
        f"{name} thinks they are a coding wizard, but their GitHub is just a graveyard of projects! Check it out: {github}.",
        f"Breaking news: {name} is still using a potato for a computer! Their latest project? A fancy notepad! GitHub: {github}.",
        f"Did you know {name}'s latest project crashed before it even launched? Check their GitHub for the evidence: {github}.",
        f"If bad setups were an Olympic sport, {name} would win gold! Check out their portfolio: {portfolio}.",
        f"Rumor has it {name} is still trying to figure out how to use GitHub properly! Maybe check their profile: {github}."
    ]
    return random.choice(dev_phrases)

@app.route("/", methods=["GET", "POST"])
def home():
    troll_text = None
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        github = request.form.get("github", "No GitHub provided")
        facebook = request.form.get("facebook", "No Facebook provided")
        portfolio = request.form.get("portfolio", "No Portfolio provided")

        troll_text = generate_troll_text(name, age, github, facebook, portfolio)

    return render_template("index.html", troll_text=troll_text)

if __name__ == "__main__":
    app.run(debug=True)
