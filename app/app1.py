from flask import Flask, render_template, request, redirect, url_for
import json
import joblib

app = Flask(__name__, static_url_path='/static')

appointments = []

categories = [
    {"name": "Covid", "image": "images/coronavirus.png"},
    {"name": "Skin and Hair", "image": "images/allergy.png"},
    {"name": "Women Health", "image": "images/woman.png"},
    {"name": "General Physician", "image": "images/stethoscope.png"},
    {"name": "Dental Care", "image": "images/floss.png"},
    {"name": "Bones and Joints", "image": "images/pain-in-joints.png"},
    {"name": "Mental Wellness", "image": "images/mental-health.png"},
    {"name": "Ear, Nose & Throat", "image": "images/sore-throat.png"},
    {"name": "Sexual Health", "image": "images/std.png"},
    {"name": "Child Specialist", "image": "images/specialist.png"},
    {"name": "Homeopathy", "image": "images/homeopathy.png"},
    {"name": "Digestive Issues", "image": "images/heart-problem.png"},
    {"name": "Eye Specialist", "image": "images/ophtalmology.png"},
    {"name": "Heart", "image": "images/heart-attack.png"},
    {"name": "Physiotherapy", "image": "images/physical-therapy.png"},
    {"name": "Brain & Nerves", "image": "images/brain.png"},
    {"name": "Lungs & Breathing", "image": "images/lungs.png"},
    {"name": "Kidney Issues", "image": "images/kidney.png"},
    {"name": "General Surgery", "image": "images/plastic-surgery.png"},
    {"name": "Diabetes Management", "image": "images/sugar-blood-level.png"},
    {"name": "Ayurveda", "image": "images/ayurveda.png"},
    {"name": "Cancer", "image": "images/breast-cancer.png"},
    {"name": "Urinary Issues", "image": "images/bladder.png"},
    {"name": "Veterinary", "image": "images/veterinary.png"},
    {"name": "Diet & Nutrition", "image": "images/diet.png"}


]
category_priority = {
    "Covid": 5,
    "Skin and Hair": 1,
    "Women Health": 3,
    "General Physician": 2,
    "Dental Care": 2,
    "Bones and Joints": 3,
    "Mental Wellness": 4,
    "Ear, Nose & Throat": 2,
    "Sexual Health": 4,
    "Child Specialist": 4,
    "Homeopathy": 1,
    "Digestive Issues": 3,
    "Eye Specialist": 2,
    "Heart": 5,
    "Physiotherapy": 2,
    "Brain & Nerves": 5,
    "Lungs & Breathing": 4,
    "Kidney Issues": 4,
    "General Surgery": 5,
    "Diabetes Management": 3,
    "Ayurveda": 1,
    "Cancer": 5,
    "Urinary Issues": 3,
    "Veterinary": 2,
    "Diet & Nutrition": 2
}




@app.route('/add_appointment', methods=['POST'])
def add_appointment():
    data = request.json  # Receive the data from the frontend
    if not data:
        return 'No data received', 400

    for key, patient in data.items():
        name = patient.get('patient_name', 'Unknown')
        age = int(patient.get('age', 0))
        category = patient.get('concern', 'General Physician')
        symptoms = patient.get('symptoms', [])

        # Get priority from category_priority dictionary
        priority = category_priority.get(category, 1)  # Default to 1 if category not found

        # Add appointment to the list with the calculated priority
        appointments.append({
            "name": name,
            "age": age,
            "category": category,
            "symptoms": symptoms,
            "priority": priority
        })

    # Sort appointments based on priority (higher priority first)
    appointments.sort(key=lambda x: x['priority'], reverse=True)

    return redirect(url_for('schedule'))


@app.route('/schedule')
def schedule():
    return render_template('schedule.html', appointments=appointments)

if __name__ == '__main__':
    app.run(debug=True)
