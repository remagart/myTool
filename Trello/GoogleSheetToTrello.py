"""
Created on Sun Feb 16 01:35:00 2020

@description Read Google sheet data & write in Trello
@author Richard
"""
#%%
import os;
import json

# Load local key and data
root_dir = os.path.abspath(os.path.dirname(__file__));
key_dir = root_dir + "/../mykey/Trello_Key.json";

with open(key_dir,"r") as load_f:
    data = json.load(load_f);

info = data["OKR_EXCEL"]
header = info["HEADER"]

#%%
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Setting Google API info and call Google Sheet API
# Need to do "pip install --upgrade google-api-python-client oauth2client gspread" in env
# Need to set service account in Google API console
# Then share sheet to this service account.
# reference: https://missterhao.me/2019/01/05/python-google-sheet-crud2/ 
GServiceKey_dir = root_dir + "/../myKey/googleAPIKey.json";
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(GServiceKey_dir, scope)
client = gspread.authorize(creds)

spreadSheet = client.open(info["NAME"]);
sheet = spreadSheet.worksheet(info["SHEET1"])

for rows in sheet.get_all_records():
    print(f"{rows[header['COL_C']]}")
    print(f"{rows[header['COL_D']]}")
    break;

#%%