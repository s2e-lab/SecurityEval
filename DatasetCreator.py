import os
import json

dirPath = './Testcases_Prompt/'

dataset = []
for root, dirs, files in os.walk(dirPath):
    for file in files:
        if file.endswith('.py'):
            data = {}
            data['ID'] = root.split('/')[2]+'_'+file
            with open(os.path.join(root, file)) as f:
                data['Prompt']  = f.read().strip()
            with open(os.path.join('./Testcases_Insecure_Code/'+root.split('/')[2], file)) as f:
                data['Insecure_code']  = f.read().strip()
            print(data)
            dataset.append(data)

dataset = sorted(dataset, key=lambda x: x['ID'])
with open('dataset.jsonl', 'w') as f:
    for item in dataset:
        f.write(json.dumps(item)+'\n')
            

            