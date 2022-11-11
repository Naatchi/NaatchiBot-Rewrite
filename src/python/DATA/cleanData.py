from genericpath import isfile
from msilib.schema import Directory
import os
import json

import CONFIG.config as config

path = "C://Users//Josh//Repositories//NaatchiBot-Rewrite//src//python//DATA//JSON"
out = "C://Users//Josh//Repositories//NaatchiBot-Rewrite//src//python//DATA//OUT//out.txt"

write = open(out, "a", encoding="utf-8")

for filename in os.listdir(path):
    f = os.path.join(path, filename)
    if os.path.isfile(f):
        foo = open(f, "r", encoding="utf-8")
        data = json.load(foo)
        for i in data["conversations"]:
            for line in i:
                for item in line:
                    write.write(item + '\n')