import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('data/diabetes.csv')

# Handle zeros in certain columns
cols_with_zero = ['Glucose','BloodPressure','SkinThickness','Insulin','BMI']
for col in cols_with_zero:
    df[col] = df[col].replace(0, df[col].mean())

# Split dataset
X = df.drop('Outcome', axis=1)
y = df['Outcome']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Save preprocessed data
import joblib
joblib.dump(scaler, 'models/scaler.pkl')
joblib.dump((X_train, X_test, y_train, y_test), 'models/data_split.pkl')
print("Preprocessing complete")
