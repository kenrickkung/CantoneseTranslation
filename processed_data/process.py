from random import shuffle, seed
import os

zh_test_length = 10

folder_name = ["../data-wenlin","train","train-short"]
file_name = ["/yue.txt","/en.txt"]

yue = []
en = []

for folder in folder_name:
    with open(folder+file_name[0],'r') as f_yue, open(folder+file_name[1],'r') as f_en:
       yue.extend(f_yue.read().splitlines())
       en.extend(f_en.read().splitlines())
    
seed(42)
data = list(zip(yue, en))
shuffle(data)

yue, en = zip(*data)

short = []
long = []

for i,y in enumerate(yue):
    if len(y) < zh_test_length:
        short.append((y,en[i]))
    else:
        long.append((y,en[i]))


def write_to_file(l: [(str,str)], folder: str) -> None:
    with open(folder+"/yue.txt", 'w', encoding='utf-8') as f_yue, open(folder+"/en.txt", 'w', encoding='utf-8') as f_en:
        for yue, en in l:
            print(yue, file=f_yue)
            print(en, file=f_en)


language = ["/yue.txt","/en.txt"]

folder = "new-train-short"

if not os.path.exists(folder):
    os.makedirs(folder)
write_to_file(short, folder)

folder = "new-train"

if not os.path.exists(folder):
    os.makedirs(folder)
write_to_file(long, folder) 
