import pandas as pd
import joblib


model = joblib.load("models/placement_model.pkl")

df = pd.read_csv("data/raw/campus_placement_data.csv")

# Remove target/leakage columns
X = df.drop(
    columns=[
        "student_id",
        "salary_lpa",
        "placed"
    ]
)

# Test the first 10 actual students from the dataset
X_test = X.head(10)

predictions = model.predict(X_test)
probabilities = model.predict_proba(X_test)

print("\n" + "=" * 70)
print("TESTING MODEL ON ACTUAL DATA")
print("=" * 70)

for i in range(10):

    placed_probability = probabilities[i][
        list(model.classes_).index(1)
    ] * 100

    print(
        f"Student {i + 1}: "
        f"Actual={df['placed'].iloc[i]} | "
        f"Predicted={predictions[i]} | "
        f"Probability={placed_probability:.2f}%"
    )

print("=" * 70)
