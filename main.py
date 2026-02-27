import os
import requests
import json
from datetime import datetime
from calendar_service import get_oncall_from_google_calendar
import schedule
import time 

# --- Clear console ---
os.system('cls' if os.name == 'nt' else 'clear')

# --- Load mapping from JSON ---
with open("mapping.json") as f:
    ONCALL_MAPPING = json.load(f)

print("Loaded mapping:", ONCALL_MAPPING)

def send_put_request(person):
    url = "https://httpbin.org/put"

    payload = {
        "mobileNumber": ONCALL_MAPPING[person],
        "onCallPerson": person
    }

    response = requests.put(url, json=payload)

    print(f"Sending PUT for: {person} -> {ONCALL_MAPPING[person]}")
    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())
    # Log each request
    with open("put_log.txt", "a") as log:
        log.write(f"{datetime.now()}: Sent PUT for {person} -> {ONCALL_MAPPING[person]}\n")

# Job that runs repeatedly
def run_oncall_job():
    print("\nRunning On-Call Update Job...")

    person = get_oncall_from_google_calendar()

    if person not in ONCALL_MAPPING:
        print("On-call person not found in mapping!")
    else:
        send_put_request(person)

# Scheduler
if __name__ == "__main__":

    print("Scheduler started...")

    # For testing: run every 10 seconds
    schedule.every(10).seconds.do(run_oncall_job)

    while True:
        schedule.run_pending()
        time.sleep(1)