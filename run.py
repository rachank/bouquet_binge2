import gspread
from google.oauth2.service_account import Credentials
import json

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

creds = json.load(open('creds.json'))
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('bouquet_binge2')

def obtain_sales_info():
    """
    This function asks the user to enter 7 numbers, sparated by commas 
    of bouquet sales for the previous week. 
    It continues to ask until the numbers are valid, if there is an error in the values 
    it will return an error message, if no errors exist it returns a list
    of 7 integers.
    """
   
    while True:
        print("Please enter bouquet sales data from the last week of sales.")
        print("Data order: Roses, Orchids, Lilies, Carnations, Hydrangeas, Mums, and Seasonal.")
        print("Example: 20,30,20,10,20,30,25\n")
        user_str = input("Enter The Weekly Data Here:\n")
        sales_info = user_str.split(",")
         if len(sales_info) != 7:
            print("Error. Please enter exactly 7 numbers seperated by commas.")
            print(f"You entered {len(sales_info)} values.")
            continue
        all_values = True
        for value in sales_info:
            try:
                int(value)
            except ValueError:
                all_values = False
                print(f"Error: '{value}' is not a valid integer.")
        sales_info = [int(value) for value in sales_info]

    print("Sales data:", sales_info)

    return sales_info        

def update_sales_worksheet(info):
    """
    Updates sales worksheet by adding new row according to the list data given.
    """
    print("Updating Sales Worksheet....\n")
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(info)
    print("Sales Worksheet has Updated Successfully!\n")

