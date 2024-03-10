import requests
import json
import csv

def convertdata(json_response):
    # Parse the JSON response
    data = json.loads(json_response)

    # Extract the list of agents
    agents = data['data']['agents']['searchAgents']

    # Specify the CSV file name
    csv_file = '18.csv'

    # Write data to CSV file
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Write header
        writer.writerow(['ID', 'First Name', 'Last Name', 'Full Name', 'Photo', 'City', 'State', 'Languages', 'Email', 'License', 'Mobile Phone', 'Is Luxury Agent', 'Market Center'])

        # Write data for each agent
        for agent in agents:
            writer.writerow([
                agent['id'],
                agent['firstName'],
                agent['lastName'],
                agent['fullName'],
                agent['photo'],
                agent['city'],
                agent['state'],
                ', '.join(agent['languages']),
                agent['email'],
                agent['license'],
                agent['mobilePhone'],
                agent['isLuxuryAgent'],
                agent['marketCenter']['name']
            ])

    print(f"Data has been written to {csv_file}.")

def main():
    url = 'https://graph.cons-prod-us-central1.kw.com'
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'https://www.kw.com/',
        'Content-Type': 'application/json',
        'Authorization': '',  # Add your authorization token here
        'Origin': 'https://www.kw.com',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'Te': 'trailers'
    }

    payload = {
        "operationName": "SearchForAgents",
        "variables": {
            "filters": {},
            "first": 1075,
            "after": 170000
        },
        "query": "query SearchForAgents($filters: AgentSearchFilters, $first: Float, $after: Float) {\n agents(filters: $filters, first: $first, after: $after) {\n totalCount\n searchAgents {\n id\n firstName\n lastName\n fullName\n photo\n city\n state\n languages\n email\n license\n mobilePhone\n isLuxuryAgent\n marketCenter {\n name\n __typename\n }\n __typename\n }\n __typename\n }\n}"
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            convertdata(response.text)
            print("Response saved to agents.csv")
        else:
            print("Failed to receive response. Status code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
