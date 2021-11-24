import json, os

dir = os.path.join("parsed")
save_path = './parsed'

if not os.path.exists(dir):
    os.mkdir(dir)

def parse(filename):
    completeName = os.path.join(save_path, filename + ".txt")
    with open(filename, 'r', encoding = 'utf-8') as json_file:
        data = json.load(json_file)
    createFile = open(completeName, 'w', encoding = 'utf-8')      
    scnLength = (len(data['scenes']))
    for texts in range(scnLength):
        try:
            for i in range(len(data['scenes'][texts]['texts'])):
                scns = data['scenes'][texts]['texts'][i][2]
                createFile.write(scns + "\n")
        except KeyError:
            pass


for filename in os.listdir():
    if filename.endswith('.json'):
        parse(filename)
print("Finished!")


