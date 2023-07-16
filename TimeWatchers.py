game_loop = True

def path3():
    print("You step into the TimeWatcher and arrive in the Wild West.")
    print("You land in a deserted town.")
    print("You see a gang of bandits approaching you.")
    print("The gang has been paid by Titron to cause chaos in town.")
    print("You must stop them!")
    print("\nHow will you stop them?")
    print("1. Negotiate with the bandits")
    print("2. Engage in a shootout")
    choice8 = input("\nEnter a number: ")
    if choice8 == "1":
        print("The bandits agreed to your deal.")
        print("They have stopped terrorizng the town.")
        print("You have saved this era!")
        print("You have been teleported back to TimeWatcher HQ.")
    elif choice8 == "2":
        print("You pull out your pistol and start shooting.")
        print("Every shot missed!")
        print("The bandits shoot back...")
        print("All of there shots hit")
        print("You are dead!")
        print("            ****GAME OVER****                   ")
        print("You have been teleported back to TimeWatcher HQ.")
    else:
        print("Invalid choice. Please input valid option.")


def path2():
    print("You step into the TimeWatcher and arrive in Ancient Egypt.")
    print("You land outside a large pyramid.")
    print("You walk into the entrance to see two paths")
    print("On the wall, you see hieroglyphs.")
    print()
    print(",-.    ,-~~\ \      ,-.       ,-.                       ")
    print("| |     (   \ \    <,- \_____/  `      ||\/             ")
    print("| .-==-. |\. \ \     /  ___. \....     |`-'_     .-==-. ")
    print("|/_______]_]`\ \ ,_(__/ ,_(__`=.`''===.'   `---/______")
    print()
    print("You need to translate this to get the correct path.")
    print("\nHow will you get the translation?")
    print("1. Seek assistance from a nearby noble.")
    print("2. Take your luck on the path.")
    choice4 = input("\nEnter a number: ")
    if choice4 == "1":
        print("You ask a noble for help.")
        print("He examines the wall.")
        print("The noble tells you the wall says \"Stay Left\"")
        print("Which way will you go?")
        print("1. Left")
        print("2. Right")
        choice5 = input("Enter a number: ")
        if choice5 == "1":
            print("You make it to the end of the path.")
            print("You see an empty pedestal.")
            print("There is supposed to be an ancient relic on it.")
            print("You must find and return it before the pyramid collapses.")
            print("You see a secret passway with a glowing light.")
            print("You walk down the path and see the ancient relic")
            print("You pick it up and return it to the pedestal.")
            print("The pyramid begins to shake and the pedestal sinks into the ground.")
            print("Behind you, you see the exit closing.")
            print("What will you do?")
            print("1. Watch the exit close")
            print("2. Run toward the exit")
            choice6 = input("Enter a number: ")
            if choice6 == "1":
                print("You stand where you are.")
                print("A boulder falls from above and crushes you.")
                print("            ****GAME OVER****                   ")
                print("You have been teleported back to TimeWatcher HQ.")
            elif choice6 == "2":
                print("You dash toward the exit.")
                print("You slide under the door before it fully shuts.")
                print("You have saved this era!")
                print("You open your TimeWatcher to select another era:")
                print("1. Wild West")
                choice7 = input("Enter a number: ")
                if choice7 == "1":
                    path3()
                else:
                    print("Invalid choice. Please input valid option.")
            else:
                print("Invalid choice. Please input valid option.")
        elif choice5 == "2":
            print("You follow the right path.")
            print("You trigger a trip wire and fall into a pit.")
            print("You fall onto spikes.")
            print("            ****GAME OVER****                   ")
            print("You have been teleported back to TimeWatcher HQ")
        else:
            print("Invalid choice. Please input valid option.")

    elif choice4 == "2":
        print("You follow the right path.")
        print("You trigger a trip wire and fall into a pit.")
        print("You fall onto spikes.")
        print("            ****GAME OVER****                   ")
        print("You have been teleported back to TimeWatcher HQ")
    else:
        print("Invalid choice. Please input valid option.")



def path1():
    print("You step into the TimeWatcher and arrive in medieval Europe")
    print("You land in the yard of the main castle.")
    print("In the near distance, you see two knights...")
    print("They are both supposed to be protecting the King.")
    print("Instead, they are about to have a deadly duel!")
    print("You hear them yelling over a lost crown.")
    print("Titron set them up against each other.")
    print("Negotiate a truce between them so they can return to the King.")
    print("\nWhat choice will you make?")
    print("1. Use your force/intimidation to break up the duel")
    print("2. Gather evidence to prove their misunderstandings")
    choice2 = input("Enter a number: ")
    if choice2 == "1":
        print("The knights were not intimidated and killed you.")
        print("            ****GAME OVER****                   ")
        print("You have been teleported back to TimeWatcher HQ")
    elif choice2 == "2":
        print("You find the missing crown resting in the bushes.")
        print("You pick it up and hand it back to the Knights")
        print("They end their duel and return to the King's throne.")
        print("You have saved this era!")
        print("You open your TimeWatcher to select another era:")
        print("1. Ancient Egypt")
        print("2. Wild West")
        choice3 = input("Enter a number: ")
        if choice3 == "1":
            path2()
        elif choice3 == "2":
            path3()
        else:
            print("Invalid choice. Please input a valid option.")
    else:
        print("Invalid choice. Please input a valid option.")


def intro():
    print()
    print()
    print(f"{name}, you activate your TimeWatcher.")
    print("This device is the hub that shows all time eras with disruptions.")
    print("\nA holographic interface appears with 3 time periods:"
          "\n1. Medieval times"
          "\n2. Ancient Egypt"
          "\n3. Wild West")
    print("Which era would you like to go to?")
    choice1 = input("\nEnter a number: ")
    if choice1 == "1":
        path1()
    elif choice1 == "2":
        path2()
    elif choice1 == "3":
        path3()
    else:
        print("Invalid choice. Please input valid option.")


print("████████╗██╗███╗   ███╗███████╗██╗    ██╗ █████╗ ████████╗ ██████╗██╗  ██╗███████╗██████╗ ███████╗")
print("╚══██╔══╝██║████╗ ████║██╔════╝██║    ██║██╔══██╗╚══██╔══╝██╔════╝██║  ██║██╔════╝██╔══██╗██╔════╝")
print("   ██║   ██║██╔████╔██║█████╗  ██║ █╗ ██║███████║   ██║   ██║     ███████║█████╗  ██████╔╝███████╗")
print("   ██║   ██║██║╚██╔╝██║██╔══╝  ██║███╗██║██╔══██║   ██║   ██║     ██╔══██║██╔══╝  ██╔══██╗╚════██║")
print("   ██║   ██║██║ ╚═╝ ██║███████╗╚███╔███╔╝██║  ██║   ██║   ╚██████╗██║  ██║███████╗██║  ██║███████║")
print("   ╚═╝   ╚═╝╚═╝     ╚═╝╚══════╝ ╚══╝╚══╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝")
print()
print("Travel through time and stop the villainous, Titron!")
print("Make clever choices and stop the alteration of the present")

while game_loop:

    startGame = input("\nDo you want to start game(yes/no)? ")
    if startGame.lower().strip() == "no":
        print("Sure, maybe someone else will save the world.")

    elif startGame.lower().strip() == "yes":
        name = input("Enter your name: ")
        intro()

    else:
        print("Invalid choice. Please input valid option.")
