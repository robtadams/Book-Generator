"""
File name: library.py
Author: Robin Adams
Date: 4/18/2022
Last updated: 4/19/2022
"""

### Imports ###
import random
from titles import titles
from nouns import nouns
from adjectives import adj
from verbs import verbs
###############

"""
makeBook():
|   Helper function for recMakeBook()
"""
def makeBook():

    # Pick a title format...
    randTitle = titles[random.randint(0, len(titles) - 1)]

    #... generate a book with the randomly selected title format
    return recMakeBook(randTitle, 0)

"""
recMakeBook(strTitle, startIndex)
|   Recursive funtion to generate a book title
|   
|   strTitle:
|   |   String
|   |   Is formatted as a title on first execution
|   |   Will become modified by the function
|                
|   startIndex:
|   |   Integer
|   |   The index of where the function should start looking for an open bracket
|   |   Initialized to 0 on the first execution
"""
def recMakeBook(strTitle, startIndex):
    # Find the index of the next open bracket
    openBracketIndex = strTitle.find('[',startIndex)

    # If there is no open bracket...
    if openBracketIndex == -1:
        #... return the string
        return strTitle

    # Find the index of the next close bracket
    closeBracketIndex = strTitle.find(']',openBracketIndex)

    # Construct a string from the open bracket to the close bracket
    # [Noun], [Adj], [Verb], or [Title]
    strSeg = strTitle[openBracketIndex:closeBracketIndex + 1]

    # Find the matching case...
    match strSeg:

        # If strSeg is [Noun]...
        case "[Noun]":

            #print(strSeg)

            #... generate a random noun...
            randNoun = nouns[random.randint(0, len(nouns) -1)]
            
            #... and then replace [Noun] with randNoun
            strTitle = strTitle.replace("[Noun]", randNoun, 1)

        # If strSeg is [Adj]...
        case "[Adj]":

            #print(strSeg)
    
            #... generate a random adjective...
            randAdj = adj[random.randint(0, len(adj) -1)]

            #... and then replace [Adj] with randAdj
            strTitle = strTitle.replace("[Adj]", randAdj, 1)

        # If strSeg is [Verb]...
        case "[Verb]":

            #print(strSeg)

            #... generate a random verb...
            randVerb = verbs[random.randint(0, len(verbs) - 1)]

            #... and then replace [Verb] with randVerb
            strTitle = strTitle.replace("[Verb]", randVerb, 1)

        # If strSeg is [Title]...
        case "[Title]":

            #print(strSeg)

            #... generate a new title...
            newTitle = titles[random.randint(0, len(titles) - 2)]

            #... and then replace [Title] with newTitle, recursively
            strTitle = strTitle.replace("[Title]", recMakeBook(newTitle, 0), 1)

        # If strSeg is not any of the above...
        case default:
            
            #... print an error message
            print("Error: Syntax Error in Title String")

    
    # Find the index of the next open bracket for later use
    nextBracketIndex = strTitle.find('[',0)

    # If there is no other open bracket...
    if nextBracketIndex == -1:
        
        #... return the modified strTitle
        return strTitle

    # If there is an open bracket...
    else:
        
        #... recursively call recMakeBook...
        #... passing the modified strTitle...
        #... and the index of the next open bracket
        return recMakeBook(strTitle, nextBracketIndex)

"""
main():
|   Asks user how many books they want to generate
|   Generates the user inputed number of books
|   Recursively run main() until user quits
"""
def main():

    while True:
        
        # Ask the user who many books they want to generate
        var = input("How many books would you like to make? ")

        # Try to convert the user input into a string
        try:
            var = int(var)
            
        # If the user doesn't put in a number...
        except:
            
            #... print an error...
            print("Please enter a number")

            #... and try again
            continue

        # If the user enters 0...
        if var == 0:

            #... exit the program
            return

        # Generate the books
        for i in range(0, var):
            
            # Print some formatting, and call makeBook()
            print(i + 1, ":", makeBook())

        # Print for formatting
        print()

main()
