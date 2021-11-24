import json, os

def reinsert(txt, json_txt):
    x = 0
    lines = []
    with open(txt, encoding = 'utf-8') as text:
        for line in text:
            lines.append(line)


    with open(json_txt, encoding = 'utf-8') as json_file:
        data = json.load(json_file)

    scnLength = (len(data['scenes']))

    for texts in range(scnLength):
        
        try:
                for i in range(len(data['scenes'][texts]['texts'])):
                    redo = lines[x]
                    data['scenes'][texts]['texts'][i][2] = redo[:-1]
                    x += 1
        except KeyError:
                pass
    
    with open(json_txt, 'r+',  encoding = 'utf-8') as json_file:
            json.dump(data, json_file, indent = 4, ensure_ascii= False)

insertion_method = input("Enter the number corresponding to the way you want to reinsert into the .json file. \n(1) Batch reinsert \n(2) Reinsert single file\n") # :picardy:

if (insertion_method == '1'):
    for text_json in os.listdir():
        if text_json.endswith('.m.json'):
                text = text_json + ".txt"
                try:
                    reinsert(text, text_json)
                except FileNotFoundError:
                    print("Could not find " + text)
elif (insertion_method == '2'):
    reinsert(input("Enter text file: "), input("Enter json file: "))
else:
    print("Invalid insertion method")

print("Finished!")