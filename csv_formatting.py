import csv

input_csv_path = "data/Nimble real data/pwd_req_real_data.csv"
output_csv_path = "data/Nimble real data/pwd_req_real_data_formated.csv"
delimiter = ";"
search_string = "info@nimblegroup.co.za> "

with open(input_csv_path, "r", newline="", encoding="latin-1") as input_file, open(
    output_csv_path, "w", newline="", encoding="utf-8"
) as output_file:
    csv_reader = csv.reader(input_file, delimiter=delimiter)
    csv_writer = csv.writer(output_file, delimiter=delimiter)

    for row in csv_reader:
        # Assuming the email field is in the first column (index 0)
        if row and len(row) > 0:
            email = row[0]
            index = email.find(search_string)
            if index != -1:
                # Remove text after the specified string
                row[0] = email[: index - len(search_string)]
            csv_writer.writerow(row)

print(
    f"Modified CSV file with text removed after '{search_string}' has been created at {output_csv_path}."
)
