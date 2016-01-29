import random
import csv
import easygui

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

all_words = gold_words \
            + red_words \
            + blue_words \
            + green_words \
            + orange_words \
            + indigo_words \
            + violet_words \
            + pink_words \
            # + purple_words \
            # + aqua_words \
            # + lime_words \
            # + lemon_words

person_name = easygui.enterbox('Input your name (filename of saved progress):')
correct_list = {}

correct_threshold = 3
try:
    with open("./" + person_name + ".csv", 'r') as lines:
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

easygui.msgbox("Number of words you know: " + str(len(correct_list[correct_threshold]))
        + "\n\n" + str(correct_list.get(3,[])))

print correct_list.get(1,[])
print correct_list.get(2,[])
print correct_list.get(3,[])

def choose_next_word():
    next_word = random.choice(all_words)
    while (correct_count.get(next_word,0) >= correct_threshold):
        next_word = random.choice(all_words)
    return next_word


correct_answer = 'No'
while (correct_answer != 'Exit'):
    word = choose_next_word()
    correct_answer = easygui.buttonbox(msg=word, choices=('Yes', 'No', 'Exit'), default_choice='Yes')
    if correct_answer == 'Yes':
        correct_count[word] = int(correct_count.get(word,0)) + 1
    else:
        correct_count[word] = 0

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

writer = csv.writer(open(person_name + '.csv', mode='w'))
for key, value in correct_count.items():
    writer.writerow([key, value])





