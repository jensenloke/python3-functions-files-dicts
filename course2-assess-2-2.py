#Assessment: Dictionary Accumulation

#Qn1
Junior = {'SI 206':4, 'SI 310':4, 'BL 300':3, 'TO 313':3, 'BCOM 350':1, 'MO 300':3}
credits = 0
for j in Junior:
    credits = credits + Junior[j]
print(credits)

#Qn2
str1 = "peter piper picked a peck of pickled peppers"
freq = {} # start with an empty dictionary
for c in str1:
    if c not in freq:
        # we have not seen this character before, so initialize a counter for it
        freq[c] = 0

    #whether we've seen it before or not, increment its counter
    freq[c] = freq[c] + 1
print(freq)

#Qn3
s1 = "hello"
counts = {} # start with an empty dictionary
for c in s1:
    if c not in counts:
        # we have not seen this character before, so initialize a counter for it
        counts[c] = 0

    #whether we've seen it before or not, increment its counter
    counts[c] = counts[c] + 1
print(counts)

#Qn4
str1 = "I wish I wish with all my heart to fly with dragons in a land apart"
str1_list = str1.split(" ")
print(str1_list)

freq_words = {}
for word in str1_list:
    if word not in freq_words:
        # we have not seen this word before, so initialize a counter for it
        freq_words[word] = 0

    #whether we've seen it before or not, increment its counter
    freq_words[word] = freq_words[word] + 1

print(freq_words)

#Qn5
sent = "Singing in the rain and playing in the rain are two entirely different situations but both can be good"
str1_list = sent.split(" ")

wrd_d = {}
for word in str1_list:
    if word not in wrd_d:
        # we have not seen this word before, so initialize a counter for it
        wrd_d[word] = 0

    #whether we've seen it before or not, increment its counter
    wrd_d[word] = wrd_d[word] + 1

print(wrd_d)

#Qn6
sally = "sally sells sea shells by the sea shore"
characters = {} # start with an empty dictionary
for c in sally:
    if c not in characters:
        # we have not seen this character before, so initialize a counter for it
        characters[c] = 0
    #whether we've seen it before or not, increment its counter
    characters[c] = characters[c] + 1
print(characters)

ks = characters.keys()
best_key_so_far = list(ks)[0]  # Have to turn ks into a real list before using [] to select an item
for k in ks:
    if characters[k] > characters[best_key_so_far]:
        best_key_so_far = k

print("key " + best_key_so_far + " has the highest value, " + str(characters[best_key_so_far]))
best_char = best_key_so_far
print(best_char)

#Qn7
sally = "sally sells sea shells by the sea shore and by the road"
characters = {} # start with an empty dictionary
for c in sally:
    if c not in characters:
        # we have not seen this character before, so initialize a counter for it
        characters[c] = 0
    #whether we've seen it before or not, increment its counter
    characters[c] = characters[c] + 1
print(characters)

ks = characters.keys()
best_key_so_far = list(ks)[0]  # Have to turn ks into a real list before using [] to select an item
for k in ks:
    if characters[k] < characters[best_key_so_far]:
        best_key_so_far = k

print("key " + best_key_so_far + " has the lowest value, " + str(characters[best_key_so_far]))
worst_char = best_key_so_far
print(worst_char)

#Qn8
string1 = "There is a tide in the affairs of men, Which taken at the flood, leads on to fortune. Omitted, all the voyage of their life is bound in shallows and in miseries. On such a full sea are we now afloat. And we must take the current when it serves, or lose our ventures."
string1 = string1.lower()
letter_counts = {} # start with an empty dictionary
for c in string1:
    if c not in letter_counts:
        # we have not seen this character before, so initialize a counter for it
        letter_counts[c] = 0

    #whether we've seen it before or not, increment its counter
    letter_counts[c] = letter_counts[c] + 1
print(letter_counts)

#Qn9
p = "Summer is a great time to go outside. You have to be careful of the sun though because of the heat."
p = p.lower()
low_d = {}
for c in p:
    if c not in low_d:
        # we have not seen this character before, so initialize a counter for it
        low_d[c] = 0

    #whether we've seen it before or not, increment its counter
    low_d[c] = low_d[c] + 1
print(low_d)
