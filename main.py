
from flask import Flask, request, jsonify, render_template
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import base64
import json

app = Flask(__name__)

# Initialize Google Sheets API
scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(credentials)

# Index Page
@app.route('/')
def index():
    return render_template('index.html')

# Sidebar
@app.route('/sidebar')
def sidebar():
    return render_template('sidebar.html')

# Configuration Update
@app.route('/config', methods=['POST'])
def update_config():
    data = request.get_json()
    with open('config.json', 'w') as f:
        json.dump(data, f)
    return jsonify(result='success')

# Get Configuration
@app.route('/config', methods=['GET'])
def get_config():
    with open('config.json', 'r') as f:
        data = json.load(f)
    return jsonify(data)

# Create Events
@app.route('/events', methods=['POST'])
def create_events():
    config = get_config().json
    spreadsheet_id = config['spreadsheet_id']
    worksheet_name = config['worksheet_name']
    calendar_id = config['calendar_id']
    sheet = client.open_by_key(spreadsheet_id).worksheet(worksheet_name)
    records = sheet.get_all_records()
    for record in records:
        event = {
            'summary': record['Event Name'],
            'description': record['Description'],
            'start': {'dateTime': record['Start Date']},
            'end': {'dateTime': record['End Date']},
            'reminders': [{'method': 'email', 'minutes': 60}, {'method': 'popup', 'minutes': 10}]
        }
        result = client.create_event(calendar_id, event)
        print(f"Event created: {result.get('summary')}")
    return jsonify(result='success')

if __name__ == "__main__":
    app.run()
