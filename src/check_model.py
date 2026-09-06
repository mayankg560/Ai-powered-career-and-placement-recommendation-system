import joblib

model = joblib.load("models/placement_model.pkl")

print("\nMODEL TYPE:")
print(type(model))

print("\nMODEL CLASSES:")
print(model.classes_)

print("\nMODEL STEPS:")
print(model.named_steps)

print("\n" + "=" * 60)
print("MODEL CHECK COMPLETE")
print("=" * 60)