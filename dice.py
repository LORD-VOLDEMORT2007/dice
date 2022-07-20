import random


value = input("to roll a dice say 'y' to roll say 'n' to quit")

if(value == "y"):
    y = "true"
elif(value == "n"):
    y = "false"

while y == "true":
    no = random.randint(1,6)
    
    if(no == 1):
        print("""
        [     ]
        [ 0   ]
        [     ]""")
        break
    if(no == 2):
        print("""
        [     ]
        [ 00  ]
        [     ]""")
        break
    if(no == 3):
        print("""
        [     ]
        [ 000 ]
        [     ]""")
        break
    if(no == 4):
        print("""
        [     ]
        [ 00  ]
        [ 00  ]
        [     ]""")
        break
    if(no == 5):
        print("""
        [ 00  ]
        [  0  ]
        [ 00  ]""")
        break
    if(no == 6):
        print("""
        [     ]
        [ 000 ]
        [ 000 ]
        [     ]""")
        break


