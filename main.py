import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

warnings.filterwarnings('ignore')

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def clean_data(df):
    df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')
    df['What is your age?'] = pd.to_numeric(df['What is your age?'], errors='coerce')
    categorical_cols = df.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        df[col].fillna(df[col].mode()[0], inplace=True)
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        df[col].fillna(df[col].median(), inplace=True)

    return df

def exploratory_data_analysis(df):
    sns.histplot(df['What is your age?'], bins=20, kde=True)
    plt.title('Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.show()
    sns.countplot(x='Gender', data=df)
    plt.title('Gender Distribution')
    plt.xlabel('Gender')
    plt.ylabel('Count')
    plt.show()
    numeric_df = df.select_dtypes(include=[np.number])
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap')
    plt.show()

def prepare_data(df):
    X = df.drop(columns=['Do you believe that playing violent video games can lead to aggressive behavior in real life?'])
    y = df['Do you believe that playing violent video games can lead to aggressive behavior in real life?']
    X = pd.get_dummies(X, drop_first=True)
    X = X.drop(columns=['Timestamp'])

    return X, y

def train_and_evaluate_model(X_train, X_test, y_train, y_test):
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    conf_matrix = confusion_matrix(y_test, y_pred)

    return accuracy, conf_matrix

def main(file_path):
    df = load_data(file_path)
    df = clean_data(df)
    exploratory_data_analysis(df)
    X, y = prepare_data(df)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    accuracy, conf_matrix = train_and_evaluate_model(X_train, X_test, y_train, y_test)
    print(f"Model Accuracy: {accuracy * 100:.2f} %")
    print(f"Confusion Matrix:\n{conf_matrix}")

if __name__ == "__main__":
    file_path = r'.\Effects of Violent Video Games On Aggression CSV MSDOS (2).csv'
    main(file_path)
