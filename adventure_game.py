import random
import time


def global_rules():
    # all definitions for any variable to be used in game
    global yes, no, colors, color, score, health, attack, defense
    global enemies, items, rarities, first_choice, second_choice
    global third_choice, fourth_choice
    # different colors
    colors = ["green", "blue", "red", "yellow",
              "black", "fuchsia", "maroon", "turqouise", "crystal"]
    # different rarites
    rarities = {
        "stone": 5,
        "bronze": 10,
        "silver": 15,
        "platinum": 20,
        "Topaz": 25,
        "Moonstone": 30,
        "sapphire": 35
        }
    # choices to make coding easier
    first_choice = ["a"]
    second_choice = ["b"]
    third_choice = ["c"]
    fourth_choice = ["d"]
    # some items
    items = ["shield", "sword", "soul shard", "key"]
    # yes or no choices to make coding easier
    yes = ["yes", "y"]
    no = ["no", "n"]
    # define player stats
    score = 0
    health = 100
    attack = 25
    defense = 5


# start Creatures
def pixie():
    global health, attack, defense, score
    # gives the player a random buff by using random.choice to choose a stat
    show("amidst the shadows, you encounter a playful pixie.", 1)
    show("its radiant aura captivating. The pixie offers you a gift.")
    show("In this ethereal illumination", 1)
    show("A strange sensation prickles your skin.", 3)
    pixie_buff = random.choice(["health", "attack", "defense"])
    pixie_buff_amount = random.choice([5, 10, 15, 20, 25, 30])
    if pixie_buff == "health":
        health += pixie_buff_amount
        score += 10
        show(f"Your health has increased to {health} now!", 1)
        show(f"Your score is now: {score}", 1)
    elif pixie_buff == "attack":
        attack += pixie_buff_amount
        score += 10
        show(f"Your attack has increased to {attack} now!", 1)
        show(f"Your score is now: {score}", 1)
    elif pixie_buff == "defense":
        defense += pixie_buff_amount
        score += 10
        show(f"Your defence has increased to {defense} now!", 1)
        show(f"Your score is now: {score}", 1)
# End Creatures


# Start Eventg
def chest():
    # Generates a random item with a random rarity to be found in the chest
    global items, attack, defense, health, score
    color = random.choice(colors)
    show(f"Venturing onward you stumble onto a {color} chest", 1)
    show("You attempt to pry the chest open with your bare hands", 1)
    show("The chest opens:", 1)
    item = random.choice(items)
    if item == "sword":
        # chenge the player stats
        rarity = random.choice(list(rarities.keys()))
        rarity_buff = rarities.get(rarity, 0)
        attack += rarity_buff
        score += 15
        show(f"You found a {rarity} sword!", 1)
        if "key" in items:
            show("You have also found a giant ancient key!", 1)
            show("now you can use it to open an ancient door!", 1)
            score += 35
            items.remove("key")
        show(f"Your attack is now: {attack}", 1)
        show(f"Your score is now: {score} +", 1)
    elif item == "shield":
        # chenge the player stats
        rarity = random.choice(list(rarities.keys()))
        rarity_buff = rarities.get(rarity, 0)
        defense += rarity_buff
        score += 15
        show(f"You found a {rarity} shield!", 1)
        if "key" in items:
            show("You have also found a giant ancient key!", 1)
            show("now you can use it to open an ancient door!", 1)
            score += 35
            items.remove("key")
        show(f"Your defense is now: {defense}", 1)
        show(f"Your score is now: {score} +", 1)
    elif item == "soul shard":
        # chenge the player stats
        rarity = random.choice(list(rarities.keys()))
        rarity_buff = rarities.get(rarity, 0)
        health += rarity_buff
        score += 15
        show(f"You found a {rarity} soul shard!", 1)
        if "key" in items:
            show("You have also found a giant ancient key!", 1)
            show("now you can use it to open an ancient door!", 1)
            score += 35
            items.remove("key")
        show(f"Your health is now: {health}", 1)
        show(f"Your score is now: {score} +", 1)


