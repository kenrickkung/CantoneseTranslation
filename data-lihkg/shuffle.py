import random

with open('mono_data.txt', 'r') as file:
    lines = file.readlines()

# Step 2: Shuffle the lines
random.shuffle(lines)

# Step 3: Write the shuffled lines back to a new file (optional)
with open('shuffled_mono_data.txt', 'w') as file:
    file.writelines(lines)
