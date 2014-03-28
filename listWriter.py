#!/usr/bin/python

import itertools

minLen = int(raw_input('Enter the minimum word length: '));
maxLen = int(raw_input('Enter the maximum word length: '));
simpList = raw_input("Generate simple wordlist? (y/n): ");
if simpList == 'y':
	charSet = 'abcdefghijklmnopqrstuvwxyz';
elif simpList == 'n':
	charSet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-=_+';
listName = raw_input('Name for the wordlist file to be created: ');

for l in range(minLen,maxLen):
	word = itertools.combinations(charSet, l)

	for i in word:
		file = open(listName, 'a');
		file.write(''.join(i)+'\n');
		file.close();