def chest_endless():
    # generates a random item with a random rarity to be found in the chest
    global items, attack, defense, health, score
    color = random.choice(colors)
    show(f"you find a {color} chest", 1)
    show("The chest opens:", 1)
    item = random.choice(items)
    if item == "sword":
        # chenge the player stats
        rarity = random.choice(list(rarities.keys()))
        rarity_buff = rarities.get(rarity, 0)
        attack += rarity_buff
        score += 15
        show(f"You found a {rarity} sword!", 1)
        show(f"Your attack is now: {attack}", 1)
        show(f"Your score is now: {score} +", 1)
    elif item == "shield":
        # chenge the player stats
        rarity = random.choice(list(rarities.keys()))
        rarity_buff = rarities.get(rarity, 0)
        defense += rarity_buff
        score += 15
        show(f"You found a {rarity} shield!", 1)
        show(f"Your defense is now: {defense}", 1)
        show(f"Your score is now: {score} +", 1)
    elif item == "soul shard":
        # chenge the player stats
        rarity = random.choice(list(rarities.keys()))
        rarity_buff = rarities.get(rarity, 0)
        health += rarity_buff
        score += 15
        show(f"You found a {rarity} soul shard!", 1)
        show(f"Your health is now: {health}", 1)
        show(f"Your score is now: {score} +", 1)
# End Events


# Start Mechanics
def fight_monster_endless():
    global health, attack, defense, score
    # define the monster stats for the fights
    monster_stats = [
        {"name": "Goblin", "health": 40, "defense": 10, "attack": 15},
        {"name": "Skeleton", "health": 50, "defense": 15, "attack": 20},
        {"name": "Orc", "health": 60, "defense": 20, "attack": 25},
        {"name": "Troll", "health": 80, "defense": 25, "attack": 30}
    ]
    while True:
        monsters_defeated = 0
        # randomly select a monster from the list
        monster = random.choice(monster_stats)
        monster_name = monster["name"]
        monster_health = monster["health"]
        monster_defense = monster["defense"]
        monster_attack = monster["attack"]
        show("Your stats:")
        show(f"Health: {health}")
        show(f"Defense: {defense}")
        show(f"Attack: {attack}")
        # display monster information
        show(f"A fearsome {monster_name} appears!")
        show(f"{monster_name} stats:")
        show(f"Health: {monster_health}")
        show(f"Defense: {monster_defense}")
        show(f"Attack: {monster_attack}")
        # fight loop until health reaches zero
        while health > 0 and monster_health > 0:
            show("Your turn - Choose an action:")
            show("a - Attack")
            show("b - Run")
            option = input("Enter your choice: ")
            if option.lower() in first_choice:
                # calculate damage
                damage = max(0, attack - monster_defense)
                monster_health -= damage
                show(f"You dealt {damage} damage to the {monster_name}!")
                if monster_health <= 0:
                    show(f"You have defeated the {monster_name}!")
                    monsters_defeated += 1
                    score += 15
                    # check how many monsters were fouaght
                    if monsters_defeated % 3 == 0:
                        pixie()
                    if monsters_defeated % 7 == 0:
                        show("Congratulations! You have earned a chest.")
                        chest_endless()
                    break
            elif option.lower() in second_choice:
                # running away decreases score
                score -= 15
                show("You try to run away but lose 15 points of score!")
                show("The battle is over.")
                show(f"your score is now{score}")
                restart_game()
                break
            else:
                show("Invalid choice! Try again.")
            show(f"The {monster_name} attacks!")
            damage = max(0, monster_attack - defense)
            health -= damage
            show(f"The {monster_name} dealt {damage} damage to you!")
            # check if the player is defeated
            if health <= 0:
                show("You have been defeated!")
                health = 100
                break
        show("The battle is over.")
        show("Do you want to continue fighting? (Y/N)")
        choice = input("Enter your choice: ")
        if choice.lower() in no:
            break
    # End of game
    show("Game over.")
    show(f"Final score: {score}")


def show(text, sleep=1):
    # to display text for a specific amount of time
    time.sleep(sleep)
    print(text)


def start():
    # display the text to start the game
    show("Welcome to ~The Hidden Forest~", 0.2)
    show("Start The Adventure?")


