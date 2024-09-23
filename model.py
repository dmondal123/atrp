import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import StandardScaler

# Load dataset (assuming it's available as a CSV)
df = pd.read_csv('malicious_software_package_dataset.csv')

# Convert categorical features to numeric
df['file_types'] = df['file_types'].apply(lambda x: len(eval(x)))  # Number of file types
df['known_developer'] = df['known_developer'].astype(int)
df['signing_certificate'] = df['signing_certificate'].astype(int)
df['has_known_vulnerabilities'] = df['has_known_vulnerabilities'].astype(int)
df['presence_of_obfuscated_code'] = df['presence_of_obfuscated_code'].astype(int)
df['contains_network_related_keywords'] = df['contains_network_related_keywords'].astype(int)
df['new_external_dependencies'] = df['new_external_dependencies'].astype(int)
df['sensitive_keywords_detected'] = df['sensitive_keywords_detected'].astype(int)
df['suspicious_file_extension'] = df['suspicious_file_extension'].astype(int)

# Select feature columns and target
features = ['package_size_kb', 'number_of_files', 'file_types', 'known_developer', 
            'signing_certificate', 'size_change_percent', 'number_of_dependencies', 
            'number_of_downloads', 'update_frequency', 'has_known_vulnerabilities', 
            'presence_of_obfuscated_code', 'contains_network_related_keywords', 
            'new_external_dependencies', 'sensitive_keywords_detected', 
            'anomalous_behavior_score', 'suspicious_file_extension']

target = 'is_suspicious'

# Split the data into train and test sets
X = df[features]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train a Random Forest classifier
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)

# Predict on the test set
y_pred = clf.predict(X_test)

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
