"""#TASK 3 — Save to a JSON File"""

import pandas as pd
import os

def main():
    file_path = "data/cleaned_trends.csv"

    if not os.path.exists(file_path):
        print("CSV not found. Please run Task 2.")
        return

    # Loading the data into a DataFrame
    df = pd.read_csv(file_path)

    # 1. Grouping by category to see which topic is most popular
    print("--- Average Score Per Category ---")
    avg_scores = df.groupby('category')['score'].mean()
    print(avg_scores)
    print("\n")

    # 2. Finding the most discussed story
    # idxmax() gives us the index of the highest value
    top_story_idx = df['num_comments'].idxmax()
    top_story = df.loc[top_story_idx]

    print(f"--- Most Commented Story ---")
    print(f"Title: {top_story['title']}")
    print(f"Comments: {top_story['num_comments']}\n")

    # 3. Filtering for Viral Stories
    # I'm using & for the 'and' condition in Pandas
    viral_df = df[(df['score'] > 50) & (df['num_comments'] > 10)]
    print(f"--- Viral Stories Count: {len(viral_df)} ---")
    print(viral_df[['title', 'score', 'num_comments']].head())

if __name__ == "__main__":
    main()
