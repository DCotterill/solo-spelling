from bottle import route, run, request, template, static_file
from os import system
import random
import csv

word_meanings_week1 = {
                 "yet":"I am yet to do my homework",
                 "yes":"The opposite of no is yes",
                 # "yell":"",
                 "yells":"I dont like it when my brother yells at me",
                 "yelled":"I yelled at the dog",
                 # "yelling":"",
                 "you":"you can do it",
                 "yolk":"The egg has a white and a yolk",
                 "yoyo":"The yoyo bounced up and down",
                 "yellow":"The egg yolk is yellow",
                 "year":"A year is 365 days",
                 "yard":"I played in the back yard",
                 "yawn":"Im so tired I want to yawn",
                 "your":"These are your spelling words",
                 "choose":"You can choose what you want to eat for dinner",
                 "huge":"The earth is huge",
                 "human":"Aliens are not human",
                 "yearly":"Your birthday is yearly. Once a year",
                 "yesterday":"The day before today is yesterday",
                 "yoga":"I stretched in my yoga class",
                 "young":"The opposite of old is young",
                 # "yours":"",
                 "yourself":"Try to be yourself",
                 "youngest":"I am the youngest in the family",
                 "usually":"I usually have toast for breakfast"
}
word_meanings_week2 = {
                 "do":"what did you do today",
                 "to":"I went to bed",
                 "into":"go into the kitchen",
                 "who":"who are you?",
                 "two":"one plus one is two",
                 "boot":"I put on my boot",
                 "moon":"the moon is shining in the sky",
                 "room":"I am in my room",
                 "too":"there are too many carrots",
                 "use":"I use a spoon to eat my pudding",
                 "noon":"mid-day is called noon",
                 "knew":"I wish I knew how to spell knew",
                 "flew":"the bird flew into the sky",
                 "blew":"The wind blew and blew",
                 "broom":"I swept the floor with the broom",
                 "classroom":"the teacher was in the classroom",
                 "used":"I used my toys",
                 "using":"I am using my toys",
                 "juice":"I drank my delicious juice",
                 "grew":"the plants grew tall",
                 "threw":"I threw the ball",
                 "through":"I walked through the door",
                 #Not on the sheet, but in the homework
                 "new":"I bought some new shoes",
                 "food":"i ate all the food",
                 "cool":"you are cool",
                 "you":"you can do it",
                 "Tuesday":"It is Tuesday today"}

word_meanings_week3 = {
                 "is":"What is your name",
                 "his":"His name is Dillon",
                 "as":"As nice as pie",
                 "was":"I was on holiday",
                 "zoom":"The fast car went zoom",
                 "quiz":"We answered the questions in the quiz",
                 "prize":"You won first prize",
                 "zebra":"A zebra has black and white stripes",
                 "fizz":"The cola had a lot of fizz",
                 "buzz":"The bee went buzz",
                 "buzzing":"The bee was buzzing",
                 "close":"Please close the door",
                 "closing":"The gate kept closing",
                 "goes":"The car goes fast",
                 "please":"Please help me",
                 "present":"Here is your birthday present",
                 "quizzes":"At school we do lots of quizzes",
                 "sneeze":"Pepper can make you sneeze",
                 "sizzle":"The sausage went sizzle on the barbecue"
}

word_meanings_week4 = {
                "down": "I jumped up and down",
                "about": "I am walking about",
                "town": "I went shopping in the town",
                "round": "The circle is round",
                "count": "I can count to 100",
                "cloud": "There is a cloud in the sky",
                "clown": "A clown at the circus was funny",
                "loud": "There was a loud bang",
                "shout": "I can shout really loudly",
                "sound": "I can hear the sound",
                "how": "How about we do our homework",
                "now": "I am doing my homework now",
                "our": "Lets do our reading",
                "out": "Shall we go out?",
                "amount": "What amount of money you have",
                "flower": "The flower was pretty",
                "frown": "My face has a frown right now",
                "crown": "The queen wore a crown",
                "mountain": "I climbed the mountain",
                "mouth": "I smile with my mouth",
                "towel": "I dried myself with the towel",
                "cow": "The cow went moo",
                "ground": "I sat on the ground",
                "thousand": "I have 1000 dollars"
}

