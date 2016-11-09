import random
import csv
import easygui
from os import system

word_meanings = {"come":"please come over here",
                 "again":"can you do it again",
                 "boat":"the boat is in the water",
                 "look":"look at me",
                 "could":"could you help me"}

gold_words = ["a","and","be", "I","in","is", "it","of","that","the","to","was"]
red_words = ["all","as","are","at","but","for","had","have","he","her","his","not","on","one","said","so","they","we",
             "with","you"]
blue_words = ["an","by","do","go","if","me","my","no","up","or"]
green_words = ["big","can","did","get","has","him","new","now","off","old","our","out","see","she","two","who"]
orange_words = ["back","bee","came","down","from","into","just","like","made","much","over",
                "them","this","well","went","when"]
indigo_words = ["call","come","here","make","must","only","some","then","were","what","will","your"]
violet_words = ["about","before","could","first","little","look","more","other","right","their",
                "there","want","where","which"]
pink_words = ["after","am","boy","day","eat","five","fly","girl","good","help","home","jump",
              "play","ran","read","saw","sing","sit","think","us"]
purple_words = ["again","ask","best","bring","far","find","give","how","kind","left","man","mother","own","room",
                "say","step","these","too","walk","wish"]
aqua_words = ["always","away","bird","dog","fast","four","going","hand","keep","let","many","night","people","round",
              "school","take","thing","tree","water","work"]
lime_words = ["another","bad","black","don't","father","found","got","head","know","live","may","once","put","run",
              "should","tell","three","under","white","would"]
lemon_words = ["any","because","blue","every","fell","gave","green","house","last","long","morning","open","red",
               "sat","soon","than","time","very","why","year"]

test_words = ["come", "again", "boat", "could"]
all_words = test_words

    # gold_words \
    #         + red_words \
    #         + blue_words \
    #         + green_words \
    #         + orange_words \
    #         + indigo_words \
    #         + violet_words \
    #         + pink_words \
    #         + purple_words \
    #         + aqua_words \
    #         + lime_words \
    #         + lemon_words

person_name = easygui.enterbox('Input your name (filename of saved progress):')

correct_list = {}

correct_threshold = 3
try:
    with open("./" + person_name + "-spelling.csv", 'r') as lines:
        reader = csv.reader(lines)
        correct_count = dict((rows[0],int(rows[1])) for rows in reader)
except IOError:
        correct_count = {}


def create_correct_lists():
    for i in range(1, correct_threshold + 1):
        current_list = correct_list.get(i, [])
        for k, v in correct_count.iteritems():
            if int(v) == int(i):
                current_list.append(k)
        correct_list[i] = current_list

correct_list = {}
create_correct_lists()

easygui.msgbox("Number of words you know how to spell: " + str(len(correct_list[correct_threshold]))
        + "\n\n" + str(correct_list.get(3,[])))

print correct_list.get(1,[])
print correct_list.get(2,[])
print correct_list.get(3,[])

def choose_next_word():
    next_word = random.choice(all_words)
    while (correct_count.get(next_word,0) >= correct_threshold):
        next_word = random.choice(all_words)
    return next_word

def find_first_wrong_letter(word, guess):
    i = 0
    while (word[i] == guess[i]):
        i = i + 1
    return i

correct_answer = 'No'
while (correct_answer != 'Exit'):
    word = choose_next_word()
    word_blanks = "_ " * len(word)
    word_speech = word + '. As in ' + word_meanings[word]

    system('say ' + word_speech)

    answer = easygui.enterbox(msg=word_blanks)

    while answer != word:
        if (len(word) != len(answer)):
            message = "Thats not right, the word " + word + " has " + str(len(word)) + " letters."
            system("say " + message)

        else:
            message = "Thats not right, would you like a hint?"
            system("say " + message)
            hint_yn = easygui.ynbox(message)
            if hint_yn:
                wrong_letter = find_first_wrong_letter(word, answer)
                word_blanks = word_blanks[0:wrong_letter*2] + word[wrong_letter] + word_blanks[wrong_letter*2 + 1:len(word_blanks)]


        system('say ' + word_speech)
        answer = easygui.enterbox(msg=word_blanks)
        correct_count[word] = 0

    correct_count[word] = int(correct_count.get(word,0)) + 1
    message = "Well done! You got it right."
    system("say " + message)
    easygui.textbox(message)

print correct_count

def check_all_colour_known(colour_words):
    for word in colour_words:
        if (correct_count.get(word, 0) < correct_threshold):
            return False
    return True

correct_list = {}
create_correct_lists()

known_words_message = "Number of words you know: " + str(len(correct_list[correct_threshold]))\
        + "\n\n" + str(correct_list.get(3,[]))

if (check_all_colour_known(gold_words)):
    known_words_message += "\n\nYou know all GOLD words"
if (check_all_colour_known(red_words)):
    known_words_message += "\n\nYou know all RED words"
if (check_all_colour_known(blue_words)):
    known_words_message += "\n\nYou know all BLUE words"
if (check_all_colour_known(green_words)):
    known_words_message += "\n\nYou know all GREEN words"
if (check_all_colour_known(orange_words)):
    known_words_message += "\n\nYou know all ORANGE words"
if (check_all_colour_known(indigo_words)):
    known_words_message += "\n\nYou know all INDIGO words"
if (check_all_colour_known(violet_words)):
    known_words_message += "\n\nYou know all VIOLET words"
if (check_all_colour_known(pink_words)):
    known_words_message += "\n\nYou know all PINK words"
# if (check_all_colour_known()):
#     known_words_message += "\n\nYou know all  words"

easygui.msgbox(known_words_message)

writer = csv.writer(open(person_name + '-spelling.csv', mode='w'))
for key, value in correct_count.items():
    writer.writerow([key, value])





