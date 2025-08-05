import csv

# Module function to calculate the total payable amount
def calculate_total_payable(principle, annual_interest, years):
    # Calculates the total amount payable
    return principle * pow(1 + annual_interest / 100, years)

# Module function to write name and total payable amount to a file
def writeToFile(name, total_payable):

    # Open the output file in append mode, so that file isn't overwritten everytime we output data
    with open('output.csv', mode='a', newline='') as file:
        data_writer = csv.writer(file)
        data_writer.writerow([name, total_payable])  # Write persons name and total payable amount to the file     

# Clear the output file before writing new data     
def clear_file(filename):
    # Opens the named file
    with open(filename, mode='w', newline='') as file: # Set to write mode to clear the file contents
        pass  # Just open and close the file to clear its contents
