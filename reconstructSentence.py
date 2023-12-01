#reconstructSentence.py
#reads two input text files and reconstructs/combines their contents to produce the complete output

#Each input file contains words that alternate with the other file but the order of the words is reversed. The script takes one word from the end of each file and reconstructs  the full text

#Example Invocation: python3 reconstructSentence.py input1.txt input2.txt

input1_txt = ['Molloy.', 'by', 'Second', 'Embedded', 'Building', 'Techniques', 'Tools', 'Exploring', 'the',
        'site', 'the', 'This\n']

input2_txt = ['Derek', 'Edition', 'Linux', 'with', 'for', 'and', 'BeagleBone:', 'book', 'for', 'companion',
        'is\n']

input1_length = len(input1_txt) #use len function to get the length/number of words in input1.txt
input2_length = len(input2_txt)

print("\ninput1.txt: \n") #display the contents of input1.txt and the number of words
print(input1_txt)
print(input1_length)
'''
print(file1.readline())
print("Input1 length is: \n",input1_length)
'''

print("\ninput2.txt: \n") #display the contents of input2.txt and the number of words
print(input2_txt)
print(input2_length)
'''
print(file2.readline())
print("Input2 length is: \n",input2_length)
'''

input1_index = 11 #index variable for the loop
'''
input2_index = 10
'''
new_txt = [] #variable for new text/output text
'''
new_txt = ""
'''

i = 11 #last index of input1.txt variable
j = 10 #last index of input2.txt variable

for input1_index in input1_txt: #for index 11 in the input1.txt file
        if i>j: #if i is greater than j
            new_txt.append(input1_txt[i] + ' ' + input2_txt[j]) #place the contents in index j of input2.txt at the end of the contents in index i of input1.txt
            i -= 1 #decrement i by 1
            j -= 1 #decrement j by 1
print("\noutput.txt: \n",new_txt) #display the contents of the output text
