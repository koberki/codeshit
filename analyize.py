import csv
from datetime import datetime

def process_event(event_title, start_date, end_date, point_of_contact, met, good_things, bad_things, summary_of_event, unit):
    # Function to process each event
    print("Processing Event...")
    print(f"Title: {event_title}")
    print(f"Start Date: {start_date}")
    print(f"End Date: {end_date}")
    print(f"Point of Contact: {point_of_contact}")
    print(f"MET: {met}")
    print(f"Good Things: {good_things}")
    print(f"Bad Things: {bad_things}")
    print(f"Summary: {summary_of_event}")
    print(f"Unit: {unit}")
    print("Event Processed\n")





def load_events_in_date_range(file_path, start_date_str, end_date_str):
    # Convert the string dates to datetime objects
    start_date = datetime.strptime(start_date_str, "%m/%d/%Y")
    end_date = datetime.strptime(end_date_str, "%m/%d/%Y")

    with open(file_path, mode='r') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            event_start_date = datetime.strptime(row['START DATE'], "%m/%d/%Y")
            event_end_date = datetime.strptime(row['END DATE'], "%m/%d/%Y")

            # Check if the event falls within the provided date range
            if event_start_date >= start_date and event_end_date <= end_date:
                process_event(
                    row['EVENT TITLE'], 
                    row['START DATE'], 
                    row['END DATE'], 
                    row['POINT OF CONTACT'], 
                    row['MET'],
                    row['GOOD THINGS'], 
                    row['BAD THINGS'], 
                    row['SUMMARY OF EVENT'], 
                    row['UNIT']
                )

if __name__ == "__main__":
    file_path = input("Enter the name of the file: ")  # You can change this to the path of your CSV file
    user_start_date = input("Enter the start date (MM/DD/YYYY): ")
    user_end_date = input("Enter the end date (MM/DD/YYYY): ")

    load_events_in_date_range(file_path, user_start_date, user_end_date)