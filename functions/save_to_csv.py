import pandas as pd
import logging

# Function to save the dataset to CSV
def save_to_csv(dataset, filename):
    try:
        # Convert the dataset (list of dictionaries) to a DataFrame
        df = pd.DataFrame(dataset)
        print(df.info)
        # Save DataFrame to a CSV file
        df.to_csv(filename, index=False)
        print(f"Dataset saved to {filename}.")
    
    except Exception as e:
        logging.error(f"Error in saving dataset to CSV: {str(e)}")
        raise