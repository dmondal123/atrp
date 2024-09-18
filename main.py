import logging
from functions.generate_dataset import generate_dataset
from functions.save_to_csv import save_to_csv

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
