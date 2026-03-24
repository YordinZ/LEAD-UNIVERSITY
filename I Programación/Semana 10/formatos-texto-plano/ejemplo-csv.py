import csv

with open("data/datos.csv", newline="") as f:
    lector = csv.DictReader(f)
    

    for fila in lector:
        print(fila)


with open("output/ejemplo.csv", "a",newline="") as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
   
    