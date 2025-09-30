import csv
p = {}

with open("products.csv", encoding = 'utf-8') as f:
    csv_data = csv.reader(f)

    results = []
    total = 0
    for this_line in csv_data:
        name = this_line[0]
        price = float(this_line[1])
        quantity = float(this_line[2])
        total = price * quantity
        results.append([name, price, quantity, total])

with open("products1.csv", "w", newline = "", encoding = "utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "price", "quantity", "total"])
    writer.writerows(results)


    