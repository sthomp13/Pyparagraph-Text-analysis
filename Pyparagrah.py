# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 04:26:07 2018

@author: User
"""
file = ("paragraph_1.txt")
with open (file, 'r') as text:

    lines = text.read()
    
wordcount = 0
sentcount = 0

wordlist = []
sentlist = []

print("PyParagraph")

wordlist = lines.split(" ")
wordcount = str(len(wordlist))
print("Word Count: " + wordcount)

sentlist = lines.split(".")
sentcount = str(len(sentlist))
print("Sentence Count: " + sentcount)

