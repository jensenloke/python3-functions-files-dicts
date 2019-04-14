#course_2_assessment_1
#Due: 2018-11-25 01:28:00

#Qn1
fileref = open("travel_plans.txt","r")
num = len(fileref.read())

#Qn2
fileref = open("emotion_words.txt","r")
num_lines = 0
num_words = 0 
for line in fileref:
    words = line.split()
    num_words += len(words)
print(num_words)

#Qn3
fileref = open("school_prompt.txt","r")
num_lines = 0
for line in fileref.readlines():
    num_lines += 1
print(num_lines)

#Qn4
fileref = open("school_prompt.txt", "r")
fileref = fileref.read()
beginning_chars = fileref[0:30]
print(beginning_chars)

#Qn5
fileref = open("school_prompt.txt", "r")
fileref = fileref.readlines()
three = []
for line in fileref:
    words = line.split()
    three.append(words[2])
print(three)

#Qn6
emotions = []
fileref = open("emotion_words.txt","r")
for line in fileref.readlines():
    words = line.split()
    emotions.append(words[0])
print(emotions)

#Qn8
fileref = open("travel_plans.txt","r")
first_chars = fileref.read()[0:33]
print(first_chars)

#Qn9
fileref = open("school_prompt.txt","r")
words = fileref.read()
words = words.strip()
word_list = words.split()
print(word_list)

p_words = []
for word in word_list:
    if "p" in word:
        p_words.append(word)
print(p_words)
               
