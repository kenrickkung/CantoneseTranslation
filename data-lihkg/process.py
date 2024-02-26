import os
import regex as re

def get_length(line):
    return len(re.findall(r'[\p{Unified_Ideograph}\u3006\u3007]', line))


files = [f for f in os.listdir(os.getcwd() + "/txt/") if f.startswith("lihkg")]

_pattern_han = re.compile(r'[\p{Unified_Ideograph}\u3006\u3007]')

with open("mono_data.txt", "w") as wf:
    for fp in files:
        with open(f"./txt/{fp}","r") as rf:
            for line in rf.readlines():
                if _pattern_han.search(line) and get_length(line) > 10:
                    line = re.sub(r'http\S+', '', line, flags=re.IGNORECASE)
                    wf.write(line)


