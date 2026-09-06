import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
os.makedirs("outputs", exist_ok=True)
df=pd.read_csv("data/raw/campus_placement_data.csv")
plt.figure(figsize=(6,4))
sns.countplot(x="placed", data=df)
plt.title("Placement Status Distribution")
plt.xlabel("Placement Status")
plt.ylabel("Number of Students")

plt.savefig("outputs/placement_distribution.png")
plt.close()


# 2. CGPA/Degree Percentage vs Placement
plt.figure(figsize=(7, 5))

sns.boxplot(
    data=df,
    x="placed",
    y="degree_percentage"
)

plt.title("Degree Percentage vs Placement")

plt.savefig("outputs/degree_vs_placement.png")
plt.close()


# 3. Internship Count vs Placement
plt.figure(figsize=(7, 5))

sns.boxplot(
    data=df,
    x="placed",
    y="internships_count"
)

plt.title("Internships vs Placement")

plt.savefig("outputs/internships_vs_placement.png")
plt.close()


# 4. Aptitude Score vs Placement
plt.figure(figsize=(7, 5))

sns.boxplot(
    data=df,
    x="placed",
    y="aptitude_score"
)

plt.title("Aptitude Score vs Placement")

plt.savefig("outputs/aptitude_vs_placement.png")
plt.close()

print("Graphs successfully saved in outputs folder!")