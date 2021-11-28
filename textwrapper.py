from os import linesep
import textwrap, os
dir = os.path.join("wrapper")
save_path = './wrapper'
if not os.path.exists(dir):
    os.mkdir(dir)

def wrap(filename):
    string = []
    textName = os.path.join(save_path, filename)
    with open(filename, encoding = 'utf-8') as file:
        for line in file:
            string.append(line)
    newText = open(textName, 'w', encoding = 'utf-8')
    for i in string:
        line = textwrap.wrap(i, width =50)
        textWrapper = ""
        for i in line:
            if i[-1] != ' ':
                textWrapper += str(i) + "\\n"
            else:
                textWrapper = str(i) + ' '
        textWrapper = textWrapper[:-2]
        newText.write(textWrapper + "\n")

for filename in os.listdir():
    if filename.endswith('.txt'):
        wrap(filename)
print("Finished!")