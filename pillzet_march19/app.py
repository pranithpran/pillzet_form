from flask import Flask, request, jsonify, render_template
import csv
import os

app = Flask(__name__)

# Define CSV file path
CSV_FILE = "pillzet_data.csv"

# Ensure the CSV file has a header if it doesn't exist
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Age", "Email", "Phone", "Smoke", "Drink", "Exercise", 
                         "Diet", "Checkups", "Stress", "Sleep", "Water", "Medical History", 
                         "Tablets", "Delivery Option", "Problems", "Health Score", "Health Status"])

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/save", methods=["POST"])
def save_data():
    try:
        data = request.get_json()

        # Extract data from request
        row = [
            data.get("name"), data.get("age"), data.get("email"), data.get("phone"),
            data.get("smoke"), data.get("drink"), data.get("exercise"), data.get("diet"),
            data.get("checkups"), data.get("stress"), data.get("sleep"), data.get("water"),
            data.get("medicalHistory"), data.get("tablets"), data.get("Deliver_opt"),
            data.get("problems"), data.get("healthScore"), data.get("healthStatus")
        ]

        # Write data to CSV
        with open(CSV_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(row)

        return jsonify({"message": "Data saved successfully!"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
