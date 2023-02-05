from peewee import *
import psycopg2

db = PostgresqlDatabase('flashcards', user='postgres', password='12345', host='localhost', port=5432)

db.connect()

class  BaseModel(Model):
    class Meta: 
        database = db

class flashcards(BaseModel):
    front = CharField()
    back = CharField()


# db.drop_tables(flashcards)
# db.create_tables([flashcards])

# React = flashcards(front='React', back='React is a Javascript Frontend framework')
# React.save()
# CSS = flashcards(front='CSS', back= 'CSS is a language for specifying how documents are presented to users')
# CSS.save()


# print(getFlashcard.front, getFlashcard.back)

# This counter variable is to keep track of the card id
counter = 1
i = 5
Incorrect =[]
Correct =[]

while i < 6:
    action = input('What would you like to do? (create, study, quit)\n')

    if action == 'study':
        how_many = int(input('How many cards would you like to study?\n'))
        for x in range(how_many):
            getFlashcard = flashcards.get(flashcards.id == counter)

            answer = input(f'{getFlashcard.front}\n')
            
            if answer == getFlashcard.back:
                print('You got it!')
                Correct += {getFlashcard.front}
            else: 
                print(f'Incorrect, the answer is: {getFlashcard.back}')
                Incorrect += {getFlashcard.front}
            counter = counter + 1
        else:            
            print(f'All Done!  Here is a list of the topics you got right: {Correct}, and wrong: {Incorrect}')
            counter =  1
    elif action == 'create': 
        f_card = input('Type the specific term the card will be about Ex. React or Data Structures\n')
        b_card = input('Type the description of the term Ex. "MongoDb is a Database"\n')
        new_card = flashcards(front= f_card, back= b_card)
        new_card.save()
    elif action == 'quit':
        i = 7
else:
    print("Quitting already? this is why your mother doesn't love you!")





# ************ DONT FORGET TO ADD A WAY TO TRACK HOW MANY TIMES A PERSON GETS A SPECIFIC CARD WRONG *****************