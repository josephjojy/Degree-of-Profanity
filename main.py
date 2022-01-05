import csv

tweets = csv.reader(open('./tweets.csv','r'))
racial_slurs = csv.reader(open('./words.csv','r'))

check_words = []
for word in racial_slurs:
    check_words.append(word[0])

for row in tweets:
    sentence = row[1].split()
    count = 0
    for word in sentence:
        if word in check_words:
            count += 1
    degree_of_profanity = count/len(sentence)
    print(row[1])
    print("Degree Of Profanity: ",degree_of_profanity)
