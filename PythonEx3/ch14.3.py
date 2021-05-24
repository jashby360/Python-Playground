import re
import os.path
import sys

d = dict()
filename = input("Enter a filename: ").strip()

# Check if file exists
if not os.path.isfile(filename):
    print("File", filename, "does not exist")
    sys.exit()

# Taken from my PLC course class CS
lines = open(filename, encoding='utf8', errors='ignore').read().lower()

# regular expression is quicker.
pattern = re.findall(r'\b[a-z]{3,15}\b', lines)

for word in pattern:
    count = d.get(word, 0)
    d[word] = count + 1

occurrence = d.keys()

for words in occurrence:
    print(words, d[words])
