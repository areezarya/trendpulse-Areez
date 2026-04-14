"""#Task 2 — Extract the Fields"""

import json
import csv
import re
import os

def clean_text(text):
    # This regex keeps only letters, numbers, and spaces
    # It helps remove emojis or weird symbols often found in HN titles
    return re.sub(r'[^a-zA-Z0-9\s]', '', text)

def main():
    # We need to find the JSON file created in Task 1
    # For simplicity, I'm looking for any JSON in the data folder
    data_folder = "data"
    json_files = [f for f in os.listdir(data_folder) if f.endswith('.json')]

    if not json_files:
        print("No JSON file found! Did you run Task 1 first?")
        return

    input_file = os.path.join(data_folder, json_files[0])
    output_file = os.path.join(data_folder, "cleaned_trends.csv")

    try:
        with open(input_file, 'r') as f:
            stories = json.load(f)

        # Preparing the CSV headers
        headers = ["post_id", "title", "category", "score", "num_comments", "author", "collected_at"]

        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()

            for story in stories:
                # Cleaning the title before saving
                story['title'] = clean_text(story['title'])
                writer.writerow(story)

        print(f"Success! Cleaned {len(stories)} stories and saved to {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
