#Project - Part 1: Sentiment Classifier

#Qn1
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(x):
    new_string = ""
    for char in x:
        if char not in punctuation_chars:
            new_string = new_string + char
        continue
    return new_string
        
word = 'wonderful'
print(word)

new_word = strip_punctuation(word)
print(new_word)

#Qn2

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

#strip function
def strip_punctuation(x):
    new_string = ""
    for char in x:
        if char not in punctuation_chars:
            new_string = new_string + char
        continue
    return new_string

# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

#calculates how many words in the string are considered positive words
print(positive_words)
def get_pos(x):
    y = x.split(" ")
    n = 0
    new_list = []
    for word in y:
        z = strip_punctuation(word)
        new_list.append(z)
        if z in positive_words:
            n = n + 1    
    print(new_list)
    return n   

#Qn3
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

#strip function
def strip_punctuation(x):
    new_string = ""
    for char in x:
        if char not in punctuation_chars:
            new_string = new_string + char
        continue
    return new_string

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

#calculates how many words in the string are considered positive words
print(negative_words)
def get_neg(x):
    y = x.split(" ")
    n = 0
    new_list = []
    for word in y:
        z = strip_punctuation(word)
        new_list.append(z)
        if z in negative_words:
            n = n + 1    
    print(new_list)
    return n         

#Qn4
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

#strip function
def strip_punctuation(x):
    new_string = ""
    for char in x:
        if char not in punctuation_chars:
            new_string = new_string + char
        continue
    return new_string

# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

#calculates how many words in the string are considered positive words
#print(negative_words)
def get_neg(x):
    y = x.split(" ")
    n = 0
    new_list = []
    for word in y:
        z = strip_punctuation(word)
        new_list.append(z)
        if z in negative_words:
            n = n + 1    
    #print(new_list)
    return n    

#calculates how many words in the string are considered positive words
#print(positive_words)
def get_pos(x):
    y = x.split(" ")
    n = 0
    new_list = []
    for word in y:
        z = strip_punctuation(word)
        new_list.append(z)
        if z in positive_words:
            n = n + 1    
    #print(new_list)
    return n   

fileconnection = open("project_twitter_data.csv", 'r')
lines = fileconnection.readlines()
header = lines[0]
field_names = header.strip().split(',')
#print(field_names)

##writing output file to csv        
outfile = open("resulting_data.csv","w")
# output the header row
outfile.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
outfile.write('\n')

for row in lines[1:]:
    vals = row.strip().split(',')
    #print(type(vals))
    pos_score = get_pos(vals[0])
    vals.append(pos_score)
    #print(pos_score)
    neg_score = get_neg(vals[0])
    vals.append(neg_score)
    net_score = pos_score - neg_score
    vals.append(net_score)
    #print(neg_score)
    vals = '{},{},{},{},{}'.format(vals[1],vals[2],vals[3],vals[4],vals[5])
    outfile.write(vals)
    outfile.write('\n')
outfile.close()
