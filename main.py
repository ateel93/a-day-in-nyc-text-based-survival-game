print("Welcome!")
name = input("What is your name? ")
health = 5


def health_check():
    if health < 1:
        print("Your health is below 1. You Lost!")
        exit()
    else: 
        pass
     
start = input(f"Hi {name}! Do you wish to start your day? ")

if start.lower() == "yes":
    print("May it go smoothly!...")
    print("RIIIIIIIING. Your sleep filled eyes focus and its 8:45AM.")
    print("You realize that you have slept past your scheduled wake up time but while you are trying to turn off the alarm, it will not let you without answering a question.")
    print("'I am now the quintessential New Yorker, and even though I am over 100 years old, I have only had work done on my face once.'")
    statue_liberty = input("Who am I?")
    if statue_liberty.lower() == "statue of liberty":
        health += 2
        print("Correct. 2 bars added")
        print(f'New health: {health}')
    else: 
         health -= 2
         health_check()
         print("Incorrect!")
         print(f'New health: {health}')

    print("After you silence the alarm, you quickly jump out of bed and throw on clothes. You need your morning fix but you cant decide if you want coffee or tea?")
    coffee_or_tea = input("Coffee or Tea?")
    if coffee_or_tea.lower() == "coffee":
        print("You make a cup of coffee and put it in your to go mug.")
    else: print("You make a cup of tea and put it in your to go mug.")

    print("As you step out onto the busy street, you check your phone to make sure the MTA is running without delays. Before you are able to see, a riddle pops up on the screen...") 
    print("What train takes you from a circle to a square?")

    one_train = input("Enter your answer here:")

    if one_train.lower() == "one train" or one_train.lower() == "1 train":
         
         health += 2
         print("Correct!")
         print(f'New health: {health}')
         print("Your phone unlocks and shows that there are no delays. You enter the train platform and both the express and local train arrive simultaneously. Seems like your morning chaos streak is ending. Now, which train will you choose?")
         local_or_express = input("Local or Express?")
         if local_or_express.lower() == "local":
            print("You jump on the local train and to your surprise, are able to snag a seat. The doors close and you begin to make your way downtown. As the train pulls out of the station, your subway car jerks causing you to spill your hot morning drink in your lap. Do you get off the train or stay on?")
            get_off = input("Get off or stay on?")
            if get_off.lower() == "get off":
                print("After fighting your way through the people trying to get on the train, You get off and angrily toss your cup in the closest trash can. Above ground, you find a bodega and grab a stack of napkins.")
            else: print("You stick it out, knowing that getting off will only make you more late.... Once you arrive to the station, you fight to get off and climb the steps to street level.")
         else: 
            print("You jump on the express, knowing it will substantially cut down on your commute time. The Local train pulls out of the station but the Express train does not and the breaks let out a loud hiss. The operator comes on and says that the train is being held due to someone being on the train tracks. Another Local train pulls into the station a few minutes later.")
            express_get_off = input("Do you switch or wait it out?")
            if express_get_off.lower() == "switch":
                        print("You decide that the express probably wont be moving for a while so you dash across the platform and jump on right before the doors close. The train pulls off and you are on your way.")
            else: print("You decide to wait it out and lucky for you, the train starts moving.")
            
         print("As you approach the street corner and wait for the traffic to clear, a pigeon sh*ts on you.")
         im_screaming = input("Do you scream or suck it up?")
         if im_screaming.lower() == "scream":
            print("You scream profanity at the top of your lungs. Everyone looks at you but you cant care any less. ")
         else: print("Even though today is going horribly.. it wont break you! While you want to scream, you instead ball up your fists, grit your teeth and keep walking.")
         print("You cross the street and continue your journey. There are tourists with maps everywhere. Some one sees you coming and waves to ask you for directions. You wip out your phone to look busy and again the screen is locked with another question")
         print("What was special about the construction of the Empire State Building?")
         print("A: It was built on a wooden frame")
         print("B: It was built with no detailed plans")
         print("C: It was built quickly and under budget")
         empire_question = input("Whats your answer?")
         if empire_question.lower() == "C":
            
             health += 2
             print("Correct!") 
             print(f'New health: {health}')
             print("They seem to have bought your lie and you quickly manuever away from them")
         else: 
             health -= 2
             health_check()
             print("Wrong.")
             print(f'New health: {health}')
             print("They dont seem to have bought your lie and B-line it towards you. 'Do you know where they Empire State Building is?' they ask, when you are standing a block away from it. You give them the directions and speed walk off. Not wanting to be roped into additional pleasantries")


    else: 
        health -= 2
        health_check()
        print("Incorrect!")
        print(f'New health: {health}')
        print("Your phone flashes red but unlocks. You quickly open the MTA app and see that everything by you is delayed due to a subway derailment.")
        walk_bus = input("Do you walk the 50 blocks or take the bus?")
        if walk_bus.lower() == "Bus":
             print("You decide to take the bus and by the looks of it, so did everyone else. As it bounces down the street you hold on for dear life. You make it about 20 blocks then the bus driver slams on the breaks. You look up and see that there is an accident.")
             get_off_walk = input("Do you stay on or get off?")
             if get_off_walk.lower() == "get off":
                  print("You ask to be let off and high tail it walking as fast as you can.")
             else: print("You stay on. Though its a slow down, you do not have the energy to walk. As the bus inches along, you catch up on emails.")
        else: 
             print("You decide to walk the 50 blocks. Whats the point in rushing now?")        

        print("Another question pops up on your screen. ")
        print("What does the Verrazano bridge connect?")
        print("A: Staten Island and Bronx")
        print("B: Staten Island and Brooklyn")
        print("C: Manhattan and Staten Island")
        verrazano = input("Whats your answer?")
        if verrazano.lower() == "B":
            health()
            print("Correct!")
            print(f'New health: {health}')
        else:
            health -= 2
            health_check()
            print("Incorrect")
            print(f'New health: {health}')
            print("Your phone again flashes red.")
        print("While you are waiting to cross the street, a taxi cab that is speeding by splashes you with street water.")
        print("Do you...")
        print("A: Stop and scream at the top of your lungs")
        print("B: Grit your teeth and keep on.")
        scream_walk = input("A or B?")
        if scream_walk.lower() == "A":
             print("While you are still wet, you feel a tad bit better.")
        else: print("Today is trying to break you, but you won't let it.")
        print("You continue on what now feels like a journey. As you walk, you cannot help but look at other people's faces, searching for reactions to see if anyone else is having the same luck.")
        print("On the next street. There are tourists everywhere. Some one sees you coming and waves to ask you for directions.")
        print("Do you stop and give them directions?")
        yes_no = input("Yes or No?")
        if yes_no.lower() == "Yes":
            print("You stop and give them directions. They thank you and you quickly walk off.")
        else: print("You decide not to make eye contact and keep walking, now speeding up your already fast pace.")


    print("On the next block, you look up and see a billboard with another riddle.")
    print("Where in New York City do you travel up to 65 miles per hour, and yet always end up where you have started?")
    cyclone = input("What is your answer?")
    if cyclone.lower() == "cyclone":
        health += 2
        print("Correct!")
        print(f'New health: {health}')
        print("You continue on your journey, now nearing your destination. Finally!")
        print("CONGRATULATIONS. YOU'VE MADE IT")
    else:
        health -= 2
        print("Incorrect!")
        print(f'New health: {health}')
        print("As you continue on, a large group of tourists bumps past you forcing you to step on a subway grate in the sidewalk. You hear a loud creek as it gives way, throwing you into a bodega cellar.")
        health_check()



else: 
     print("Goodbye!")
     exit()
   

   