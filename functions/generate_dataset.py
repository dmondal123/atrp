import transformers
import json
import pandas as pd
import logging
import torch
from langchain.prompts import ChatPromptTemplate

# Set the model ID for LLaMA, which you can replace with the correct version you're using
model_id = "meta-llama/Meta-Llama-3-8B"

# Initialize the LLaMA model and tokenizer using Hugging Face transformers
model = transformers.AutoModelForCausalLM.from_pretrained(model_id)
tokenizer = transformers.AutoTokenizer.from_pretrained(model_id)

# Set up the pipeline for text generation using the loaded model and tokenizer
llama_pipeline = transformers.pipeline(
    task="text-generation", 
    model=model, 
    tokenizer=tokenizer,
    device=0 if torch.cuda.is_available() else -1,
    max_new_tokens=8192  # Use GPU if available, otherwise CPU
)

# Function to generate a dataset
def generate_dataset(sys_message, human_message):
    try:

        # Prompts to LLM for generating the dataset
        prompt = ChatPromptTemplate.from_messages([
            ("system", sys_message),
            ("human", human_message),
        ])

        # Invoke the model pipeline with the prompt and get the response
        prompt_text = f"{sys_message} {human_message}"
        response = llama_pipeline(prompt_text, max_new_tokens=4096)

        # Debugging: Print the raw response from the model
        print("Raw output from LLaMA:\n", response[0]["generated_text"])

        # Extract the generated dataset
        dataset_json = response[0]["generated_text"]
        # Locate JSON content between the code block markers (```json and ```)
        start_index = dataset_json.find("``json`") + len("```json")
        end_index = dataset_json.find("```", start_index)
        
        # Extract and clean up the dataset from the response
        filtered_dataset = dataset_json[start_index:end_index].strip()
        print(filtered_dataset)
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
