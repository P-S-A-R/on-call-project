import os
import requests
import json
from datetime import datetime

# --- Clear console ---
os.system('cls' if os.name == 'nt' else 'clear')

# --- Load mapping from JSON ---
with open("mapping.json") as f:
    ONCALL_MAPPING = json.load(f)

print("Loaded mapping:", ONCALL_MAPPING)

# Step 2: Define a simple rotation function
def get_oncall_from_calender():
   return "satya"

# Step 3: Send PUT request
def send_put_request(person):

    """
    Simulates reading the on-call person from Google Calendar.
    Rotates based on weekday for testing purposes.
    """
    people = list(ONCALL_MAPPING.keys())
    person = people[datetime.today().weekday() % len(people)]
    return person

   # --- Send PUT request function ---
def send_put_request(person):
    url = "https://httpbin.org/put"  # Replace with real Telekom API later
    payload = {
        "mobileNumber": ONCALL_MAPPING[person],
        "onCallPerson": person
    }

    response = requests.put(url, json=payload)

    print(f"Sending PUT for: {person} → {ONCALL_MAPPING[person]}")
    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())

    # Log each request
    with open("put_log.txt", "a") as log:
        log.write(f"{datetime.now()}: Sent PUT for {person} -> {ONCALL_MAPPING[person]}\n")
# --- Main execution ---
if __name__ == "__main__":
    person = get_oncall_from_calender()
    send_put_request(person)