import csv

# open and read in csv file (unpack the content of the csv file into a variable)
with open('superbowl-01.csv', 'r') as csv_data:
    csv_data_in_dict = csv.DictReader(csv_data)
    
    # print(csv_data_in_dict)


    # This print operation must be inside the indent of the open function because
    # ... once the function finishes, it closes the file
    # So anything done outside the function in reference to anything inside the function
    # ... will be done to a closed file
    for row in csv_data_in_dict:
        print(row)