def reset():
    global health, defense, score, attack
    # resets all stats back to their original state
    score = 0
    health = 100
    attack = 10
    defense = 5
    show("Would You Like To Start Again?")
    while True:
        option = input("(y/n):")
        if option.lower() in yes:
            start_game()
        elif option.lower() in no:
            break
        else:
            print("Invalid choice. Please choose again.")


def restart_game():
    # after resetting everything it exits if the player says no
    reset()
    show("Alright then, See Ya Later!", 0.3)
    exit()
# End Mechanics


# Start Story
def intro():
    # intro scene with random colors
    global necklace_color
    color = random.choice(colors)
    necklace_color = random.choice(colors)
    show("beyond the magical kingdom, there was an enchanted forest.", 3)
    show("Many legends spoken of its creatures and hidden valuables.", 3)
    show("Many explorers ventured through it, only a few had returned.", 4)
    show("You were told by your grandparents that it was your destiny.", 3)
    show("to unravel its mysteries and unlock the hidden truth within it.")
    show(f"After being given a {necklace_color} necklace as a gift.", 3)
    show("You finally stand before the ominous enchanted forest", 4)
    show("you start to feel that it has become aware of your prescence.")
    show("You confirm of its awareness, some of the trees merge together", 3)
    show(f"forming what seems to be a {color} door.")
    show("Go through the door?", 4)


def enter_forest():
    # the scene when the player decides to enter the forest
    global score
    score += 15
    show(f"your score is now: {score} + ", 1)
    color = random.choice(colors)
    show("you decide to step through and enter the enchanted forest.", 1)
    show("As you traverse further into the enchanted forest.", 1)
    show("you come across a diverging path.")
    show("One stares into darkness, obscured by an ominous fog.", 3)
    show("but a subtle glimmer pierces through the black void.", 3)
    show(f"The other path is lit by {color} torches", 4)
    show("However, as you step closer, you notice an odd noise in there.", 3)
    show("Both of the paths lie before you. Which path will you choose?", 4)
    show("a - The Dark Path", 1)
    show("b - The Illuminated Path", 1)


def dark_path():
    # this is the endless mode, one of the two choices the player gets
    global score
    score += 15
    show(f"your score is now: {score} +", 1)
    show("As you go through the dark path.", 1)
    show("The subtle shimmer at the end of the path increases.", 4)
    show("a sight of mystical beings are dancing beyond your vision.")
    show("unsettling whispers in the air, beckoning you into the darkness.", 4)
    pixie()
    show("With a sly smile, the pixie fades into the void.", 1)
    show("The dark path continues deeper into the enchanted forest.", 3)
    show("You are entering endless mode:")
    fight_monster_endless()


