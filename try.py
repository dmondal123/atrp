from langchain_anthropic import ChatAnthropic
from langchain.prompts import ChatPromptTemplate
import json
import pandas as pd
import logging

# Set API Key for Anthropic
from validation.credentials import set_credentials

# Set credentials
ChatAnthropic.api_key = set_credentials()

# Initialize the Claude model (replace model name with the latest available if needed)
model = ChatAnthropic(model_name="claude-3-5-sonnet-20240620", max_tokens=4096)

# Define prompt for generating the dataset
sys_message = """
Generate a JSON dataset for two software packages: one legitimate and one suspicious. Each package should include the following fields:

- package_name: The name of the software package.
- version_number: The version number of the package.
- package_size_kb: The size of the package in kilobytes.
- upload_time: The time when the package was uploaded.
- number_of_files: The total number of files in the package.
- file_types: The types of files contained in the package.
- developer_id: A unique identifier for the developer.
- known_developer: Whether the developer is known (true/false).
- signing_certificate: Whether the package has a valid signing certificate (true/false).
- previous_version_size_kb: The size of the previous version in kilobytes.
- size_change_percent: The percentage size change compared to the previous version.
- number_of_dependencies: Number of dependencies required by the package.
- number_of_downloads: The number of downloads for the package.
- update_frequency: The average time between updates in days.
- hash_of_contents: A hash value of the package content (e.g., SHA-256).
- has_known_vulnerabilities: Whether the package includes known vulnerabilities (true/false).
- presence_of_obfuscated_code: Whether the package contains obfuscated code (true/false).
- contains_network_related_keywords: Whether network-related keywords are present (true/false).
- new_external_dependencies: Whether the current package introduces new external dependencies (true/false).
- sensitive_keywords_detected: Whether sensitive keywords are detected (true/false).
- anomalous_behavior_score: A float score indicating how much the package deviates from previous versions.
- suspicious_file_extension: Whether the package contains files with suspicious extensions (true/false).
- is_suspicious: Whether the package is suspicious (true/false).

Make sure that:
1. At least one package is legitimate with a clean description and common scripts.
2. The other packages may be malicious with hidden or harmful functionality, and the description should clearly reflect its malicious nature.

Ensure the JSON structure is correct and well-formed.

The output should start with :
```json
.......
```
"""

human_message = """
Please generate a dataset of 10 software packages with the specified fields.
"""

# Function to generate a dataset
def generate_dataset():
    try:
        # Prompts to LLM for generating the dataset
        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", sys_message),
                ("human", human_message),
            ]
        )
        
        # Create the chain and invoke the model
        chain = prompt | model
        out = chain.invoke({})
        
        # Debugging: Print the raw response from Claude
        print("Raw output from Claude:\n", out.content)

        # Extract the generated dataset
        dataset_json = out.content

        start_index = dataset_json.find("```json") + len("```json")
        end_index = dataset_json.find("```", start_index)
        
        #Apply filters to extract only the generated test cases
        filtered_dataset = dataset_json[start_index:end_index].strip()
        # Convert JSON string into Python list
        dataset = json.loads(filtered_dataset)
        print(dataset)
        return dataset
    
    except json.JSONDecodeError as e:
        # Log JSON parsing error and show raw response
        logging.error(f"Error parsing JSON: {str(e)}")
        raise
    except Exception as e:
        # Log any other errors encountered during the generation process
        logging.error(f"Error in generating the dataset: {str(e)}")
        raise

# Function to save the dataset to CSV
def save_to_csv(dataset, filename="malicious_software_package_dataset.csv"):
    try:
        # Convert the dataset (list of dictionaries) to a DataFrame
        df = pd.DataFrame(dataset)
        print(df.info())
        # Save DataFrame to a CSV file
        df.to_csv(filename, index=False)
        print(f"Dataset saved to {filename}.")
    
    except Exception as e:
        logging.error(f"Error in saving dataset to CSV: {str(e)}")
        raise

# Main function to generate and save the dataset
def main():
    try:
        # Generate the dataset
        dataset = generate_dataset()

        # Save the dataset to CSV
        save_to_csv(dataset)
    
    except Exception as e:
        logging.error(f"Error in the main execution: {str(e)}")

# Execute the main function
if __name__ == "__main__":
    main()
