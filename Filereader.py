def filecheck(f):
    
    file = open(f,'r') #opening inputted file and preparing to read it into a list 
    x = file.readlines()

    #Initializing variables
    totallines = 0
    comments = 0
    singlecomments = 0
    comments_in_block = 0
    block_line_comments = 0
    todo = 0
    
    totallines = len(x)#Finding the total number of lines

    for i in range(len(x)):
        #Iterating through each line to look for TODO and total number of comments
        if '#' in x[i] or '//' in x[i] or '*' in x[i] or '/*' in x[i] or '*/' in x[i]:
            comments+=1
        if 'TODO' in x[i]:
            todo +=1

        #Looking for single comments
        if '#' in x[i] and '#' not in x[i+1] and '#' not in x[i-1]: #Looking for comment symbols used in python
            singlecomments +=1
            
        if '//' in x[i]:
            singlecomments+=1
                
        #Looking for comments in block and number of block lines increments respective variables
        if '#' in x[i] and '#' in x[i+1]: #Checks to see if current line and next line include a comment
            comments_in_block +=1
            
        #Checks for the end of a block of comments indicating that there is a block 
        elif '#' in x[i] and '#'  not in x[i+1] and '#' in x[i-1]:
            block_line_comments +=1
            comments_in_block +=1
            

        if '/*' in x[i] or '*' in x[i] or '*/' in x[i]:
            comments_in_block +=1
            if '*/' in x[i]:
                block_line_comments +=1
        
    file.close()

    return totallines,comments,singlecomments,comments_in_block, block_line_comments,todo
        
while True:
    filename = input("Input file name: ")  #Taking user input for file to be used
    if filename[0] == '.':                  #Used to catch wrong input by user and prompt them to enter it again
        print("Error: cannot input file starting with '.")  #Ensures that input has extension and filname doesn't start with '.'
    elif '.' not in filename:
        print("Error: only file with an extension is accepted")
    
    else:
        break

result = filecheck(filename)
print("Total # of lines: ",result[0])
print("Total # of comment lines: ",result[1])
print("Total # of single comment lines: ",result[2])
print("Total # of comments lines within block comments: ",result[3])
print("Total # of block line comments: ",result[4])
print("Total # of TODO's: ",result[5])
