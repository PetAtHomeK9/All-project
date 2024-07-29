#CBT Exams on Dog and Snake Plant


EXAM = [
    {"question" : "What is the most popular dog breed in the United States?",
"option" : { "A" :"Labrador Retriever",
"B" : "German Shepherd",
"C" : "Golden Retriever",
"D" : "Bulldog"},
    
"Answer" : "C"},
    
{"question" : "What is the smallest dog breed in the world?",
"option" : {"A" : "Pomeranian",
"B" : "Chihuahua",
"C" : "Dachshund",
"D" : "Shih Tzu"},
"Answer" : "B"
   },

{"question" : "What breed is known as the “King of Terriers”?",
"option" : {"A" : "Airedale Terrier",
"B" : "Scottish Terrier",
"C" : "Bull Terrier",
"D" : "Jack Russell Terrier"},
"Answer" : "A"
},

{"question" : "Which dog breed is famous for its blue-black tongue?",
"option" : {"A" : "Dalmatian",
"B" : 'Chow Chow',
"C" : "Shar Pei",
"D" : "Siberian Husky"},
"Answer" : "B"
},

{"question" : "What is the name of the dog in the classic movie 'The Wizard of Oz'?",
"option" : {"A" : "Toto",
"B" : "Max",
"C" : "Rover",
"D" : "Buddy"},
"Answer" : "A"
},

{"question" : "Which dog breed is known for its distinctive “wrinkled” appearance?",
"option" : {"A" : "Beagle",
"B" : "Basset Hound",
"C" : "Pug",
"D" : "Boxer"},
"Answer" : "C"
},

{"question" : "What breed is the fastest dog in the world?",
"option" : {"A" : "Greyhound",
"B" : "Whippet",
"C" : "Dalmatian",
"D" : "Border Collie"},
"Answer" : "A"
},

{"question" : "Which breed is often used by police and military forces?",
"option" : {"A" : "Beagle",
"B" : "Border Collie",
"C" : "German Shepherd",
"D" : "Golden Retriever"},
"Answer" : "C"},

{"question" : "What is a group of puppies called?",
"option" : {"A" : "Pack",
"B" : "Litter",
"C" : "Herd",
"D" : "Clutch"},
"Answer" : "B"},

{"question" : "Which dog breed has a reputation for being “nanny dogs” due to their good nature with children?",
"option" : {"A" : "Poodle",
"B" : "Beagle",
"C" : "Staffordshire Bull Terrier",
"D" : "Dachshund"},
"Answer" : "C"},

{"question" : "What is another common name for the Snake Plant?",
"option" : {"A" : "Peace Lily",
"B" : "Spider Plant",
"C" : "Mother-in-Law’s Tongue",
"D" : "Aloe Vera"},
"Answer" : "C"},

{"question" : "What type of light conditions does a Snake Plant prefer?",
"option" : {"A" : "Low light",
"B" : "Bright, indirect light",
"C" : "Direct sunlight",
"D" : "Shade"},
"Answer" : "B"},

{"question" : "How often should you water a Snake Plant?",
"option" : {"A" : "Every day",
"B" : 'Once a week',
"C" : "Every two weeks",
"D" : "When the soil is completely dry"},
"Answer" : "D"},

{"question" : "What is the main benefit of having a Snake Plant in your home?",
"option" : {"A" : "It blooms frequently",
"B" : "It purifies the air",
"C" : "It repels insects",
"D" : "It requires frequent watering"},
"Answer" : "B"},

{"question" : "Which of the following best describes the ideal soil for a Snake Plant?",
"option" : {"A" : "Heavy clay soil",
"B" : "Sandy soil",
"C" : "Well-draining soil",
"D" : "Moist, rich soil"},
"Answer" : "C"}


]

EXAM_SCORE = 0
for question in EXAM:
    print(question["question"])
    print(question["option"])
    Answer = input("Enter Your correct answer: ").capitalize()
    if Answer == question["Answer"]:
        EXAM_SCORE += 1
    else:
        pass

print("The assessment is completed")
print(f"Your Score Is: {EXAM_SCORE}/15")