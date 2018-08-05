'''
 Exercise 3:
 Given a paragraph of text, 
 1. count the number of times each character occurs in the text, 
   and print out each character and its count (in any order).
 2. do it now in a case-insensitive manner for the alphabets
 3. extension: print in the descending order of the count
'''


def count_char(text):
	i = 0
	count = 0
	d = dict()


	for i in range(len(text)):
		if text[i] in d and text[i] != ' ':
			d[text[i]] += 1
		elif text[i] != ' ':
			d[text[i]] = 1

	for i in d:
		print (i, d[i])


def count_char_insensitive(text):
	string = text.lower()
	i = 0
	count = 0
	d = dict()


	for i in range(len(text)):
		if string[i] in d and string[i] != ' ':
			d[string[i]] += 1
		elif string[i] != ' ':
			d[string[i]] = 1

	for i in d:
		print (i, d[i])

# bonus task:
def count_char_ordered(text):
    pass
    # add your code here 

text1 = "I felt happy because I saw the others were happy and because I knew I should feel happy but I wasn't really happy" 
text2 = 'HellO, WorLd!'

# testing exercise 2
count_char(text1)
count_char_insensitive(text1)
count_char_ordered(text2)

