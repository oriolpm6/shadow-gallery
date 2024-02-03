# main.py
import os
from web_scraping import extract_match_information
from calendar_events import authenticate_google_calendar, create_calendar_event
from datetime import datetime, timedelta

# URL for futboltv.info
url = "https://futboltv.info"

# Extract match information
match_data = extract_match_information(url)

# Teams you are interested in
chosen_teams = ["Barcelona", "Real Madrid", "Liverpool", "Chelsea", "Arsenal", "Manchester City"]

# Filter matches for chosen teams
chosen_matches = [match for match in match_data if match['home_team'] in chosen_teams or match['away_team'] in chosen_teams]

# Get the current working directory
current_directory = os.getcwd()

# Path to your downloaded JSON file in the "Credentials" folder
credentials_path = os.path.join(current_directory, "Credentials", "futboltv-calendar-credential.json")

# Authenticate with Google Calendar
service = authenticate_google_calendar(credentials_path)

# Create events on Google Calendar for chosen teams
for match in match_data:
    home_team = match['home_team']
    away_team = match['away_team']

    if home_team in chosen_teams or away_team in chosen_teams:
        # Adjust the format to match the 'start_date' in your data
        start_time = datetime.strptime(match['start_date'], "%Y-%m-%dT%H:%M:%S")

        # Calculate the end_time as 2 hours after the start_time
        end_time = start_time + timedelta(hours=2)

        summary = f"{home_team} vs {away_team}"
        description = f"TV Channels: {', '.join(match['channels'])}"

        create_calendar_event(service, summary, start_time, end_time, description)
