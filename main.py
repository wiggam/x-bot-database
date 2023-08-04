import os
import pandas as pd
import sqlite3
import random

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Global variable to store the dictionary mapping chronological order to random tweet IDs
tweet_order_dict = {}

def create_database(db_file_path):
    connection = sqlite3.connect(db_file_path)
    cursor = connection.cursor()

    # Create the 'tweets' table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tweets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            art_title TEXT,
            artist TEXT,
            year TEXT,
            search TEXT,
            description TEXT
        )
    ''')

    connection.commit()
    connection.close()

def add_csv_to_database(csv_file_path, db_file_path):
    # Read CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file_path)

    # Establish a connection to the SQLite database
    conn = sqlite3.connect(db_file_path)

    # Append the updated data to the existing database
    df.to_sql('tweets', conn, if_exists='append', index=False)

    # Close the connection to the database
    conn.close()

def description_counter(csv_file_path): 

    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file_path)

    # Add a new column 'description_char' containing the character count for each description
    df['description_char'] = df['description'].apply(lambda x: len(str(x)))

    # Filter rows with character count over 280
    filtered_df = df[df['description_char'] > 280]

    # Display the filtered DataFrame
    print(filtered_df)

def create_random_tweet_order_dict(num_entries):
    # Generate a list of unique random values from 1 to num_entries
    random_values = random.sample(range(1, num_entries + 1), num_entries)
    
    # Create the dictionary with keys in order from 1 to num_entries
    tweet_order_dict = {order: tweet_id for order, tweet_id in enumerate(random_values, start=1)}

    # Save the tweet order dictionary to a file
    with open("tweet_order_dict.txt", "w") as file:
        for k, v in tweet_order_dict.items():
            file.write(f"{k},{v}\n")

if __name__ == "__main__":
    # For initial import
    create_database('my_database.db')

    # add_csv_to_database("data.csv", "my_database.db")
    # description_counter('data.csv')
    # create_random_tweet_order_dict(806)
    

