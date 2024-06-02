import csv
from openai import OpenAI

from datetime import datetime
with open('.openai_key', 'r') as keyfile:
    key = keyfile.read().replace('\n', '')
    print(key)
client = OpenAI(api_key=key, organization="org-nuYZ4gjIHjxzzvDGJC0J98SK")

def load_event(event_title, start_date, end_date, point_of_contact, met, good_things, bad_things, summary_of_event, unit):
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

    # combine the summary, good, and bad, things into one string
    full_summary = summary_of_event + " " + good_things + " " + bad_things

    # Replace newlines with spaces
    full_summary = full_summary.replace("\n", " ")

    return full_summary






def load_events_in_date_range(file_path, start_date_str, end_date_str):
    # Convert the string dates to datetime objects
    start_date = datetime.strptime(start_date_str, "%m/%d/%Y")
    end_date = datetime.strptime(end_date_str, "%m/%d/%Y")

    with open(file_path, mode='r') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        all_events = []
        for row in csv_reader:
            event_start_date = datetime.strptime(row['START DATE'], "%m/%d/%Y")
            event_end_date = datetime.strptime(row['END DATE'], "%m/%d/%Y")

            # Check if the event falls within the provided date range
            if event_start_date >= start_date and event_end_date <= end_date:
                event_summary = load_event(
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
                all_events.append(event_summary)
        
        print("Events Processed: ", str(len(all_events)))

        # Use OpenAI to summarize the events
        messages = [
            {"role": "system", "content": """
            You are the BI AI
            You have been given a list of events.
            Summarize the events.
            """
            },
        ]
        for event in all_events:
            messages.append({"role": "user", "content": "Event: " + event})
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages
        )
        print(response.choices[0].message.content)

if __name__ == "__main__":
    file_path = input("Enter the name of the file: ")  # You can change this to the path of your CSV file
    user_start_date = input("Enter the start date (MM/DD/YYYY): ")
    user_end_date = input("Enter the end date (MM/DD/YYYY): ")
    load_events_in_date_range(file_path, user_start_date, user_end_date)
    