def questions():
    # the scene where the player will ask their questions to the guards
    global score
    show("Suddenly, a surge of power courses through the room.", 3)
    show("and the switch activates. In an instant.")
    show("the once-dark room becomes a display of colorful torches.")
    show("The vibrant hues illuminate the space.", 4)
    show("revealing the breathtaking sight, hidden in the darkness.")
    show("you see two colossal statues standing at the river.", 1)
    show("Carved with great detail, the guardians awaken.")
    show("they don't seem too harmful, but their looming prescence", 3)
    show("strikes you with a sense of uncomfort.")
    show("You have the choice:", 1)
    show("a - Examine the writings first.")
    show("b - Approach the ancient statues.")
    # invalid input handling
    while True:
        option = input("(a/b):")
        if option.lower() in first_choice:
            score += 10
            show(f"your score is now: {score} +", 1)
            examine_writings()
            pass
        elif option.lower() in second_choice:
            score += 5
            show(f"your score is now: {score} +", 1)
            pass
        else:
            print("Invalid choice. Please choose again.")
            continue
        ancient_statues()
        show("What would you like to ask the ancient statues?", 3)
        show("a - ask about the Enchanted Forest.", 1)
        show("b - ask about the purpose of the statues.", 1)
        while True:
            option = input("(a/b):")
            if option.lower() in first_choice:
                score += 15
                show(f"your score is now: {score} +", 1)
                forest_origins()
                show("The Statues: What more knowledge do you seek?:", 3)
                show("a - ask about the purpose of the statues.", 1)
                while True:
                    option = input("(a):")
                    if option.lower() in first_choice:
                        ancient_purpose()
                        show("What would you like to do?", 3)
                        show("a - go to The heart of the forest", 1)
                        show("b - go to The treasure room", 1)
                        while True:
                            option = input("(a/b):")
                            if option.lower() in first_choice:
                                forest_heart()
                                break
                            elif option.lower() in second_choice:
                                treasure_room()
                                break
                            else:
                                print("Invalid choice. Please choose again.")
                                continue
                        break
            elif option.lower() in second_choice:
                score += 15
                show(f"your score is now: {score} +", 1)
                ancient_purpose()
                show("What would you like to do?", 3)
                show("a - go to The heart of the forest.", 1)
                show("b - go to The treasure room.", 1)
                show("c - ask about the Enchanted Forest.", 1)
                while True:
                    option = input("(a/b/c):")
                    if option.lower() in first_choice:
                        forest_heart()
                        break
                    elif option.lower() in second_choice:
                        treasure_room()
                        break
                    elif option.lower() in third_choice:
                        forest_origins()
                        show("The Statues: What more knowledge do you seek?:")
                        show("a - go to the heart of the forest.", 1)
                        show("b - go to the treasure room.")
                        while True:
                            option = input("(a/b):")
                            if option.lower() in first_choice:
                                forest_heart()
                                break
                            elif option.lower() in second_choice:
                                treasure_room()
                                break
                            else:
                                print("Invalid choice. Please choose again.")
                                continue
                            break
                    else:
                        print("Invalid choice. Please choose again.")
                        continue
                    break
            else:
                print("Invalid choice. Please choose again.")
                continue


def lit_path():
    # the story mode,where the player can know more about the story of the game
    global score
    score += 15
    show(f"your score is now: {score} + ", 1)
    show("you tread confidently through the torch-lit trail.", 1)
    show("despite the peculiar noises that fill the air.")
    show("the torches cast their dancing glow upon the ancient trees.", 1)
    show("revealing branches and shadows that whisper in the forest.", 1)
    show("The path ahead is illuminated, deeper into the mystical realm.", 3)
    show("you keep walking till the end of the path.", 3)
    show("you notice the torchlight getting weaker the further you tread.")
    show("Finally, you step into a vast, dark room.", 3)
    show("The torches lining the path completely fade.")
    show("leaving you in near-total darkness.")
    show("The darkness within the room is impenetrable.", 3)
    show("obscuring any shapes or objects that may lie within.")
    show("you make out something in within, doesn't seem to be moving.", 3)
    show("approach it?", 3)
    # invalid input handling (same with every while loop used)
    while True:
        option = input("(y/n):")
        if option.lower() in yes:
            score += 15
            show(f"your score is now: {score} +", 1)
            show("You go into the darkness to see what could be in it.", 1)
            chest()
            show("opening the chest caused a disturbance in the room.", 1)
            show("some fruits fall from the trees above you.", 3)
            show("one of them lands on a switch nearby and you hear a click.")
            show("its accompanied by strange writings on the wall.", 1)
            questions()
            break
        elif option.lower() in no:
            show("you decide it's risky to approach the mysterious object", 1)
            show("Your eyes catch a faint glimmer on the wall nearby.", 1)
            show("As you move closer, you see that it's a switch.", 1)
            show("flicking it might do something.")
            show("The switch is accompanied by writings on the wall.", 1)
            show("It's up to you to decide what to do next:", 1)
            show("a - Examine the writings first.", 1)
            show("b - Flip The Switch", 1)
            while True:
                option = input("(a/b):")
                if option.lower() in first_choice:
                    examine_writings()
                    pass
                elif option.lower() in second_choice:
                    pass
                else:
                    print("Invalid choice. Please choose again.")
                    continue
                show("You decide to flip the switch and see what happens", 1)
                questions()
                break
            break
        else:
            print("Invalid choice. Please choose again.")
            continue


