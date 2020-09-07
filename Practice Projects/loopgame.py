# Area 1


print("Hello, ______. Wow this won't work at all... ")
input1 = input("What do I call you ______?")

print("Hell0 " + input1 + "!!")
input2 = input("Ok " + input1 + ". Are you ready to begin your adventure? (yes / no)")


if input2.strip().lower() == "yes":
    print("Ok lets get this started!")
    input3 = input("You wake up in a dark room, a small light flickers from the far end.(Stand up / Remain still): ")
   
    if input3.strip().lower() == "remain still":
        print("You lay in silence for a little bit.")
        input4 = input("You lay there for what seems like hours trying to recall what is going on. The last thing you recall is going to sleep, around 10 PM approximately. You lump inching closer and closer to you in the dim light from the other side of the room. (Get away! / Remain still)")
        
        if input4.lower().strip() == "get away":
            print("You quickly get up and head to the opposite side of the room.")
        # Dead, Start over.
        if input4.lower().strip() == "remain still":
            print("The lump slowly makes its way over to you, it turns out it is an old crippled man. He observes you for a second and the slowly slips a knife in your neck. You are dead.")
            print("Reload the program if you would like to retry your adventure!")
        else:
            print("Please ener a valid command.")
    
    if input3.lower().strip() == "stand up":
        print("You stand up, trying to think of how you got here.")
        input5 = input("You try to stand up, and barely make it to your feet with the help of the nearby wall. After a couple minutes you feel the life coming back to your legs. You then notice a lump inching closer and closer to you in the dimg light from the other side of the room. (Attack it / Get away) ")

        if input5.lower().strip() == "attack it":
            print("You attack the lump, kicking it with full force.")
        if input5.lower().strip() == "get away":
            print("You try to avoid it, quickly shifting from one side of the dark room to another. No matter which way you go the lumps seems to follow, albeit at a very slow pace")
        else:
            print("Please ener a valid command.")

    
    else:
        print("Please enter a valid command.")

else:
    print("Well I am sorry to hear that.")


