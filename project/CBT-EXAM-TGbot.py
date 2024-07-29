import telebot
from question_bank import EXAMS

API_TOKEN = '7185484495:AAHj7NgAw9E45ePbSzPYxup3TteyjMC7h-Y'

bot = telebot.TeleBot(API_TOKEN)

user_scores = {}

# Handle '/start' command
@bot.message_handler(commands=['start'])
def start(message):
    global user_scores
    user_id = message.chat.id
    user_scores[user_id] = {"current_question": 0, "score": 0}
    send_question(message)

# Function to send a question
def send_question(message):
    global user_scores
    user_id = message.chat.id
    question_index = user_scores[user_id]["current_question"]
    if question_index < len(EXAMS):
        question = EXAMS[question_index]["question"]
        options = EXAMS[question_index]["options"]
        question_and_options = f"{question}\nA. {options['A']}\nB. {options['B']}\nC. {options['C']}\nD. {options['D']}"
        bot.send_message(user_id, question_and_options)
    else:
        end_message(message)

# Function to send end message
def end_message(message):
    user_id = message.chat.id
    score = user_scores[user_id]["score"]
    bot.send_message(user_id, f"Congratulations! Your final score is {score} out of {len(EXAMS)}.")

# Handle responses
@bot.message_handler(func=lambda message: True)
def handle_response(message):
    global user_scores
    user_id = message.chat.id
    question_index = user_scores[user_id]["current_question"]
    if question_index < len(EXAMS):
        correct_answer = EXAMS[question_index]["answer"]
        if message.text.upper() == correct_answer:
            user_scores[user_id]["score"] += 1
        user_scores[user_id]["current_question"] += 1
        send_question(message)

bot.infinity_polling()
