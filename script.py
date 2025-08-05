import csv # Importing csv module to read csv files
import functions # Importing the writeToFile function to output data to file

functions.clear_file('output.csv')  # Clear the output file before writing new data

with open('input.csv', mode='r') as file: # Open the csv file in read mode
    data_reader = csv.reader(file)
    for row in data_reader: # Reads contents of file row-by-row
        name = str(row[0])  # First column contains the name
        principle = int(row[1])  # Second column is the loan principal (amount borrowed)
        annual_interest = float(row[2])  # Third column is the annual interest rate
        years = int(row[3])  # Fourth column is the number of years to pay back loan
        
        # Uses the function from the imported functions module
        total_payable = int(functions.calculate_total_payable(principle, annual_interest, years))  # Calculate total amount payable
        
        # Calculate monthly payment by dividing total payable by the total number of months
        monthly_payment = total_payable / (years * 12)
        
        # Write the name and total payable amount to the output file
        functions.writeToFile(name, total_payable) 