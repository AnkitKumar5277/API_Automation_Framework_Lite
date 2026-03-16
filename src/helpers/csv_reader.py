import csv

def read_csv(file_path):
    data = []
    with open(file_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data