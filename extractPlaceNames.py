#!/bin/python

import spacy
import csv
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

mySet = {''}

csvFile = open("gnr_part1.csv", "r+", encoding="ISO-8859-14")

reader = csv.reader(csvFile)
for item in reader:
    mySet.add(item[1])

text = open("ex.txt", "r").read()
nlp = spacy.load('en')
doc = nlp(text)

names = {''} 

for ent in doc.ents:
    if ent.label_ == 'GPE':
           names.add(ent.text)

for item in mySet:
    if process.extractBests(item, names, score_cutoff=91):
        print(str(item) + str(process.extract(item, names)))
