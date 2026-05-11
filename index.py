from flask import Flask, render_template, request
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from device import Device

from attacks import (
    sniff_data,
    brute_force_attack,
    mitm_attack,
    replay_attack,
    injection_attack
)

from defence import apply_defence
from risk import assess_risk

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)


def run_simulation(attack_type):

    device = Device()

    data = device.generate_data()

    original_data = data.copy()

    if attack_type == "Sniffing":

        attacked = sniff_data(data)

    elif attack_type == "Brute Force":

        attacked = brute_force_attack()

    elif attack_type == "MITM":

        attacked = mitm_attack(data)

    elif attack_type == "Replay":

        attacked = replay_attack(data)

    elif attack_type == "Injection":

        attacked = injection_attack()

    else:

        attacked = {"error": "Unknown attack"}

    secured = apply_defence(
        attacked,
        attack_type,
        original_data
    )

    risk = assess_risk(
        original_data,
        attacked,
        secured,
        attack_type
    )

    return {
        "original": original_data,
        "attacked": attacked,
        "secured": secured,
        "risk": risk["level"],
        "score": risk["score"],
        "recommendations": risk["recommendations"]
    }


@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        attack = request.form["attack"]

        result = run_simulation(attack)

    return render_template(
        "index.html",
        result=result
    )


app.debug = False

if __name__ == "__main__":
    app.run(debug=True)