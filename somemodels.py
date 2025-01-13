import pandas as pd
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.svm import SVC

def load_and_clean_data(filepath):
    data = pd.read_csv(filepath)
    data = data.dropna()
    return data


def preprocess_data(data):
    data = data.replace(',', '', regex=True)
    data.iloc[:, :-2] = data.iloc[:, :-2].apply(pd.to_numeric, errors='coerce')
    
    data = data.fillna(0)  
    data = data.infer_objects(copy=False)  
    scaler = StandardScaler()
    data_scaled = data.iloc[:, :-2]
    data_scaled = scaler.fit_transform(data_scaled)
    
    encoder = LabelEncoder()
    data_encoded = data.iloc[:, -2:].apply(encoder.fit_transform)
    
    processed_data = pd.DataFrame(data_scaled, columns=data.columns[:-2])
    processed_encoded = pd.DataFrame(data_encoded, columns=data.columns[-2:])
    final_data = pd.concat([processed_data, processed_encoded], axis=1)
    final_data = final_data.dropna()
    
    return final_data



def train_and_evaluate_model(final_data, target_column):
    X = final_data.drop(columns=[target_column]) 
    y = final_data[target_column]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)


    rf_model = RandomForestClassifier(random_state=42)
    rf_model.fit(X_train, y_train)
    rf_predictions = rf_model.predict(X_test)
    rf_accuracy = accuracy_score(y_test, rf_predictions)
    print(f"Random Forest Accuracy (Target: {target_column}): {rf_accuracy * 100:.2f}%")


    gb_model = GradientBoostingClassifier(random_state=42)
    gb_model.fit(X_train, y_train)
    gb_predictions = gb_model.predict(X_test)
    gb_accuracy = accuracy_score(y_test, gb_predictions)
    print(f"Gradient Boosting Accuracy (Target: {target_column}): {gb_accuracy * 100:.2f}%")


    svm_model = SVC(random_state=42)
    svm_model.fit(X_train, y_train)
    svm_predictions = svm_model.predict(X_test)
    svm_accuracy = accuracy_score(y_test, svm_predictions)
    print(f"support vector machine (Target: {target_column}): {svm_accuracy * 100:.2f}%")
    return rf_accuracy , gb_accuracy , svm_accuracy




def main():
    filepath = r"./data.csv"

    # Load and preprocess data
    data = load_and_clean_data(filepath)
    print(data)
    final_data = preprocess_data(data)
    print(final_data)
    target_column = "Do you believe that playing violent video games can lead to aggressive behavior in real life?"
    train_and_evaluate_model(final_data, target_column)

if __name__ == "__main__":
    main()

