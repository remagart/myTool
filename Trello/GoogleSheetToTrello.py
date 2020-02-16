"""
Created on Sun Feb 16 01:35:00 2020

@description Read Google sheet data & write in Trello
@author Richard
"""
#%%

import os;
import json

root_dir = os.path.abspath("..");
key_dir = root_dir + "/mykey/Trello_Key.json";

with open(key_dir,"r") as load_f:
    data = json.load(load_f);
    
excel_id = data["OKR_EXCEL_ID"];
sheet_id = data["OKR_SHEET_ID"];

#%%
