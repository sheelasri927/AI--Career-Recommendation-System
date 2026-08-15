import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

# Load dataset
data = pd.read_csv("dataset/career_data.csv")

# Features and target
features = [
    "python",
    "machine_learning",
    "web_development",
    "data_science",
    "cloud",
    "cybersecurity"
]

X = data[features]
y = data["career"]

# Convert text values into numbers
encoder = LabelEncoder()

for column in features:
    X[column] = encoder.fit_transform(X[column])

# Encode career names
career_encoder = LabelEncoder()
y_encoded = career_encoder.fit_transform(y)

# Train ML model
model = DecisionTreeClassifier(random_state=42)
model.fit(X, y_encoded)


def recommend_career(
    python,
    machine_learning,
    web_development,
    data_science,
    cloud,
    cybersecurity
):
    user_data = pd.DataFrame([[
        python,
        machine_learning,
        web_development,
        data_science,
        cloud,
        cybersecurity
    ]], columns=features)

    # Convert user input using the same encoders
    for column in features:
        user_data[column] = encoder.fit_transform(
            list(X[column].unique()) + [user_data[column].iloc[0]]
        )[-1]

    prediction = model.predict(user_data)

    return career_encoder.inverse_transform(prediction)[0]