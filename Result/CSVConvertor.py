import json
import csv
header = ['CWEID', 'SampleID', 'Modified','CodeQL', 'Bandit','Manual']
rows =[]
with open('./testcases.json', 'r') as f:
    data = json.load(f)
    for content in data[0]['contents']:

        if content['type']=='directory':
            print(content['name'])
            files = content['contents']
            for file in files:
                row = []
                row.append(content['name'])
                row.append(file['name'])
                row.append(0)
                row.append(0)
                row.append(0)
                row.append(0)
                rows.append(row)
                print(file)

with open('testcases_bad.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(rows)