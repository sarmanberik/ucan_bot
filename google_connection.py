from __future__ import print_function
from google.oauth2 import service_account
from googleapiclient.discovery import build
from pprint import pprint
from datetime import datetime, timedelta


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1MAcWgT2vtA7OI3pshIXzhNcJf78ycwcUbRB7xWI5-jY'

# 1299724951
SERVICE_ACCOUNT_FILE = 'credentials.json'
SAMPLE_RANGE_NAME = 'Ответы на форму (1)'


def get_value(name):
    res = []
    today = (datetime.today() - timedelta(days=1)).strftime('%d.%m.%Y')
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    service = build('sheets', 'v4', credentials=credentials).spreadsheets().values()

    result = service.get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME).execute()

    data_from_sheet = result.get('values', [])
    for each in data_from_sheet:
        if today in each[0] and name in each[2]:
            res.append(each)
    return res
    # pprint(data_from_sheet)


# get_value('Райымбек Талшын 6КОУ')

# student = []
# for each in data_from_sheet:
#     if each[2] not in student:
#         student.append(each[2])
#
# print(student)
# print(len(student))
