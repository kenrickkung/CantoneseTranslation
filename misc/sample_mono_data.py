import random

with open("news.2012.en.shuffled", "r", encoding='utf-8') as f:
  mono_data = f.readlines()

print(f"Read {len(mono_data)} Lines from 2012 News")

random.seed(42)

mono_data_sampled = random.sample(mono_data, 500_000)

with open("mono_data_en.txt", "w") as f:
  for line in mono_data_sampled:
    length = len(line.split(" "))
    if length > 7:
      f.write(line)