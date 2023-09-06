import os
import json
import logging

# Initialize logging
logging.basicConfig(filename='data_ingestion.log', level=logging.INFO)

# Define the directory path as a raw string to handle backslashes
directory_path = r"C:\Users\qaism\OneDrive - University of Virginia\Documents\GPT INFOBASE\QBOT_Jobs"
if not os.path.exists(directory_path):
    print(f"The directory path '{directory_path}' does not exist. Please check the path.")
    
# Function to ingest data from the directory
def ingest_data_from_directory(directory_path):
    ingested_data = {}
    logging.info(f"Starting data ingestion from directory: {directory_path}")

    for filename in os.listdir(directory_path):
        filepath = os.path.join(directory_path, filename)
        
        try:
            # Read JSON files
            if filename.endswith('.json'):
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = json.load(f)
                    logging.info(f"Successfully ingested JSON file: {filename}")
        
            # Read Text files
            elif filename.endswith('.txt'):
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    logging.info(f"Successfully ingested TXT file: {filename}")
        
            # Skip other file types
            else:
                logging.warning(f"Skipped file: {filename}. Unsupported file type.")
                continue
            
            ingested_data[filename] = content
        
        except Exception as e:
            logging.error(f"Failed to ingest file: {filename}. Error: {e}")

    logging.info("Data ingestion completed.")
    return ingested_data

# Function to update ingested data
def update_data(ingested_data):
    new_data = ingest_data_from_directory(directory_path)
    ingested_data.update(new_data)

# Function to parse ingested data
def parse_data(ingested_data):
    parsed_data = {}
    for filename, content in ingested_data.items():
        if filename.endswith('.json'):
            parsed_data[filename] = content
        elif filename.endswith('.txt'):
            parsed_data[filename] = content.split('\n\n')
    
    return parsed_data

# Main execution block
if __name__ == "__main__":
    try:
        ingested_data = ingest_data_from_directory(directory_path)
        logging.info("Data Ingestion completed. Log has been saved to data_ingestion.log.")

        parsed_data = parse_data(ingested_data)
        print("Parsed Data:", {k: parsed_data[k] for k in list(parsed_data)[:1]})
        
    except Exception as e:
        logging.error(f"An error occurred: {e}")
