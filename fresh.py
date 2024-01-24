from unicodedata import category
from urllib import response
import requests
import json
from bs4 import BeautifulSoup
import time
import os
from categorize import categorize

# BASE_URL = "https://nimblegroupservicedesk.freshservice.com/api/v2"
BASE_URL = "https://tateinc.freshdesk.com/api/v2"
API_KEY = os.environ["TATEINC_API_KEY"]
PASSWORD = "123"
URL = BASE_URL + "/tickets"


#  LAST_TICKET_FILE = "last_ticket_id.txt"


def fetch_all_tickets():
    # last_ticket_id = load_last_ticket_id(default=2)
    # filter_params = "created_at:2024-01-06T01:00:07Z"
    # query_params = {"include": "department"}

    response = requests.get(URL, auth=(API_KEY, PASSWORD))

    if response.status_code == 200:
        tickets = json.loads(response.content)
        for ticket in tickets["tickets"]:
            subject = ticket["subject"]
            body = ticket["description_text"]

            print(ticket["id"])
            print(subject)
            # print(body)
            print("")
    else:
        print(f"Failed to fetch tickets. Status code: {response.status_code}")


def fetch_unprocessed_tickets():
    # url_query = 'query="priority:2"'
    url_query = 'query="cf_auto_classified:false"'
    params = {"include": "description"}
    FILTER_URL = BASE_URL + "/search/tickets?" + url_query

    response = requests.get(FILTER_URL, auth=(API_KEY, PASSWORD))

    if response.status_code == 200:
        response_data = json.loads(response.content)
        tickets = response_data["results"]
        print("filtered tickets")
        for ticket in tickets:
            subject = ticket["subject"]
            body = ticket["description_text"]
            ticket_id = ticket["id"]
            custom_fields = ticket["custom_fields"]
            auto_classified = custom_fields["cf_auto_classified"]

            print(ticket_id)
            print("Auto Classified = ", auto_classified)
            print(subject)
            # print(body)
            print("")

        return tickets


def update_ticket(ticket_id, category):
    # label ticket as auto_classified
    update_fields = {
        "custom_fields": {
            "cf_auto_classified": True,
            "cf_department": "CC - Payment/Settlement Arrangement",
        }
    }

    headers = {
        "Content-Type": "application/json",
    }
    UPDATE_URL = BASE_URL + f"/tickets/{ticket_id}"

    response = requests.put(
        UPDATE_URL, auth=(API_KEY, PASSWORD), json=update_fields, headers=headers
    )

    if response.status_code == 200:
        print(f"ticket {ticket_id} successfully updated")
    else:
        print(f"Update failed. Status Code: {response.status_code}")


def reply_to_ticket(id, body):
    reply_url = URL + f"/{str(id)}/reply"
    data = {"body": body}
    headers = {"Content-Type": "application/json"}
    response = requests.post(
        reply_url, auth=(API_KEY, PASSWORD), headers=headers, json=data
    )

    print(response.status_code)
    print(response.text)


# fetch_all_tickets()
tickets = fetch_unprocessed_tickets()


if tickets is not None:
    for ticket in tickets:
        category = categorize(ticket["description_text"])
        if category == 1:
            update_ticket(ticket["id"], "CC - Payment/Settlement Arrangement")
        elif category == 0:
            print("Not a payment/settlement agreement")
else:
    print("No unprocessed tickets found.")

# reply_to_ticket(28, "HEllo this is a reply")
