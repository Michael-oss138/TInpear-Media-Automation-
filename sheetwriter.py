import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", scope)
client = gspread.authorize(creds)

sheet = client.open("Media Automation").sheet1

def writetosheet(row_data):
    all_links = sheet.col_values(8)
    if row_data.get("link") in all_links:
        print("⏭ Skipping duplicate:", row_data.get("title"))
        return

    sheet.append_row([
        row_data.get("title"),
        row_data.get("summary"),
        row_data.get("twitter"),
        row_data.get("linkedin"),
        row_data.get("instagram"),
        row_data.get("facebook"),
        row_data.get("hashtags"),
        row_data.get("link")
    ])