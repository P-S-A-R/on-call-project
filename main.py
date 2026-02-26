import requests
from mapping import ONCALL_MAPPING
from datetime import datetime



# Step 2: Define a simple rotation function
def get_oncall_from_calender():
   return "satya"

# Step 3: Send PUT request
def send_put_request(person):
    url = "https://httpbin.org/put"  # Replace with Telekom API later
    payload = {
        "mobileNumber": ONCALL_MAPPING[person],
        "onCallPerson": person
    }
    response = requests.put(url, json=payload)
    print( "sending PUT for :", person)
    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())

# Step 4: Main execution
if __name__ == "__main__":
    person = get_oncall_from_calender()
    send_put_request(person)