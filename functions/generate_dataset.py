import json
import logging
from langchain.prompts import ChatPromptTemplate
from prompts.default_prompts import human_message
from prompts.sys_prompts import sys_message
from model.claude_model import model

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
        
        # Debugging: Print the raw response from the model
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
