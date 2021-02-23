#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

count = 0
fname = input("Enter a file name: ")
fhand = open (fname)
list1 = list()
dict1 = dict()
for line in fhand:
    if line.startswith('From'):
        if line.startswith('From:'):
            continue
        else:
            count = count+1
            words=line.split()
            str1 = ''.join(words[5])
            list1.append(str1[0:2])
for word in list1:
    dict1[word] = dict1.get(word,0)+1
for i,y in sorted(dict1.items()):
    print(i,y)
            
            