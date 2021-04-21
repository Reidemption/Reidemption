#Reid Gubler Tue. Thur. 1:30

import os.path

#returns a list of the lines in the file
#REMOVE NEWLINE CHARACTER FROM THE END OF EACH LINE
#if file is empty or does not exist, return empty list
def fileToList(filename):
    #return empty list if file doesn't exist
    list_of_lines = []
    if not os.path.isfile(filename):
        return []
    f = open(filename, 'r')
    lines = f.readlines()
    for line in lines:
        stripped = line.strip()
        list_of_lines.append(stripped)
    f.close()
    return list_of_lines

#strings is a list of strings and returns the first string
#if list if empty return an empty string
def returnFirstString(strings):
    if not strings:
        return ''
    return strings[0]

#both parameters are strings
#return True if both strands have a length greater than zero
#False otherwise
def strandsAreNotEmpty(strand1, strand2):
    return len(strand1) > 0 and len(strand2) > 0

#return True if both strands are of equal length
def strandsAreEqualLengths(strand1, strand2):
    return len(strand1) == len(strand2)

#target is a string
#candidate is a string
#overlap is an integer
#Checks to see if the target and candidate strands have an overlap of overlap characters
#return True if they overlap
#slice target and candidate with overlap
def candidateOverlapsTarget(target, candidate, overlap):
    return target[len(target)-overlap:] == candidate[:overlap]
    

#both params are strings
#Find the largest overlap and return that size
#if either strand if empty or not the same length, return '-1'
#use functions strandsAreNotEmpty() and strandsAreEqualLengths()
#pair the start of one with the end of the other
def findLargestOverlap(target, candidate):
    check = 0
    if strandsAreNotEmpty(target, candidate) and strandsAreEqualLengths(target, candidate):
        #code to determine the length of the overlap
        for i in range(len(target)+1):
            if candidateOverlapsTarget(target,candidate,i):
                check = i
        return check
    return -1

#candidates = list of strings
#Examine each candidate in the list and determine the candidate with largest overlap
#use findLargestOverlap() function
#if 2 candidates have the same overlap keep the first one
#returns a tuple containing the candidate string with largest overlap and the size of the overlap
#if no candidate overlaps, return an empty string with 0 as the overlap ('',0)
def findBestCandidate(target, candidates):
    x = 0
    empty_string = ''
    for i in range(len(candidates)):
        if findLargestOverlap(target,candidates[i]) > x:
            x = findLargestOverlap(target,candidates[i])
            empty_string = candidates[i]
    return (empty_string,x)
#print(findBestCandidate('ABC', ['BBC', 'BCC', 'BCA', 'CBA'])) # ('BCC', 2)

#joins the target and candidate strands together and merges them 
#return the combined string
def joinTwoStrands(target, candidate, overlap):
    #'abcdefg', 'defgabc', 4), 'abcdefgabc',
    if overlap != 0:
        return target[:len(target)-overlap] + candidate
    return target




#returns nothing
#asks the user for the filename of the target strand file and candidate strands file
#use functions fileToList() returnFirstString() findBestCandidate()
#print the combined strand
#joinTwoStrands()
def main():
    target = input('Target strand filename: ')
    candidate = input('Candidate strands filename: ')
    
    newtarget = fileToList(target)
    newcandidate = fileToList(candidate)
     
    target2 = returnFirstString(newtarget)
    candidate2 = findBestCandidate(target2, newcandidate)
     
    print(joinTwoStrands(target2, candidate2[0], candidate2[1]))



if __name__ == '__main__':
    main()