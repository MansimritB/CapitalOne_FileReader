#Mansimrit Bajwa
#FileReader.py
#Assumption: Commenting syntax used for program files Python,C,Java
#Assumption: When finding total number of lines whitespaces are considered in the linecount
#Assumption: File that will be checked is in the same directory as FileReader.py

def filecheck(f):

    try:
        file = open(f,'r') #opening inputted file and preparing to read it into a list
    except IOError:
        print("File does not exist")                        #check to see if the file exists in the directory
        return "N/A","N/A","N/A","N/A","N/A","N/A"           #Stops the program, returning strings indicating error
    
    x = file.readlines()  #Variable x used to store all the data being read from file

    #Initializing variables
    totallines = 0
    comments = 0
    singlecomments = 0
    comments_in_block = 0
    block_line_comments = 0
    todo = 0
    
    totallines = len(x)#Finding the total number of lines

    if f.endswith(".py"):# Check to see if file is a python file 
        for i in range(len(x)):
            if '#' in x[i]:
                comments+=1
            if 'TODO' in x[i]:
                todo +=1
            #Looking for single comments
            if '#' in x[i] and '#' not in x[i+1] and '#' not in x[i-1]: #Looking for comment syntax used in python
                singlecomments +=1
            #Looking for comments in block and number of block lines increments respective variables
            if '#' in x[i] and '#' in x[i+1]: #Checks to see if current line and next line include a comment
                comments_in_block +=1           #Looking for comment syntax used in python
            
            #Checks for the end of a block of comments indicating that there is a block 
            elif '#' in x[i] and '#'  not in x[i+1] and '#' in x[i-1]: #Looking for comment syntax used in python
                block_line_comments +=1
                comments_in_block +=1
            
        
    else: #Covers other program files like C,Java
        for i in range(len(x)):
            #Iterating through each line to look for TODO and total number of comments
     
            if '//' in x[i] or '*' in x[i] or '/*' in x[i] or '*/' in x[i]:
                comments+=1
            if 'TODO' in x[i]:
                todo +=1
            #Looking for SingleComments    
            if '//' in x[i]:
                singlecomments+=1
            
            if '/*' in x[i] or '*' in x[i] or '*/' in x[i]: #Looking for blockcomments and how many comments inside
                comments_in_block +=1
                if '*/' in x[i]:
                    block_line_comments +=1                 #Checks for the end of block
        
    file.close()

    return totallines,comments,singlecomments,comments_in_block, block_line_comments,todo
        
while True:
    filename = input("Input file name: ")  #Taking user input for file to be used

    if filename[0] == '.':                  #Used to catch wrong input by user and prompt them to enter it again
        print("Error: cannot input file starting with '.'")  #Ensures that input has extension and filename doesn't start with '.'
    elif '.' not in filename:
        print("Error: only file with an extension is accepted")

    else:
        break
#Displaying results
result = filecheck(filename)
print("Total # of lines: ",result[0])
print("Total # of comment lines: ",result[1])
print("Total # of single comment lines: ",result[2])
print("Total # of comments lines within block comments: ",result[3])
print("Total # of block line comments: ",result[4])
print("Total # of TODO's: ",result[5])
