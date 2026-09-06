import pandas as pd
import joblib


MODEL_FILE = "models/placement_model.pkl"


# Load trained model
model = joblib.load(MODEL_FILE)


def predict_placement(student_data):

    # Convert student data into DataFrame
    student_df = pd.DataFrame([student_data])

    # Make prediction
    prediction = model.predict(student_df)[0]

    # Get prediction probabilities
    probabilities = model.predict_proba(student_df)[0]

    # Find probability corresponding to class 1 (Placed)
    class_index = list(model.classes_).index(1)

    placement_probability = probabilities[class_index] * 100

    # Determine readiness level
    if placement_probability >= 75:
        readiness = "High"

    elif placement_probability >= 50:
        readiness = "Medium"

    else:
        readiness = "Low"

    return {
        "prediction": int(prediction),
        "placement_probability": round(
            placement_probability, 2
        ),
        "readiness": readiness
    }