word_meanings_week5 = {
                "she":"she is a girl",
                "ship":"I am on a ship",
                "beach":"I am at the beach",
                "lunch":"I am eating lunch",
                "shelf":"The book is on the shelf",
                "sound":"I can hear the sound",
                "chip":"I am eating a chip",
                "much":"I dont have much money",
                "chain":"There is a chain around my neck",
                "chew":"I must chew my food",
                "catch":"I can catch a ball",
                "chop":"I can chop food",
                "shell":"I found a shell at the beach",
                "church":"I got married in a church",
                "wish":"I have a wish",
                "chases":"The dog chases the cat",
                "cheese":"I am eating cheese",
                "itch":"I have an itch on my leg",
                "kitchen":"I cook in the kitchen",
                "shiver":"When I am cold I shiver",
                "short":"The opposite of long is short",
                "rubbish":"The bin is full of rubbish"
                }

word_meanings_week6 = {
                "toy": "I played with the toy",
                "boy": "Dillon is a boy",
                "oil": "You need oil in your car",
                "coin": "I flipped the coin",
                "join": "You can join lego pieces together",
                "ear": "Mr Bean can wiggle his ear",
                "year": "Happy new year",
                "toys": "I bought toys from the shop",
                "here": "I live here",
                "fear": "I fear zombies",
                "near": "The boy is near the truck",
                "dear": "I wrote a letter to my dear friend",
                "deer": "There are lots of deer in this park",
                "annoy": "You annoy me",
                "boil": "The water is on the boil",
                "enjoy": "I enjoy playing Pokemon cards",
                "destroy": "I will destroy the world",
                "noise": "Shouting makes a lot of noise",
                "point": "You can point with your finger",
                "beard": "I have a long beard",
                "feared": "I have always feared zombies",
                "clear": "The sky is clear",
                "cheering": "I am cheering my friend at the soccer game"}

word_meanings_week7 = {
                # "the": "",
                # "thin": "",
                # "with": "",
                "bath": "I was dirty so had a bath",
                "path": "I walked down the path",
                # "that": "",
                # "thick": "",
                # "them": "",
                # "then": "",
                "three": "one plus two is three",
                # "these": "",
                "birthday": "We sang happy birthday",
                "month": "January is the first month of the year",
                "mouth": "my mouth is open",
                "teeth": "I bite with my teeth",
                # "thank": "",
                "third": "i came third in the race",
                "thirsty": "i was thirsty so I drank some water",
                # "gather": "",
                "feather": "as light as a feather"
                }

word_meanings_week8 = {
                "air": "",
                "pair": "",
                "hair": "",
                "chair": "",
                "where": "",
                "their": "",
                "stairs": "",
                "bare": "",
                "bear": "",
                "dare": "",
                "fair": "",
                "repair": "",
                "anywhere": "",
                "square": "",
                "careful": "",
                "downstairs": "",
                "scare": ""
                }
all_word_meanings = dict(word_meanings_week7.items()
                         + word_meanings_week6.items()
                         + word_meanings_week5.items()
                         + word_meanings_week4.items()
                         + word_meanings_week3.items()
                         + word_meanings_week2.items())
all_words = all_word_meanings.keys()


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
    return template ('welcome')

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

    return template("spelling", person_name=person_name, correct_number=str(len(correct_list[correct_threshold])))


@route('/spell-word')
def spell_word():
    global word
    global word_blanks

    choose_next_word()

    word_blanks = "_ " * len(word)
    word_speech = word + '.  As in ' + all_word_meanings[word]

    create_correct_lists()
    progress_message = "You can spell " + str(len(correct_list[correct_threshold])) + " out of " + \
                       str(len(all_words)) + " correctly."

    percent = 100 * len(correct_list[correct_threshold]) / len(all_words)

    return template("spell-word", word_speech=word_speech, word_blanks=word_blanks, correct_number = str(len(correct_list[correct_threshold])),
                                total_words = str(len(all_words)), progress_message = progress_message,
                                percent = str(int(percent)))

@route('/spell-word', method='POST')
def do_spell_word():
    global guess

    guess = request.forms.get("guess")

    if (len(word) != len(guess)):
        message = "Thats not right. The word " + word + " has " + str(len(word)) + " letters."
        # system("say " + message)
        correct_count[word] = 0

        return template("wrong_length", length=str(len(word)), message=message)

    if (guess == word):
        if (word_blanks == "_ " * len(word)):  #there's not been a hint
            correct_count[word] = int(correct_count.get(word,0)) + 1
        writer = csv.writer(open(person_name + '-spelling.csv', mode='w'))
        for key, value in correct_count.items():
            writer.writerow([key, value])

        return template("correct")
    else:
        correct_count[word] = 0

        return template("wrong_spelling")

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

    return template("spell-word", word_speech=word_speech, word_blanks=word_blanks, correct_number = str(len(correct_list[correct_threshold])),
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

run(host='0.0.0.0', port=8080, debug=True)

