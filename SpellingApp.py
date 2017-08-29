from bottle import route, run, request, template, static_file
import os
import random
import csv

word_meanings_week9 = {"ever":"",
                       "over":"",
                       "dollar":"",
                       "other":"",
                       "better":"",
                       "dinner":"",
                       "mother":"",
                       "father":"",
                       "caterpillar":"",
                       "doctor":"",
                       "butter":"",
                       "letter":"",
                       "actor":"",
                       "under":"",
                       "over":"",
                       "paper":"",
                       "corner":"",
                       "December":"",
                       "brother":"",
                       "butterfly":"",
                       "November":"",
                       }
all_word_meanings = {}
all_words = {}


person_name = ""
correct_list = {}
correct_threshold = 3
correct_count = {}
word = ""
word_blanks = ""

def create_correct_lists():
    global correct_list
    correct_list = {}

    for i in range(1, correct_threshold + 1):
        current_list = correct_list.get(i, [])
        for k, v in correct_count.iteritems():
            if int(v) == int(i):
                current_list.append(k)
        correct_list[i] = current_list

def choose_next_word():
    global word
    word = random.choice(all_words)
    while (correct_count.get(word,0) >= correct_threshold):
        word = random.choice(all_words)

def find_first_wrong_letter(word, guess):
    i = 0
    while (word[i] == guess[i]):
        i = i + 1
    return i


@route('/spelling')
def spelling():
    return template ('templates/welcome')

@route('/spelling', method='POST')
def do_spelling():
    global correct_count
    global person_name
    correct_count = {}

    person_name = request.forms.get("name")

    try:
        with open("./" + person_name.lower() + "-spelling.csv", 'r') as lines:
            reader = csv.reader(lines)
            correct_count = dict((rows[0],int(rows[1])) for rows in reader)
    except IOError:
            correct_count = {}

    create_correct_lists()

    return template("templates/spelling", person_name=person_name, correct_number=str(len(correct_list[correct_threshold])))


@route('/spell-word')
def spell_word():
    global word
    global word_blanks

    choose_next_word()

    word_blanks = "_ " * len(word)
    print all_word_meanings[word]
    word_speech = word + '.  As in ' + all_word_meanings[word]

    create_correct_lists()
    progress_message = "You can spell " + str(len(correct_list[correct_threshold])) + " out of " + \
                       str(len(all_words)) + " correctly."

    percent = 100 * len(correct_list[correct_threshold]) / len(all_words)

    return template("templates/spell-word", word_speech=word_speech, word_blanks=word_blanks,
                                correct_number = str(len(correct_list[correct_threshold])),
                                total_words = str(len(all_words)), progress_message = progress_message,
                                percent = str(int(percent)))

@route('/spell-word', method='POST')
def do_spell_word():
    global guess

    guess = request.forms.get("guess").lower()

    if (len(word) != len(guess)):
        message = "Thats not right. The word " + word + " has " + str(len(word)) + " letters."
        # system("say " + message)
        correct_count[word] = 0

        return template("templates/wrong_length", length=str(len(word)), message=message)

    if (guess.lower() == word.lower()):
        if (word_blanks == "_ " * len(word)):  #there's not been a hint
            correct_count[word] = int(correct_count.get(word,0)) + 1
        writer = csv.writer(open(person_name + '-spelling.csv', mode='w'))
        for key, value in correct_count.items():
            writer.writerow([key, value])

        return template("templates/correct")
    else:
        correct_count[word] = 0

        return template("templates/wrong_spelling")

@route('/try-again', method = 'POST')
def do_try_again():
    global word
    global word_blanks
    global guess

    if request.forms.get("hint"):
        print "asked for a hint"
        wrong_letter = find_first_wrong_letter(word, guess)
        word_blanks = word_blanks[0:wrong_letter*2] + word[wrong_letter] + word_blanks[wrong_letter*2 + 1:len(word_blanks)]

    word_speech = word + '. As in ' + all_word_meanings[word]
    # system('say ' + word_speech)

    create_correct_lists()
    progress_message = "You can spell " + str(len(correct_list[correct_threshold])) + " out of " + \
                       str(len(all_words)) + " correctly."

    percent = 100 * len(correct_list[correct_threshold]) / len(all_words)

    return template("templates/spell-word", word_speech=word_speech, word_blanks=word_blanks,
                                correct_number = str(len(correct_list[correct_threshold])),
                                total_words = str(len(all_words)), progress_message = progress_message,
                                percent = str(int(percent)))
@route('/css/<filename>')
def server_static(filename):
    return static_file(filename, root='./css/')

@route('/js/<filename>')
def server_static(filename):
    return static_file(filename, root='./js/')

@route('/fonts/<filename>')
def server_static(filename):
    return static_file(filename, root='./fonts/')

def load_words_and_definitions():
    word_meanings = {}
    try:
        for file in os.listdir("words"):
            if file.endswith(".csv"):
                with open("words/" + file, 'r') as words:
                    reader = csv.reader(words)
                    print file
                    word_meanings[file] = dict((rows[0],rows[1]) for rows in reader)
    except IOError:
        word_meanings = {}

    print word_meanings
    global all_word_meanings
    print "----"
    for words in word_meanings.values():
        print words
        all_word_meanings.update(words)

    global all_words
    all_words = all_word_meanings.keys()


## MAIN

load_words_and_definitions()
run(host='0.0.0.0', port=8080, debug=True)

