import os
import regex as re

files = [f for f in os.listdir(os.getcwd() + "/TXT/") if f.startswith("lihkg")]

_pattern_han = re.compile(r'[\p{Unified_Ideograph}\u3006\u3007]')

with open("mono_data.txt", "w") as wf:
    for fp in files:
        with open(f"./TXT/{fp}","r") as rf:
            for line in rf.readlines():
                if _pattern_han.search(line) and len(line) > 3:
                    wf.write(line)


