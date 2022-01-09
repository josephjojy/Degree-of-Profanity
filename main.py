import csv
import sys

def deg_of_profanity(check_words,tweets):
    for row in tweets:
        sentence = row[1].split()
        count = 0
        for word in sentence:
            if word in check_words:
                count += 1
        degree_of_profanity = count/len(sentence)
        print(row[1])
        print("Degree Of Profanity: ",degree_of_profanity)


def check_words_array(racial_slurs):
    check_words = []
    for word in racial_slurs:
        check_words.append(word[0])
    return check_words


def main():

    tweets_file = sys.argv[1]
    words_file = sys.argv[2]

    tweets = csv.reader(open(tweets_file,'r'))
    racial_slurs = csv.reader(open(words_file,'r'))

    check_words = check_words_array(racial_slurs)

    deg_of_profanity(check_words,tweets)


if __name__=="__main__":
    main()