def examine_writings():
    # scene where the player reads some writings they found
    show("You decide to examine the writings on the wall.", 1)
    show("They seem to be reciting some sort of poetry:", 1)
    show("The path through shadows leads to truth,", 1)
    show("In whispers of trees, secrets take root.", 1)
    show("Beneath the boughs, mysteries unfold,", 1)
    show("Seek the heart, where destiny is foretold.", 1)
    show("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", 1)
    show("Beware the temptations that riches may bring,", 1)
    show("For treasures can ensnare, a siren's sting.", 1)
    show("Choose wisely, adventurer, heed the call,", 1)
    show("In the hidden forest, destinies befall.", 1)
    show("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", 1)
    show("To the heart or the vault, paths diverge,", 1)
    show("One leads to answers, the other to urge.", 1)
    show("Decide your fate with wisdom profound,", 1)
    show("Unlock the mysteries, let truths resound.", 1)
    show("You're unsure of what these words could be linked to.", 5)
    show("But you venture owards and continue your Journey.", 1)


def ancient_statues():
    # scene where the player confronts the statues
    show("You approach the statues, their presence looming over you.", 1)
    show("The statues emanate an aura, as if holding ancient knowledge.", 1)
    show("You gather your courage and decide to speak.", 3)
    show("hoping to unveil the mysteries.")


def forest_origins():
    # scene where the statues explain the origins of the forest
    show("You ask the statues about the origins of the Enchanted Forest.", 1)
    show("The statues begin to speak in a calm and resonant manner.", 1)
    show("Ancient Statue: The Enchanted Forest was once a kingdom.", 3)
    show("Ancient Statue: ruled by a great king named Koshi.")
    show("Ancient Statue: King Koshi was a man of honor.", 3)
    show("Ancient Statue: believed in peace to achieve prosperity.")
    show("Ancient Statue: his beliefs were to be tested by humans.", 3)
    show("Ancient Statue: as they set thier plans to harness its power.")
    show("Ancient Statue: King Koshi prepared his brave soldiers.", 4)
    show("Ancient Statue: the battle between us, And the Humans.")
    show("Ancient Statue: Although the King's strength was great.", 3)
    show("Ancient Statue: the Humans' thirst for power wes too strong.")
    show("Ancient Statue: The Humans stole the magic pendant.", 3)
    show("Ancient Statue: that powers the heart of the Enchanted Kingdom.")
    show("Ancient Statue: Leaving its lifeless remains to waste away.")
    show("Ancient Statue: The King was overloaded with sadness and dispair.")
    show("Ancient Statue: channeling his anger through nature.")
    show("Ancient Statue: Without the pendant to power the forest again.")
    show("Ancient Statue: we fear there might not be hope for this Kingdom.")


def ancient_purpose():
    # scene where the statues explain why they are standing at the door
    show("You inquire about the purpose of the statues.", 1)
    show("The statues' voices intertwine, recounting their purpose.", 1)
    show("The Statues: Our purpose to guard the ancient door of the Kingdom.")
    show("The Statues: you must have the ancient key to open the door.", 3)
    show("The Statues: The door leads to the place mostly desired by you.", 1)
    show("The Statues: Wait what??? You found the key already??", 1)
    show("The Statues: Well this is awkward, go open the door then.", 3)
    show("The statues step aside to fully reveal a giant ancient door.", 4)
    show("The key fits into the door, it reveals a massive portal inside.", 3)


