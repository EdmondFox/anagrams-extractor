import re
open('my-anagrams.txt', 'w').close()

file = open("text.txt", "r")
myText = file.read()
file.close()

myList = re.compile(r'[^a-z]+').split(myText)

# filter() - removes empty strings from list
# list() - re-converts the iterator (generated by filter) to a list
myList = list(filter(None, myList))

# my list without empty strings and words not sorted
print(myList)

# clone list without affecting the content of the original
mySortedList = list(myList)

# sort letter in each element of the new list and to uppercase
for idx in range(len(mySortedList)):
    mySortedList[idx] = ''.join(sorted(mySortedList[idx])).upper()

# my list without empty strings and words sorted
# print(mySortedList)

# list of indexes that would be skipped if the word was checked once
myIndexes = []

for idx in range(len(mySortedList)):
    count = 0
    if idx in myIndexes:
        continue

    myAnagrams =[]

    for idy in range(idx, len(mySortedList)):
        if mySortedList[idx] == mySortedList[idy]:
            # count += 1
            myAnagrams.append(myList[idy])
            if idy not in myIndexes:
                myIndexes.append(idy)
    if len(myAnagrams) > 1:
        print(len(myAnagrams))
        for x in range(len(myAnagrams)):
            file = open("my-anagrams.txt", "a")
            if x == len(myAnagrams) - 1:
                file.write(str(myAnagrams[x]) + '\n')
            else:
                file.write(str(myAnagrams[x]).rstrip('\n') + ", ")
            file.close()
            print(myAnagrams[x])

# print(sorted(myIndexes))



