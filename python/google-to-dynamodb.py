import boto3
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Set up Google Sheets API credentials
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('path/to/credentials.json', scope)
client = gspread.authorize(creds)

# Open the Google Sheet
sheet = client.open('Your Sheet Name').sheet1

# Get all the data from the sheet
data = sheet.get_all_records()

# Set up DynamoDB client
dynamodb = boto3.resource('dynamodb', region_name='your-region')
table = dynamodb.Table('your-table-name')

# Migrate data to DynamoDB
with table.batch_writer() as batch:
    for row in data:
        batch.put_item(Item=row)

print("Data migration from Google Sheet to DynamoDB completed.")