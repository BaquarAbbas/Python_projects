# function to create the chatbot
# we have the read_only to false so the chatbot learns from the user input as 
def create_bot(name):
    from chatterbot import ChatBot
    Bot = ChatBot(name = name,
                  read_only = False,                  
                  logic_adapters = ["chatterbot.logic.BestMatch"],                 
                  storage_adapter = "chatterbot.storage.SQLStorageAdapter")
    return Bot

# function to train the bot with a variety of topics
# the language we have chosen is english
# we can train the bot for other languages as well
def train_all_data(Bot):
    from chatterbot.trainers import ChatterBotCorpusTrainer
    corpus_trainer = ChatterBotCorpusTrainer(Bot)
    corpus_trainer.train("chatterbot.corpus.english")

# function to train the bot with custom data
# it uses ListTrainer to train data from lists 
def custom_train(Bot, conversation):
    from chatterbot.trainers import ListTrainer
    trainer = ListTrainer(Bot)
    trainer.train(conversation)

# function to start and take responses from the chatbot
# the chatbot stays running unless a word is typed from the bye_list 
def start_chatbot(Bot):
    print('\033c')
    print("Hello, I am Jordan. How can I help you")
    bye_list = ["bye jordan", "bye", "good bye"] 
    
    while (True):
        user_input = input("me: ")   
        if user_input.lower() in bye_list:
            print("Jordan: Good bye and have a blessed day!")
            break
        
        response = Bot.get_response(user_input)
        print("Jordan:", response)

# create chatbot 
bot = create_bot('Jordan')

# train all data
train_all_data(bot)
## check identity
identity = input("State your identity please: ")
# rules for responding to different identities
if identity == "Mark":
    print("Welcome, Mark. Happy to have you at home.")

elif identity == "Jane":
    print("Mark is out right now, but you are welcome to the house.")

else:
    print("Your access is denied here.")
    exit()

# train chatbot with your custom data
house_owner = [
    "Who is the owner of the house?",
    "Mark Nicholas"
]
custom_train(bot, house_owner)
#cutom_data
if identity == 'Mark':   
    city_born = [
        "Where was I born?",
        "Mark, you were born in Seattle."
    ]

    fav_book = [
        "What is my favourite book?",
        "That is easy. Your favourite book is The Great Gatsby."
    ]

    fav_movie = [
        "What is my favourite movie?",
        "You have watched Interstellar more times than I can count."
    ]

    fav_sports = [
        "What is my favourite sport?",
        "You have always loved baseball."
    ]
    # train chatbot with your custom data
    custom_train(home_bot, city_born)
    custom_train(home_bot, fav_book)
    custom_train(home_bot, fav_movie)
    custom_train(home_bot, fav_sports)


# start chatbot
start_chatbot(bot)
