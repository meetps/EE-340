####################################################
# Authors: Meet Shah, Yash Bhalgat, Navjot Singh 
# File :   morse-decoder
# Desc :   Take input from an audio file, generate
# 		   a string of 1's, 0's. Decode the message 
#		   using standard run-length encoding method 
#		   and comparing with data gathered from 
#		   supervised learning.
####################################################


def getMorseFromAudio(filename):
	'''Top function:
	Returns morse-decoded string from audio'''
	with open(filename) as f:
	    content = str(f.readlines())
	
	morse_data = []
	morse_data_binary = []

	splittedContent = content.split("\\x")

	for data in splittedContent:
		if(data == "80?"):
			morse_data.append("x")
		elif(data == "00"):
			morse_data.append("y")

	i=0
	while(i < len(morse_data)):
		# print(morse_data[i:i+3])
		if(morse_data[i:i+3] == ['y','y','x']):
			morse_data_binary.append("1")
			i = i+3
		else:
			morse_data_binary.append("0")
			i = i+1

	binary_sequence =''

	for word in morse_data_binary:
		binary_sequence = binary_sequence + word;

	# print(binary_sequence)

	def encode(input_string):
	'''Run-length encode the input file'''
	    count = 1
	    prev = ''
	    lst = []
	    for character in input_string:
	        if character != prev:
	            if prev:
	                entry = (prev,count)
	                lst.append(entry)
	                #print lst
	            count = 1
	            prev = character
	        else:
	            count += 1
	    else:
	        entry = (character,count)
	        lst.append(entry)
	    return lst

	encoded_dic = encode(binary_sequence)

	morse_code_string = ''

	for enc in encoded_dic:
		if(enc[0] == '1'):
			if(enc[1] < 5):
				continue
			elif(enc[1] < 30):
				morse_code_string = morse_code_string + '.'
			else:
				morse_code_string = morse_code_string + '-'
		else:
			if(enc[1] >200):
				morse_code_string = morse_code_string + ' '

	morse_code_string = morse_code_string[1:-1]

	# print(morse_code_string)
	''' dictionary containing train data'''
	morseAlphabet ={
	    "A" : ".-",
	    "B" : "-...",
	    "C" : "-.-.",
	    "D" : "-..",
	    "E" : ".",
	    "F" : "..-.",
	    "G" : "--.",
	    "H" : "....",
	    "I" : "..",
	    "J" : ".---",
	    "K" : "-.-",
	    "L" : ".-..",
	    "M" : "--",
	    "N" : "-.",
	    "O" : "---",
	    "P" : ".--.",
	    "Q" : "--.-",
	    "R" : ".-.",
	    "S" : "...",
	    "T" : "-",
	    "U" : "..-",
	    "V" : "...-",
	    "W" : ".--",
	    "X" : "-..-",
	    "Y" : "-.--",
	    "Z" : "--..",
	    " " : "/",
	    }

	inverseMorseAlphabet=dict((v,k) for (k,v) in morseAlphabet.items())

	def getChar(a):
		if(inverseMorseAlphabet.has_key(a)):
			return inverseMorseAlphabet[a]
		else:
			return ""

	morse_list = morse_code_string.split(" ");

	alphabetString = ''

	for chars in morse_list:
		alphabetString = alphabetString +  getChar(chars)

	return alphabetString

