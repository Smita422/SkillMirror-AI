import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Load dataset
data = pd.read_csv("career_data.csv")

X = data[['Python', 'ML', 'Communication', 'Projects']]
y = data['Role']

# Train model
model = DecisionTreeClassifier()

model.fit(X, y)

# Prediction function
def predict_career(
    python_skill,
    ml_skill,
    communication,
    projects
):

    input_data = pd.DataFrame([[
        python_skill,
        ml_skill,
        communication,
        projects
    ]], columns=[
        'Python',
        'ML',
        'Communication',
        'Projects'
    ])

    prediction = model.predict(input_data)

    return prediction[0]