def forest_heart():
    # scene where the player goes into the heart of the forest and gets rewards
    global score
    # random color
    color = random.choice(colors)
    show("determined, you go on the journey to the heart of the forest.", 1)
    show("The statues' enchanting chant blesses you, strengthning you.", 3)
    show("A portal materializes, pulsating with the heart of the forest.", 3)
    show("you step forward into the beckoning depths of the portal.", 3)
    show("The statues' chant fades, and the portal fully opens.", 3)
    show("With their final blessing, you step through the portal", 4)
    show("The Heart Of The forest senses your arrival.", 4)
    pixie()
    show("As you venture further, the heart of the forest unfolds.", 3)
    show("The room emanates abundance, darkness, and a hint of emptiness.", 3)
    chest()
    show("In the center, a giant waterfall cascades before a stone wall.", 1)
    show(f"it's where the original {necklace_color} necklace was stolen.")
    show("you have the choice:")
    show("a - return stolen necklace")
    show("b - keep the necklace")
    # invalid input handling
    while True:
        option = input("(a/b):")
        if option.lower() in first_choice:
            show("you attempt to put the necklace back into the stone")
            if score >= 115:
                # if the player score exceeds a certain amount they win or lose
                show("Your score is above 150!")
                show("the stone shines bright")
                show("and the kingdom arises once again")
                show("the king is very grateful")
                show("and gifts you with some treasures")
                show("you win!!")
                restart_game()
                break
            else:
                show("Your score is less than 150")
                show("you lose")
                restart_game()
                break
            break
        elif option.lower():
            # alternate ending with same logic as before
            show("you decide to keep the necklace")
            show("king koshi awakes")
            show("he fights you to retrieve the necklace")
            if score >= 150:
                show("you defeat king koshi and you rule the kingdom")
                show("you win!")
                restart_game()
                break
            else:
                show("king koshi defeats you")
                show("he imprisons you for the rest of eternity")
                show("you lose!")
                restart_game()
                break
            break
        else:
            print("Invalid choice. Please choose again.")
            continue


def treasure_room():
    # ending where the player loses the game for choosing wrong
    show("With ambition in your eyes, you decide to pursue the path.", 3)
    show("the path that leads to the forest's treasure room.")
    show("As you make your choice, sadness is on the ancient statues' faces.")
    show("Resolute in your decision, you watch the statues chant once again.")
    show("their voices filled with a mix of resignation and duty.")
    show("the portal to the treasure room begins to appear before you.", 4)
    show("Your heart races with anticipation as the portal fully forms.", 3)
    show("revealing a room with gleaming jewels and chests with treasures.")
    show("you step through the portal and enter the treasure room.", 3)
    show("the scent of opulence filling your senses.")
    show("You revel in the riches surrounding you.", 3)
    show("your hands reaching for the treasures that lie within your grasp.")
    show("you bask in the glory of your wealth, a realization dawns upon you")
    show("The portal that brought you here, your only means of escape.", 1)
    show("has silently closed behind you.")
    show("Panic emerges, its icy grip tightening around your heart.", 1)
    show("You find yourself alone in there, its transformed into a prison.")
    show("In the eerie silence, you stand as a solitary figure.", 3)
    show("surrounded by countless treasures, yet trapped.")
    show("The ancient statues' chants fade into the distance.", 3)
    show("their warnings echoing through your mind.")
    show("You are left to face the consequences of your choice.", 1)
    show("with no one to save you from the depths of your own greed.")
    show("~~~~~The End~~~~~", 3)
    show("You lost all your score.", 4)
    show("You lose.", 1)
    restart_game()


def leave():
    # scene where player doesn't decide to play
    show("You decide that the forest was too dangerous for you to enter.", 1)
    show("You go back home and enjoy the rest of your life.", 3)
    show("without ever setting foot into that forest, ever again.")
    show("~~~~~The End~~~~~", 5)
    show(f"Your score: {score}", 1)
    restart_game()
# End Story


# Start Game
def start_game():
    # main game loop
    global_rules()
    # set the definitions from earlier
    start()
    # start scene
    while True:
        # invalid input handling
        option = input("(y/n): ")
        if option.lower() in yes:
            show("Great! let me set up the scene for you:", 0.3)
            intro()
            while True:
                option = input("(y/n):")
                if option.lower() in yes:
                    enter_forest()
                    # player gets the main two game modes
                    while True:
                        option = input("(a/b):")
                        if option.lower() in first_choice:
                            dark_path()
                            break
                        elif option.lower() in second_choice:
                            lit_path()
                            break
                        else:
                            print("Invalid choice. Please choose again.")
                            continue
                    break
                elif option.lower() in no:
                    leave()
                else:
                    print("Invalid choice. Please choose again.")
                    continue
                break
        elif option.lower() in no:
            show("Alright then, See Ya Later!", 0.3)
            break
        else:
            print("Invalid choice. Please choose again.")
            continue


start_game()
# End Game
