import os
import pandas as pd
import numpy as np
import csv 

def listToString(s):
    str1 = ""
    i = 1
    for element in s:
        str1+=element
        i += 1
        total = 1497770
        percent = i / total
        print(percent)
    return str1

filepath = "C:\\Users\\Josh\\Repositories\\NaatchiBot-Rewrite\\src\\python\\DATA\\OUT\\out.txt"
csvpath = "C:\\Users\\Josh\\Repositories\\NaatchiBot-Rewrite\\src\\python\\DATA\\OUT\\data.csv"

lines = [line.rstrip('\n').replace('\\n', ' ') for line in open(filepath, 'r', encoding="utf-8")]

subtitles = pd.DataFrame(columns=['context', 'reply'])
subtitles['context'] = lines
subtitles['context'] = subtitles['context'].apply(lambda x: x.lower())
subtitles['reply'] = lines[1:] + ['...']
subtitles['reply'] = subtitles['reply'].apply(lambda x: x.lower())

subtitles.info()

subtitles.to_csv(csvpath, index=False)