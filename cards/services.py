import os
import gspread
from typing import List
from django.conf import settings
from dotenv import load_dotenv

load_dotenv()

def initialize_gspread() -> gspread.client.Client:
  return gspread.service_account_from_dict(get_credentials())

def get_credentials() -> dict:
  return {
    "type": os.getenv("TYPE"),
    "project_id": os.getenv("PROJECT_ID"),
    "private_key_id": os.getenv("PRIVATE_KEY_ID"),
    "private_key": os.getenv("PRIVATE_KEY"),
    "client_email": os.getenv("CLIENT_EMAIL"),
    "client_id": os.getenv("CLIENT_ID"),
    "auth_uri": os.getenv("AUTH_URI"),
    "token_uri": os.getenv("TOKEN_URI"),
    "auth_provider_x509_cert_url": os.getenv("AUTH_PROVIDER_X509_CERT_URL"),
    "client_x509_cert_url": os.getenv("CLIENT_X509_CERT_URL"),
    "universe_domain": os.getenv("UNIVERSE_DOMAIN")
  }

def get_all_cards(doc_name: str, sheet_name: str = None) -> List[dict]:
  sh = settings.GSPREAD_CLIENT.open(doc_name)
  worksheet = sh.worksheet[sheet_name] if sheet_name else sh.get_worksheet(0)
  return worksheet.get_all_records()

def get_card(doc_name: str, row_id: int, sheet_name: str = None):
    sh = settings.GSPREAD_CLIENT.open(doc_name)
    worksheet = sh.worksheet[sheet_name] if sheet_name else sh.get_worksheet(0)
    records = worksheet.get_all_records()
    return next((row for row in records if row["ID"] == row_id), None)

def add_card(doc_name: str, sheet_name: str = None, card_data: dict = None):
  sh = settings.GSPREAD_CLIENT.open(doc_name)
  worksheet = sh.worksheet(sheet_name) if sheet_name else sh.get_worksheet(0)
    
  if card_data is not None:
    worksheet.append_row(list(card_data.values()))
    return True
    
def delete_card(doc_name: str,  row_id: int, sheet_name: str = None):
  sh = settings.GSPREAD_CLIENT.open(doc_name)
  worksheet = sh.worksheet(sheet_name) if sheet_name else sh.get_worksheet(0)
  try:
    all_data = worksheet.get_all_values()
    header, data = all_data[0], all_data[1:]
    new_data = [row for row in data if str(row[0]) != str(row_id)]  
    worksheet.clear()
    worksheet.append_row(header)
    for row in new_data:
        worksheet.append_row(row)
    return True
  except Exception as e:
    print(f"Error: {e}")
    return False

def update_card(doc_name: str, row_id:int, new_data: list, sheet_name: str = None):
  sh = settings.GSPREAD_CLIENT.open(doc_name)
  worksheet = sh.worksheet(sheet_name) if sheet_name else sh.get_worksheet(0)
  try:
      all_data = worksheet.get_all_values()
      for index, row in enumerate(all_data):
          if str(row[0]) == str(row_id):  
              worksheet.update(f'A{index+1}:F{index+1}', [new_data])
              return True
      
      return False
  except:
      return False