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
    #'abcdef', 'fedcba', 2
    t = overlap
    candidate = candidate[::-1]
    return target[:t] == candidate[:t]
    

#both params are strings
#Find the largest overlap and return that size
#if either strand if empty or not the same length, return '-1'
#use functions strandsAreNotEmpty() and strandsAreEqualLengths()
#pair the start of one with the end of the other
def findLargestOverlap(target, candidate):
    check = 1
    if strandsAreNotEmpty(target, candidate) and strandsAreEqualLengths(target, candidate):
        #code to determine the length of the overlap
        for i in range(len(target)):
            if target[i] == candidate[0-check]:
                check += 1
                #if 
            return check
    return '-1'
#target = string
#candidates = list of strings
#Examine each candidate in the list and determine the candidate with largest overlap
#use findLargestOverlap() function
#if 2 candidates have the same overlap keep the first one
#returns a tuple containing the candidate string with largest overlap and the size of the overlap
#if no candidate overlaps, return an empty string with 0 as the overlap ('',0)
def findBestCandidate(target, candidates):
    pass

#joins the target and candidate strands together and merges them 
#return the combined string
def joinTwoStrands(target, candidate, overlap):
    #check and see if there are problems later
    if overlap != 0:
        return target[:overlap-1] + candidate
    return target + candidate




#returns nothing
#asks the user for the filename of the target strand file and candidate strands file
#use functions fileToList() returnFirstString() findBestCandidate()
#print the combined strand
#joinTwoStrands()
def main():
    pass



#if __name__ == '__main__':
#    main()



#tests
#print(joinTwoStrands('abcef', 'cefgh', 3))
#print(findLargestOverlap('sdssaaa', 'aaadsds'))
print(candidateOverlapsTarget('abcdef', 'fsddgcba', 1))