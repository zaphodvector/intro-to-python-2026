"""
----------------------------------------------------------------------------------------------------------
    Name:	EVW_Week13_Text_Sample
    Author:	Ed Weber
    Language:	Python
    Date:	2025-01-08
    Purpose:	The purpose of this program is to provide a brief multi-step process to explain
                some of the more common file handling classes, methods, and functions that are
                part of the Python environment.  This is NOT a comprehensive demonstration of
                everything that Python has to offer in this regard.  However, it should be 
                enough to help new programmers begin to work with reading and writing data
                using files.
----------------------------------------------------------------------------------------------------------
    Change Log
----------------------------------------------------------------------------------------------------------
    Who		Date		Reason
    EVW		2025-01-08	Original Version of Code
----------------------------------------------------------------------------------------------------------
"""
import random

def main():
    # Step 1 - just opening files
    strOriginalFileMessage = "Hello World - in a file!"
    strMsg = 'This program demonstrates basic Python file manipulations.\n'
    strMsg += f'  First we will create a file consisting of the phrase {strOriginalFileMessage}\n'
    strMsg += "  The command we will use to open (and create if necessary) is:\n"
    strMsg += "  \thdlFile = open('./EVW_RawTextFile','w')\n"
    strMsg += "\nLet's take a moment to discuss file handles, file paths, file names,\n"
    strMsg += "  file types and extensions, and access modes and permissions.\n"
    fncPauseAndReflect(strMsg)
    hdlFile = open('./EVW_RawTextFile','w')
    strMsg = "The file is now open and ready to receive data.  If this is the first time\n"
    strMsg += "  this program is running, then the file will not have existed and so the\n"
    strMsg += "  file has now been created and opened for writing in text format.\n"
    strMsg += "But if this is the second (or more) time that we are running the program,\n"
    strMsg += "  then this file access is currently overwriting the old file...!\n"
    fncPauseAndReflect(strMsg)

    # Step 2 - writing data into a file and creating the file if necessary
    hdlFile.write(strOriginalFileMessage)
    strMsg = 'The value {strOriginalFileMessage} which was'
    strMsg += f'{strOriginalFileMessage}\n'
    strMsg += f'  was written to the file.  (Actually, the output was written to the output buffer\n'    
    strMsg += f'  so it may not actually be on the disk until either a buffer flush occurs or\n'
    strMsg += f'  until the file is closed and the cleanup process empties the buffer...)\n'
    strMsg += f"Let's discuss...\n"
    fncPauseAndReflect(strMsg)

    # step 3 - closing a file to flush the buffer and release the file handle
    fncCloseOpenFile(hdlFile)
    strMsg = f'The newly created file has now been closed.  This releases the system resources\n'
    strMsg += f'  and also ensures that any pending write requests (buffers) are finished\n'    
    strMsg += f'  and flushed.\n'
    strMsg += f"Now, let's review the created file and its output by first looking at the\n"
    strMsg += f"  file using some external tools like a simple text editor.  After we\n"
    strMsg += f"  are done looking at the file, we will continue with the next steps...\n"
    fncPauseAndReflect(strMsg)

    # step 4 - opening an existing file to overwrite the content.
    hdlFile = open('./EVW_RawTextFile','w')
    strMsg = 'Opening the file now (a 2nd time) with the exact same command as before, will\n'
    strMsg += f'  actually open the file as though it were new and all of the old data will\n'
    strMsg += f'  be completely overwritten.\n'    
    strMsg += f"This time, we are going to write 10 phrases into the file and then\n"
    strMsg += f'  close the file when we are done.\n'
    strMsg += f"Let's discuss...\n"
    fncPauseAndReflect(strMsg)
    strUserInput = input("What phrase would you like me to put in the file? ")
    for i in range(10):
        hdlFile.write(f'{strUserInput} ... was written {i + 1} time(s).\n' )
    fncCloseOpenFile(hdlFile)
    strMsg = f'The file has be re-written with the new output.  Look at the file\n'
    strMsg += f'  externally as you did last time.  Note:  the actual command that\n'
    strMsg += f"  was used to write the output was: \n"
    strMsg += r"       hdlFile.write(f'{strUserInput} ... was written {i + 1} time(s).')"
    strMsg += f"\nLet's discuss...\n"
    fncPauseAndReflect(strMsg)

    # step 5 - opening a file to append data
    hdlFile = open('./EVW_RawTextFile','a')
    strMsg = 'Opening the file now (a 3rd time) with the same command as before but with\n'
    strMsg += f'  the "a" (append) mode instead of the "w" (write) mode.\n'
    strMsg += f'  The file is opened and the pointer is moved (seek) to the end of the file.\n'    
    strMsg += f"This time, we are going to append 10,000 random integers between 1 and 100.\n"
    strMsg += f"Let's discuss...\n"
    fncPauseAndReflect(strMsg)
    for i in range(10000):
        hdlFile.write(f'{str(random.randrange(1,100))}\n' )
    fncCloseOpenFile(hdlFile)
    strMsg = f'The file has be appended with the additional output.  Look at the file\n'
    strMsg += f'  externally as you did last time.  Observe the file structure and decide \n'
    strMsg += f'  if you think this is a good thing or a bad thing...'
    strMsg += f"\nLet's discuss...\n"
    fncPauseAndReflect(strMsg)

    # step 6 - opening a file using the with command and reading only from the file
    strMsg = 'Opening the file now (a 4th time) but this time we are using the "with"\n'
    strMsg += f'  command and the "r" (read-only) mode instead of the "a" or "w" mode.\n'
    strMsg += f'  The file is open and the file handle object now supports additional file\n'
    strMsg += f'  methods such as read(), readline(), readlines() and others!\n'    
    strMsg += f"This time, since we know we have those first ten text lines,\n"
    strMsg += f'  we will first loop through the first 10 reads and just show the lines on\n'
    strMsg += f"  the screen.  Then we'll handle the rest of the file a different way.\n"
    strMsg += f"Let's discuss...\n"
    fncPauseAndReflect(strMsg)
    with open('./EVW_RawTextFile','r') as hdlFile:
        for i in range(10):    # loop through first 10 'header' (text) lines of data in the file
            str1FileLine = hdlFile.readline()
            print(f'File Read of one line only - Line #{i + 1} - contains: {str1FileLine}',end='')
    strMsg = f'The file was read and the first 10 lines were read and printed.\n'
    strMsg += f'  However, since this was accomplished using a "with" block, \n'
    strMsg += f'  and now we are executing code outside of that "with" block,\n'
    strMsg += f'  the termination of the "with" block has closed the file,\n'
    strMsg += f'  (resetting the file pointer) and releasing all file resources.\n'
    strMsg += f"\nLet's discuss...\n"
    fncPauseAndReflect(strMsg)

    # step 7 - opening a file and attempting to read (and skip) the headers to get to
    # the numeric data only.
    strMsg = 'Opening the file now (a 5th time).  This time, we will read (and skip)\n'
    strMsg += f'  the first 10 text header lines (like last time), but then we will\n'
    strMsg += f'  attempt to read ALL of the rest of the file be using the read()\n'
    strMsg += f'  method.\n'    
    strMsg += f"Since the first 10 lines have been read and skipped, we are hoping that\n"
    strMsg += f'  the read command will just read all of the rest of the file from the\n'
    strMsg += f"  current file pointer until the end.\n"
    strMsg += f"Let's discuss...\n"
    fncPauseAndReflect(strMsg)
    print('Reading (and skipping) the first 10 "header" lines...')
    with open('./EVW_RawTextFile','r') as hdlFile:
        for i in range(10):    # loop through first 10 'header' (text) lines of data in the file
            str1FileLine = hdlFile.readline()
        print('The loop to skip the header text entries just completed!')
        print('Now attempting to read the rest of the entire file into a new')
        print(r'variable using the command strRestOfFile = hdlFile.read()')
        strRestOfFile = hdlFile.read()
    strMsg = f'The read() command has been completed. It was the last line in the "with" block.\n'
    strMsg += f'  Now, we need to examine the variable to see what was actually read in. \n'
    strMsg += f'  len(strRestOfFile) = {len(strRestOfFile)}\n'
    strMsg += f'  Trying to carve off a slice of the first 100 bytes of the new variable:\n'
    strMsg += f'  (strRestOfFile[:100]) = {(strRestOfFile[:100])}\n'
    strMsg += f'  What does this examination tell us about the read() method?\n'
    strMsg += f"\nLet's discuss...\n"
    fncPauseAndReflect(strMsg)

    # step 8 - process the read data
    strMsg = f"That's right!\n"
    strMsg += f'  The read() operation reads all of the remaining content of a file (from\n'
    strMsg += f'  the current file pointer) through the end of the file whereas the\n'
    strMsg += f'  readline() operation only reads a single line.  The readlines() operation\n'
    strMsg += f'  is like the read() but then parses the lines into a list for easier processing.\n'
    strMsg += f'What does this examination tell us about the readlines() method?\n'
    strMsg += f"\nLet's discuss...\n"
    fncPauseAndReflect(strMsg)

    # step 9 - opening a file and attempting to read (and skip) the headers to get to
    # the numeric data only.
    strMsg = 'Opening the file now (a 6th time).  This time, we will read (and skip)\n'
    strMsg += f'  the first 10 text header lines (like last time), but then we will\n'
    strMsg += f'  attempt to read ALL of the rest of the file be using the readlines()\n'
    strMsg += f'  method.\n'    
    strMsg += f"The readlines() method will read all of the rest of the file from the\n"
    strMsg += f'  current file pointer until the end of the file and put all of the\n'
    strMsg += f"  read data into a list with each line as a separate element.\n"
    strMsg += f"Let's discuss...\n"
    fncPauseAndReflect(strMsg)
    print('Reading (and skipping) the first 10 "header" lines...')
    with open('./EVW_RawTextFile','r') as hdlFile:
        for i in range(10):    # loop through first 10 'header' (text) lines of data in the file
            str1FileLine = hdlFile.readline()
        print('The loop to skip the header text entries just completed!')
        print('Now attempting to read the rest of the entire file into a new')
        print(r'variable using the command lstRestOfFile = hdlFile.readlines()')
        lstRestOfFile = hdlFile.readlines()
    strMsg = f'The read() command has been completed as the last line in the "with" block.\n'
    strMsg += f'  Now, we need to parse the returned list. To do this, we will loop through\n'
    strMsg += f'  the returned list and strip off the whitespace (and carriage returns)\n'
    strMsg += f'  so we are left with just the numeric data stored in lstTheNumbersOnly.\n'
    lstTheNumbersOnly = []
    for strOneLine in lstRestOfFile:
        lstTheNumbersOnly.append(int(strOneLine.strip()))
    strMsg += f'With the numbers now stripped and converted into actual ints, we can do\n'
    strMsg += f'  further analysis on the numbers themselves.  Here are a couple of quick\n'
    strMsg += f'  observations:\n'
    strMsg += f"\nLet's discuss...\n"
    fncPauseAndReflect(strMsg)
    print(f"There were: {len(lstTheNumbersOnly)} items in the rest of the file.")
    intCountEvens = len([num for num in lstTheNumbersOnly if num % 2 == 0])
    print(f"There were: {intCountEvens} even numbers in the data.")
    fltAvgAll = sum(lstTheNumbersOnly) / len(lstTheNumbersOnly)
    print(f"The average of the numbers was: {fltAvgAll:.2f}.")
    strMsg = "And we could just keep on analyzing...!!!"
    fncPauseAndReflect(strMsg)
    print(f"{('> ' * 16)} That is all folx! {('< ' * 16)}")


def fncCloseOpenFile(hdlFile2Close=None):
    if(hdlFile2Close is None):
        return False
    else:
        hdlFile2Close.close()
        return True


def fncPauseAndReflect(strMsg = '',sep='-',rpt=80):
    '''Function to allow a message to be displayed after a configurable separator line.
    Then, waits for the user to press the enter key before returning.
    '''
    print(sep * rpt)
    print(strMsg)
    input('Press the Enter Key when ready to continue...')

if (__name__) == '__main__':
    main()