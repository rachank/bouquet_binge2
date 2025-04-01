# Bouquet Binge Flower Shop

This is a project which was very much inspired by the Love Sandwiches project. It is designed to function in command line based Python to calculate the weekly sales inputs from a non-existent flower shop called Bouquet Binge. Upon the start of the program, the user is prompted to input 7 values for the latest variety of bouquet sales data from the flower shop. The program then calculates any excesses or shortages in inventory and produces recommendations for the number of bouquet inventory required for the following week based on a recommended 15% inventory surplus as a buffer for projected sales.

This program utilizes google sheets to store the inventory, sales and excess data information for the Bouquet Binge Flower Shop.


[View the live project here.] (ADD URL)

## Features

-   Once the program is run the user is prompted to input 7 numbers representing sales values for the 7 different types of bouquets that are sold: Roses, Orchids, Lilies, Carnations, Hydrangeas, Mums, and Seasonal.

![IMAGE DESCRIPTION](RELATIVE PATH)

- The program then checks the user input for any invalid inputs, such as non integer inputs or missing numbers and will give error messages to the user and request the user to input the 7 numbers again.

![IMAGE DESCRIPTION](RELATIVE PATH)


- This program uses the gspread API to interact with Google Sheets where the data is stored in all of the respective worksheets “inventory”, “excess” and “sales” for the data given, calculated and updated for all of the different types of flower bouquets sold.

![IMAGE DESCRIPTION](RELATIVE PATH)
PUT IN IMAGES OF ALL 3 ORIGINAL GOOGLE WORKSHEETS FROM THE START


- Once the input is valid, the program will update the sales information given in the Google Sheets “sales” worksheet.

![IMAGE DESCRIPTION](RELATIVE PATH)
PUT IN IMAGE OF GOOGLE SHEETS “SALES”

- It will also calculate the excess or shortage of each type of bouquet based on the sales numbers given and the current listed inventory in the “inventory” worksheet.

- The “excess” worksheet will then also be updated with either an excess, results of a positive number, or a shortage, results of a negative number, for each type of bouquet.

![IMAGE DESCRIPTION](RELATIVE PATH)
PUT IN IMAGE OF GOOGLE SHEETS EXCESS


- The “inventory” worksheet will also be updated in Google Sheets.

PUT IN IMAGE OF GOOGLE SHEETS INVENTORY
![IMAGE DESCRIPTION](RELATIVE PATH)


- The program then calculates the average weekly sales over 5 weeks and recommends the required inventory, adding on an additional 15% inventory surplus to allow for additional quick, last minute sales.


## Possible Future Features

- Include actual sales numbers for each type of bouquet to then also calculate profits and losses

- Include options for items to be sold at a discount of a certain percentage to mitigate losses the last two days of the week.

- Add a feature to generate weekly or monthly sales reports to track sales trends over time to show which bouquet types are in high demand and during which periods of time.


## Testing

- Some issues found when run through PEP8 linter, mostly missing or too many spaces and a few lines that contained too many characters. All was corrected.


![PEP8 CI Python Linter](images/pep8_ci_python_linter.png)











## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.
