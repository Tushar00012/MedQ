# train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import joblib

# Sample categories and their priority scores based on severity
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

# Generate sample data
data = []
for category, priority in category_priority.items():
    for age in range(0, 101, 10):  # Age groups from 0 to 100
        data.append([age, category, priority])

# Create DataFrame
df = pd.DataFrame(data, columns=['age', 'category', 'priority'])

# Convert categorical data to numeric for ML model
df['category'] = df['category'].astype('category').cat.codes

# Split data
X = df[['age', 'category']]
y = df['priority']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, 'priority_model.pkl')
print("Model trained and saved as 'priority_model.pkl'")
