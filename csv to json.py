import csv
import json
import logging

 #Setup logging
 logging.basicConfig(level=logging.INFO)

 def convert_csv_to_json(csv_file, json_file):
    try: 	
         #Read CSV file
         with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
             csv_reader = csv.DictReader(file)
             data = list(csv_reader)

         logging.info("CSV file read successfully.")

          #Write JSON file
         with open(json_file, mode='w', encoding='utf-8') as file:
             json.dump(data, file, indent=4)

         logging.info("JSON file created successfully.")

     except FileNotFoundError:
         logging.error("The CSV file was not found.")
     except Exception as e:
         logging.error(f"An error occurred: {e}")

  #Example usage
 convert_csv_to_json("data.csv", "data.json")
