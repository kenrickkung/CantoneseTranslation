from random import shuffle
import os

zh_test_length = 10
dev_data_count = 3000
test_data_count = 3000

folder_name = ["../data-wenlin","../data-words.hk"]
file_name = ["/yue.txt","/en.txt"]

for folder in folder_name:
    with open(folder+file_name[0],'r') as f_yue, open(folder+file_name[1],'r') as f_en:
       yue = f_yue.read().splitlines()
       en = f_en.read().splitlines()

short = []
long = []

for i,y in enumerate(yue):
    if len(y) < zh_test_length:
        short.append((y,en[i]))
    else:
        long.append((y,en[i]))

shuffle(long)

# Split Data to Train, Dev and Test Set
dev_data = long[:dev_data_count+1]
test_data = long[dev_data_count+1:dev_data_count+test_data_count+1]
train_data= long[dev_data_count+test_data_count+1:]




def write_to_file(l: [(str,str)], folder: str) -> None:
    with open(folder+"/yue.txt", 'w', encoding='utf-8') as f_yue, open(folder+"/en.txt", 'w', encoding='utf-8') as f_en:
        for yue, en in l:
            print(yue, file=f_yue)
            print(en, file=f_en)

split = ["train","dev","test"]
language = ["/yue.txt","/en.txt"]
data = [train_data, dev_data, test_data]

folder = "train-short"

if not os.path.exists(folder):
    os.makedirs(folder)
write_to_file(short, folder)
 
for i,t in enumerate(split):
    if not os.path.exists(t):
        os.makedirs(t)
    write_to_file(data[i],t)





