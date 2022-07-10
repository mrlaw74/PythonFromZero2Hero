import csv
with open('csv_demo.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} lam viec trong {row[1]}, va duoc sinh ra thang {row[2]}')
            line_count += 1
    print(f'Processed {line_count} lines.')