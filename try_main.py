import logging
from prompts.default_prompts import human_message
from prompts.sys_prompts import sys_message_2
from functions.generate_dataset import generate_dataset
from functions.save_to_csv import save_to_csv

# Main function to generate and save the dataset
import pandas as pd

def main():
    try:
        # Initialize an empty list to store all datasets
        all_datasets = []

        # Loop to generate dataset 250 times
        for i in range(10):
            # Generate the dataset
            dataset = generate_dataset(sys_message_2, human_message)

            # Append the dataset to the list
            all_datasets.extend(dataset)  # Assuming dataset is a list of dictionaries
            print(f"Dataset {i+1} generated")

        # Convert the accumulated data into a DataFrame
        df = pd.DataFrame(all_datasets)

        # Save the combined dataset to a single CSV file
        save_to_csv(df, filename="malicious_software_package_dataset_mistral.csv")
        print("All datasets saved to malicious_software_package_dataset.csv")
    
    except Exception as e:
        logging.error(f"Error in the main execution: {str(e)}")

# Execute the main function
if __name__ == "__main__":
    main()
