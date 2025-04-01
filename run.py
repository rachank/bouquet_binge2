import gspread
from google.oauth2.service_account import Credentials
import json

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('bouquet_binge2')

def obtain_sales_info():
    """
    This function asks the user to enter 7 numbers, sparated by commas, 
    of the bouquet sales for the previous week. 
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
                print(f"Error: '{value}' is not a valid integer. Please re-enter valid numbers.")
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

def update_excess_worksheet(info):
    """
    Update excess worksheet by adding new row according to the list 
    information given.
    """
    print("Updating Excess Worksheet...\n")
    excess_worksheet = SHEET.worksheet("excess")
    excess_worksheet.append_row(info)
    print("Excess Worksheet Updated successfully!\n")

def calc_excess_info(sales_row):
    """
    This compares the sales with the inventory and then calculates the excess or short amount for each bouquet type.
    The excess is evaluated as the number of sales subtracted from the inventory.
    * A Negative excess points to the requirement of additional inventory made that week.
    * A Positive excess results in the number of bouquets that were thrown away.
    """
    print("Determining Excess data...\n")
    inventory = SHEET.worksheet("inventory").get_all_values()
    inventory_row = inventory[-1]
    excess_info = []
    for i in range(len(inventory_row)):
    # Note: try/except is not necessary because inventory is already a validated 
    # integer from above.
        inventory_value = int(inventory_row[i])  
        sales_value = sales_row[i]
        excess = inventory_value - sales_value
        excess_info.append(excess)
    return excess_info

def get_latest_sales_info():
    """
    This retreives the lastest of 5 weeks of Bouquet sales from the spreadsheet.
    Returned as a list of lists.
    """
    sales_sheet = SHEET.worksheet("sales")
    last_5_entries = []
    for col_index in range(1,8):
        column_info = sales_sheet.col_values(col_index)
        last_5 = column_info[2:]
        last_5_entries.append(last_5)
    return last_5_entries

def calc_inventory_info(info):
    """
    This calculates the average inventory for each item type, 
    adding 15% for additional available inventory.
    """
    print("calculating Inventory Information...\n")
    new_inventory_info = []
    for column in info:
        int_column = [int(num) for num in column]
        average = sum(int_column) / len(int_column)
        inventory_num = average * 1.15
        new_inventory_info.append(round(inventory_num))
    return new_inventory_info

def obtain_inventory_info(info):
    """
    This retrieves the names of the headings for the different types of bouquets 
    and returns the calculated inventory number for the corresponding bouquet.
    """
    bouquet_options = SHEET.worksheet("inventory").get_all_values()[0]
    print("\U0001F33C Please prepare the following number of flower bouquets for next week's inventory:\n")
    inventory_options = {}
    for bouquet_option, inventory in zip(bouquet_options, info):
        inventory_options[bouquet_option] = inventory
    return inventory_options

def main():
    """
    This calls all other functions in the program.
    """
    sales_info = obtain_sales_info()
    update_sales_worksheet(sales_info)
    excess_info = calc_excess_info(sales_info)
    update_excess_worksheet(excess_info)
    latest_sales_info = get_latest_sales_info()
    inventory_info = calc_inventory_info(latest_sales_info)
    inventory_need_next_week = obtain_inventory_info(inventory_info)
    print(inventory_need_next_week)

main()

print("\U0001F33C Welcome to the Bouquet Binge Flower Shop Inventory Information. \U0001F33C")