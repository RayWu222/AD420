import sys, os, re
import logging
import time
import logging.config 
import configparser

#start the execution time 
start_time = time.time()

logging.basicConfig(filename='consoleapp.log', level= logging.DEBUG, format = "%(levelname)s %(asctime)s -%(message)s", filemode='w')
#logging.config.fileConfig('logging_config.ini', disable_existing_loggers=True)

#testing logging to see if it log into consoleapp log file
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")

#get the text file from command line argument
strTextFile = str(sys.argv[1])
#get read or write from command line argument
readOrWrite = str(sys.argv[2])
x = ""

#read method
def read():
    #open the text file and read the file
    f = open(strTextFile, "r")
    toText = f.read()

    #found all the 'imperdiet' in the text file
    count = len(re.findall(r"\bimperdiet\b", toText))
    print("number of imperdiet appears in this text file: " + str(count))
    #take out all the empty spaces
    toText = toText.replace('\n\n', '\n')
    #split line by line and put it into a list
    toTextList = toText.splitlines()
    #calculate length of list
    lineListLength = len(toTextList)

    whileCounter = 0
    imperdietAppearedInList = 0
    #creating a list for calculating average time 
    averageTimeList = [None]*lineListLength
    #print("averageTimeList length: " + str(len(averageTimeList)))

    #read line by line to see if imperdiet is in the line
    imperdietInLineList = []
    while(whileCounter < lineListLength):
        startReadLineTime = time.time()
        if(re.search(r"\bimperdiet\b", toTextList[whileCounter])):
            startTimeToLookForImperdiet = time.time()
            imperdietAppearedInList +=1
            executeTime = (time.time() - startReadLineTime)
            averageTimeList[whileCounter] = executeTime
            finishedTime = (time.time() - startTimeToLookForImperdiet)
            imperdietInLineList.append(finishedTime)
            whileCounter+=1
        else:
            executeTime = (time.time() - startReadLineTime)
            averageTimeList[whileCounter] = executeTime
            whileCounter +=1

    logging.info("Average time to read a line from file: " + str(round(sum(averageTimeList) /len(averageTimeList),3)) + " seconds")
    logging.info("Average time to find the word 'imperdiet' in the line " + str(round(sum(imperdietInLineList) /len(imperdietInLineList),3)) + " seconds" )
    print("imperdiet appeared in this many lines: " + str(imperdietAppearedInList))
    logging.info("Execution time: %s seconds" % (round(time.time() - start_time,3)))

writeList = []
averageWriteTime =  []



#write method
def write():
    #clear text file
    open("test.txt", "w").close
    sentencesWithImperdiet = 0
    sentenceCounters = 0
    userInput = 'y'

    #let user keep writing to the file 
    while(True):
        val = input("Please enter a sentences: ")
        sentenceCounters+=1

        #if user input have 'imperdiet' in it +1 to the counter and addi it to list
        if(re.match(r"\bimperdiet\b",val)):
            sentencesWithImperdiet +=1
        writeList.append(val)
        writeFileTime = time.time()
        f = open(strTextFile, "a")
        f.write(val+"\n")
        f.close()

        #get the start and end time of writing to file
        endTime = (time.time() - writeFileTime)
        averageWriteTime.append(endTime)
        userInput = input("Continue - 'y' or 'n' to exit: ")

        if(userInput == "n"):
            break
        #if user enter anything else 
        elif(userInput != "y"):
            print("please enter a valid input")
            userInput = input("Continue -'y' or 'n' to exit: ")

    print("Users entered this many sentences: " + str(sentenceCounters))
    print("'imperdiet' appeared in the user input': " + str(sentencesWithImperdiet))
    logging.info("Average time to write a line to file: " + str(round(sum(averageWriteTime) /len(averageWriteTime),3)) + " seconds")
    

#this function look for how many sentences the word "imperidet" appeared by putting into a list
def imperdietAppeared():
    loggingTimeList =  []
    lengthOfSentences = len(writeList)
    whileCounter = 0
    countWordinSentence = 0
    while(whileCounter < lengthOfSentences):
        startTime = time.time()

        if re.search(r"\bimperdiet\b", writeList[whileCounter]):
            endTime = (time.time() - startTime)
            loggingTimeList.append(endTime)
            countWordinSentence +=1
            whileCounter+=1
        else:
            whileCounter+=1
    print("imperdiet appeared in : " + str(countWordinSentence) + " sentences")
    logging.info("Average time to find the word 'imperdiet' in the line: " + str(sum(loggingTimeList) /len(loggingTimeList)) + " seconds")


#main function - initalize at the very beginning
def main():

    logging.info("Execution time: %s seconds" % round(time.time() - start_time,3))
    #if user put write as second argument 
    if readOrWrite == "read":
        read()

    #if uer enter write as second argument
    elif readOrWrite == "write":
        write()
        imperdietAppeared()
        logging.info("Execution time: %s seconds" % round(time.time() - start_time,3))
    #if not read or write return this 
    else:
        print("Sorry, this program only accept read or write as arguments")


if __name__ == "__main__":
    main()