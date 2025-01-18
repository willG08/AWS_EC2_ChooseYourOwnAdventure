# Name: Will Gunther
# Date: 1/9/2025
# Project Description: Choose your own adventure with at least 10 decisions and 20 outcomes

class Player:
    def __init__(self):
        self.name = "Greg"
        self.difficulty = "Beg"
        self.lives = 1
        self.next_scene = "Intro"

    def takeDamage(self):
        self.lives -= 1
        if self.lives < 1:
            print(f"You hear a voice say, 'You ran out of lives' :( \n Game Over \n Better Luck Next Time!")
            try_again()
        else:
            print(f"You hear a voice say, 'INCORRECT CHOICE, you have {self.lives} lives left, be careful!'")
    
    def finish(self):
        successfulDifficulty = ""
        if self.difficulty == "Beg":
            successfulDifficulty = "Beginner"
        elif self.difficulty == "Int":
            successfulDifficulty = "Intermediate"
        elif self.difficulty == "Adv":
            successfulDifficulty = "Advanced"
        elif self.difficulty == "Nig":
            successfulDifficulty = "Nightmare"
        else:
            successfulDifficulty = "Impossible"
        
        print(f"You begin to see your body disintegrate and fly upwards. You see your hands, clothes, and shoes on your body! You cannot be more thrilled to be back! You're startled by the loudness as you hear the game say High Score! Enter your initials! You know that voice will forever haunt you but you will remember to focus on what matters most.", 
              f"You completed {successfulDifficulty} mode with {self.lives} lives remaining! Congratulations!")
        try_again()

class Scene:
    def __init__(self, name, description, choices):
        self.name = name
        self.description = description
        self.choices = choices  # Dictionary with choice descriptions as keys and next scenes as values
    
    def display(self):
        print(self.description)
        for idx, (option, next_scene) in enumerate(self.choices.items(), 1):
            print(f"{idx}) {option}")
        return list(self.choices.values())
    
    def displayDescription(self):
        print(self.description)

def try_again():
    choice = input("Would you like to try again? (yes/no): ").strip().lower()
    if choice == "yes":
        print(f"Restarting the game...\n")
        # Restart the game by calling the main function
        main()  
    else:
        print("Thanks for playing!")
        # Exit the program if they choose not to try again
        exit()  

def start_adventure():
    #Get player's name
    player = Player()
    player.name = input("What's your name? ")

    print(f"\nWelcome to Echoes of Time, {player.name}!\n")

    Intro.displayDescription()

    input(f"\nPress any button to continue")

    #Introduction
    for difficulty, description in Difficulties.items():
        print(difficulty, f"\n", description)

    choice = input("Enter your choice (0-5): ")
    while True:
        if choice == '0':
            with open('adventure_outcomes.txt', 'r') as input_file:
                #Process each line in file
                for line in input_file:
                    print(line)
            try_again()
        if choice == '1':
            player.difficulty = "Beg"
            player.lives = 5
            player.next_scene = "StartBeg"
            print("As soon as you select start you slowly begin to see you're hands disintegrate, then you're arms, followed by your body as it sucked in the arcade game. You hear a loud voice proclaim, 'You have 5 lives, defend the mountain, FIGHT!'")
            break
        elif choice == '2':
            player.difficulty = "Int"
            player.lives = 4
            player.next_scene = "StartInt"
            print("As soon as you select start you slowly begin to see you're hands disintegrate, then you're arms, followed by your body as it sucked in the arcade game. You hear a loud voice proclaim, 'You have 4 lives, defend the mountain, FIGHT!'")
            break
        elif choice == '3':
            player.difficulty = "Adv"
            player.lives = 3
            player.next_scene = "StartAdv"
            print("As soon as you select start you slowly begin to see you're hands disintegrate, then you're arms, followed by your body as it sucked in the arcade game. You hear a loud voice proclaim, 'You have 3 lives, defend the mountain, FIGHT!'")
            break
        elif choice == '4':
            player.difficulty = "Nig" 
            player.lives = 2
            player.next_scene = "StartNig"
            print("As soon as you select start you slowly begin to see you're hands disintegrate, then you're arms, followed by your body as it sucked in the arcade game. You hear a loud voice proclaim, 'You have 2 lives, defend the mountain, FIGHT!'")
            break
        elif choice == '5':
            player.difficulty = "Imp" 
            player.lives = 1
            player.next_scene = "StartImp"
            print("As soon as you select start you slowly begin to see you're hands disintegrate, then you're arms, followed by your body as it sucked in the arcade game. You hear a loud voice proclaim, 'You have 1 life, defend the mountain, FIGHT!'")
            break
        else:
            print("Invalid choice!")
            choice = input("Enter your choice (1-5): ")
    return player


#List all scenes
Intro = Scene("Intro",
"Bored one day you decide to visit the arcade. You find that most of the games are out of order or aren't worth your time. However, you find a string of 5 games that seem pretty cool.", None)

# Dictionary Storing Difficulty, Game titles, and Description minimum of 1 decision point
Difficulties = {f"\n0. Read Outcomes \n1. Beginner: X \n Journey Through Time: First Steps": "A gentle introduction to time travel, perfect for beginners finding their way through the ages.", f"\n2. Intermediate: XX \n Journey Through Time: Rising Tides":"A balanced adventure where the stakes are higher, and every decision matters.", f"\n3. Advanced: XXX \n Journey Through Time: The Shifting Sands" : "A complex and challenging odyssey requiring skill and strategy to navigate the perils of time.", f"\n4. Nightmare: XXXX \n Journey Through Time: Echoes of Chaos": "A relentless test where time itself fights against you. Only the strong survive.", f"\n5. Impossible: XXXXX \n Journey Through Time: The Final Paradox": "The ultimate challenge. The fate of the universe is at stake, and only the most determined can restore balance."}




################Beginner's Scenes
## Cavemen minimum of 3 decision points
StartBeg = Scene("StartBeg", "You are standing at the top of a mountain! You see a small family hiding a cave behind you. You are dressed in nothing more than a piece of cloth draped over your shoulder and a large club in your hand. You immediately see a large cavemen screaming as he runs towards you swinging his club. What will you do?",
                  {f"Dodge": "Damage", f"Attack": "DamageCaveman", f"Run": "Damage"})

DamageCaveman = Scene("DamageCaveman", "You successfully damaged the caveman and he disappeared! You're confused but more scared for your life than anything. There's more enemies coming at you! What will you do?",
                       {"Keep fighting": "StartBegVictory", "Escape": "Damage", "Look for another weapon": "OtherWeaponBeg"})

OtherWeaponBeg = Scene("OtherWeaponBeg", "You find a long sharp stick you can use to damage the enemy from afar! The cavemen are nearly upon you! What will you do?",
                       {f"Dodge": "Damage", f"Attack": "StartBegVictory", f"Run": "Damage"})

StartBegVictory = Scene("StartBegVictory", "The Cavemen have been defeated! You fought with some other worldly strength. What will you do?",
                        {"Celebrate":"GreekBeg", "Drop your weapons and check on the family":"GreekBeg"})

##Greek Era minimum of 3 decision points
GreekBeg = Scene("GreekBeg", "You close your eyes briefly and you hear a voice saying, 'Commander, we are surrounded on all sides what should we do?' You notice you are covered head to toe in armor with a sword on your hip. You are stationed at the top of a mountain with seemingly no means of escape. What will you do?", 
                 {"Prepare the archers at each corner of our fortress with the majority covering the entrances.": "GreekArchers", "Surrender": "Damage", "Escape through the less guarded side of the fortress and fight our way out!": "GreekEscape"})

GreekArchers = Scene("GreekArchers", "Your men are in position to defend the fortress, it is an amazing battle and you are holding them off well. However, your arrows won't last forever. What will you do?", 
                     {"Send all available soldiers and some of the archers out to start fighting with swords.":"GreekEscape", "Continue firing arrows":"Damage", "Move all archers to the main entrance":"Damage"})

GreekEscape = Scene("GreekEscape", "You are battling every inch, trying to get through this army to freedom! There seems to be no end in sight of these enemy soldiers. What will you do?", 
                    {"Fight On!": "Damage", "Tell your men to retreat to the fortress": "GreekRetreat"})

GreekRetreat = Scene("GreekRetreat", "Your men retreated, the remaining archers at the fortress damaged the enemy as the infantry made it back to the fortress.", 
                     {"Circle your infantry around the backside and pinch the enemy": "GreekVictory", "Hold the fortress with everything we can":"Damage"})

GreekVictory = Scene("GreekVictory", "They had nowhere to go. Victory is yours!", 
                     {"Press 1 to continue": "DragonsBegin"})

##Dragons Era minimum of 5 decision points
DragonsBegin = Scene("DragonsBegin", "You open your eyes to see you are now in a new world. You are on top of a majestic castle, covered head to toe in a metallic armor you don't recognize. You walk in to discover a meeting beginning. 'Since our worlds have merged the Orcs have began to take over but we need to stop them.' Everyone shouts in agreement and begin introductions, 'I am Ragnarik, leader of the mountain trolls and we will fight!' 'I am Bargon, leader of the dwarves and we will fight!' 'I am Serasee, leader of the elves and we will fight!' 'I am Harvin the wizard, protector of all and I will fight!' You are then asked, 'Who are you?'",
                      {"I am Talithan, leader of the humans and we will fight!":"DragonsLeader", "I am Talithan, lead commander of Dragon Defense":"DragonsCommander", "I am Talithan, the janitor":"DragonsJanitor"})

DragonsCommander = Scene("DragonsCommander", "You liar, I'm in charge of the dragon defense team.Who are you?", 
                         {"I am Talithan, leader of the humans and we will fight!":"DragonsLeader", "I am Talithan, lead commander of Dragon Defense":"Damage", "I am Talithan, the janitor":"DragonsJanitor"})

DragonsJanitor = Scene("DragonsJanitor", "You are told to immediately leave the room. What will you do?",
                       {"Demand you haven't finished cleaning the sinks in this room":"DragonsSinks", "Leave the room with the door open a crack and listen in on the meeting": "DragonsSpy"})

DragonsSpy = Scene("DragonsSpy", "You walk out of the door but leave it cracked open so you can overhear. Harvin the wizard says, 'We need to act swiftly and discreetly if we want to eliminate this Orc problem once and for all. We need someone to sneak behind enemy lines and take out their leader Lighten.'",
                     {"You stomp back into the room and demand that you cannot stand idly by and that you want to be a part of this elite team.": "DragonsEliteTeam"})

DragonsSinks = Scene("DragonsSinks", "They allow you stay to clean but they do not have the time to wait for you to leave to continue the meeting. Harvin the wizard says, 'We need to act swiftly and discreetly if we want to eliminate this Orc problem once and for all. We need someone to sneak behind enemy lines and take out their leader Lighten.'",
                     {"You demand that you cannot stand idly by and that you want to be a part of this elite team.": "DragonsEliteTeam"})

DragonsEliteTeam = Scene("DragonsEliteTeam", "Your enthusiasm was meant to be a bad joke to get you out of the room but before you know it you are sneaking behind enemy lines with the bravest souls in all the land. You still have no clue why you were asked to come along but you soon reached the outer wall under the cover of night. Orcs are nocturnal so this won't be easy. You all sneak over a side wall to the fortress and take out some enemy guards without being detected. You now realize why you were recruited, you are the only one that is tall enough to pass themselves off as an orc. You need to disguise yourself in the orc's clothing, visit Lighten's lair and take him out. What will you do?",
                         {"Use a back window as a means of entrance with a dagger": "DragonsAssassin","Run away screaming in fear":"DragonsAssassinFear"})

##Outcome Beg 1
DragonsAssassin = Scene("DragonsAssassin", "You are boosted up the side wall and sneak your way through the building. You are narrowly spotted but the guards are called off by something else. You arrive at Lighten's Lair to find he is in a room filled with orcs. At that same moment you hear Orcs yelling and screaming everywhere and figure out that your allies have started multiple fires as a diversion. You quickly hide and all the orcs run to the burning buildings while Lighten stays behind alone. You sneak in and take him out without a sound. It takes you all night to sneak your way out of the city but by morning you are a hero. The orcs are mindless without a leader and their threat is now nonexistent. Good has overcome evil!",
                        {"Press 1 to continue":"Finish"})

##Outcome Beg 2
DragonsAssassinFear = Scene("DragonsAssassinFear", "You are soon spotted by an orc on watch. He shoots you with an arrow and you die three days later. Your elite team was immediately discovered and imprisoned for the rest of their lives. The trolls, dwarves, elves, wizards, and humans lived out terrible lives under the reign of Lighten",
                            {"Press 1 to continue": "Death"})

DragonsLeader = Scene("DragonsLeader", "Talithan, we know you have the most fearless dragons in all the land. We need your best dragon riders to assemble.",
                      {"Assemble the dragon riders":"DragonsAssemble", "Instead, form an elite team to assassinate Lighten once and for all with me in charge": "DragonsEliteTeam"})
                      
DragonsAssemble = Scene("DragonsAssemble", "We need dragons to fly over Lighten's fortress and drop barrels of gunpowder on the enemy then light them on fire, destroying their city. What will you do once the fires have been lit?",
                      {"Hold a siege over their fortress until they surrender or fight": "DragonsSiege", "Send a barrage of arrows over the city walls, followed by an army of infantry storming the city gates.":"DragonsBruteForce"})

DragonsSiege = Scene("DragonsSiege", "You wait in silence outside their gates with an army for days on end, for the perfect opportunity to strike at their fortress. What will you do?",
                     {"Send arrows over the city walls and attack after 3 days":"Damage","Send arrows over the city walls and attack after 10 days":"DragonsBruteForce", "Send arrows over the city walls and attack after 20 days":"Damage"})

DragonsBruteForce = Scene("DragonsBruteForce", "The arrows were unsuspected and injured a large amount of the orcs. Your infantry run in attacking the city.",
                          {"Go after Lighten yourself to his tower":"DragonsLighten", "Fight with the infantry pushing towards Lighten's tower":"DragonsInfantryPush"})

DragonsLighten = Scene("DragonsLighten", "You chase after Lighten yourself circling around the fortress and entering on a different side. Just as you enter Lighten to see he isn't there you look out the window. Lighten is escaping on a horse. You have no time to think. What will you do?",
                       {"Look in the stable for another horse":"DragonsHorse", "Hurry back to find a dragon hunt down Lighten yourself":"DragonsSearch"})                   

##Outcome Beg 3
DragonsHorse = Scene("DragonsHorse","When you finally returned with a horse, it was too late, Lighten was gone. The battlefield was eerily quiet, the orc army reduced to ashes and ruin. For now, the danger has been averted, and peace has been restored. The remaining orc forces were swiftly dealt with, their threat extinguished with precision and force. Yet, something strange occurred. Some of the orc armies seemed to vanish without a trace. Their whereabouts remain a mystery, and no one knows where they went or what became of them. But we are fearful the orc armies are growing stronger each day.",
                            {"Press 1 to continue":"Finish"})
##Outcome Beg 4
DragonsInfantryPush = Scene("DragonsInfantryPush","When you got to Lighten's lair he was gone. The orc army has been destroyed and the threat is neutralized ... for now. The rest of the orc hordes were taken care of swiftly and efficiently. The forces of good have succeeded for a while. I wonder how things would have turned out if we did something different, oh well.",
                            {"Press 1 to continue":"Finish"})

##Outcome Beg 5
DragonsSearch= Scene("DragonsSearch", "By the time you made it back to fortress you all but lost hope when you noticed some men running in the same direction you saw Lighten go. Once you land they tell you they found the horse's tracks. You quickly fly ahead looking for anything you can see. You notice that once the river is crossed the clearing turns into a heavily wooded forest. You spot in the corner of your eye some movement, you fly closer. You discover a horse riding away from small hill without a rider. You quickly land at that hill and face Lighten himself. It is the most epic battle ever told. But in the end it was inevitable. Good conquered evil. Yay!",
                    {"Press 1 to continue":"Finish"})





###############Intermediate's Scenes
##Jungle era minimum of 3 decision points
StartInt = Scene("StartInt", "You are standing in the middle of the jungle! You see a small family hiding behind you. You are dressed in nothing more than a piece of cloth draped over your shoulder and a large club in your hand. You immediately see a large Beetle shrieking as it flies towards you opening its pincers. What will you do?",
                 {f"Dodge": "Damage", f"Attack": "DamageBeetle", f"Run": "Damage"})

DamageBeetle = Scene("DamageBeetle", "You successfully damaged the Beetle and he disappeared! You're confused but more scared for your life than anything. There's more enemies coming at you! What will you do?", 
                     {"Keep fighting": "StartIntVictory", "Escape": "Damage", "Look for another weapon": "OtherWeaponInt"})

OtherWeaponInt = Scene("OtherWeaponInt", "As you search you look under every rock, next to tree, and in every hole.",
                       {"You find a sling to hurl rocks and fight with it": "Damage", "You find a long sharp stick and fight with it":"StartIntVictory", "You find a large sharp rock and fight with it.": "Damage"})

StartIntVictory = Scene("StartIntVictory", "The Beetles have been defeated! You fought with some other worldly strength. What will you do?",
                        {"Celebrate":"Damage", "Drop your weapons and check on the family":"EgyptianInt"})

##Egyptian Era minimum of 4 decision points
EgyptianInt = Scene("EgyptianInt", "You close your eyes briefly and the darkness all around you disappears as the light from your torch illuminates the room to display a tan stone hallway. You see a large pit at least 10 feet long with no bottom in sight. You hear a friendly telling you to hurry up from another room on the other side of the pit. It sounds like their voice is leaving you behind. What will you do?", 
                    {"Lower yourself into the pit to check the depth": "Damage", "Look around":"EgyptianWhipInt", "Jump across the pit":"Damage"})

EgyptianWhipInt = Scene("EgyptianWhipInt", "You look around and find a whip, a pair of gloves, and an old wood plank. What will you do?",
                        {"Try to Indian Jones your away across the pit with the branch above the pit":"EgyptianVictoryInt", "Place the plank over the pit and walk across":"EgyptianPlank"})

EgyptianPlank = Scene("EgyptianPlank", "As you take your second step on the plank it begins to creak underneath you. What will you do?",
                      {"Retreat and try the whip":"EgyptianVictoryInt", "Jump across the pit":"Damage", "Get on your hands and knees and scoot across the plank":"Damage"})

EgyptianVictoryInt = Scene("EgyptianVictoryInt", "You have no idea how you did it but you earned your real life Indiana Jones accomplishment, you that branch with your whip magically tying it up, swung across, landed safely, and flicked your whip magically releasing it. You reunite with your partner. You discover a room full of mummies. What will you do?", 
                           {"Will you open up mummy number 1": "EgyptianCorrectMummy", "Will you open up mummy number 2": "Damage", "Will you open up mummy number 3": "Damage", "Leave the mummies and run like a bat out of heck out of there": "Damage"})

EgyptianCorrectMummy = Scene("EgyptianCorrectMummy", "As you open up the mummy you discover a strange looking artifact in the mummy's hands. Your partner is relieved to know you found the heart of the pyramid. Great job!", 
                             {"Keep the heart of the pyramid for yourself and sprint out of there":"Damage", "Return as a team with the heart of the pyramid in hand": "EgyptianVictory"})

EgyptianVictory = Scene("EgyptianVictory","You both return in glory with heart of the pyramid in hand", 
                        {"Press 1 to continue": "FutureCity"})

#Future Era minimum of 3 decision points
FutureCity = Scene("FutureCity", "You open your eyes to an amazing view of a city built so high most buildings are taller than the clouds.There are flying cars zipping by you in every direction. Someone is pointing to something on a hologram that you can't quite decipher. What will you say?", 
                   {"What is that?":"FutureCityAI", "What's the plan?":"FutureCityPlan"})

FutureCityAI = Scene("FutureCityAI", "It is Earth's AI overlord. It is worshipped as a God. We are victim to its demands. We need to break free.", 
                     {"Press 1 to continue":"FutureCityPlan"})

FutureCityPlan = Scene("FutureCityPlan", "You hear someone say, 'We are out of time. We need to act quick. You are our best agent, the world lies in your hands. If we do not take over Artificial Intelligence by midnight freedom as we know it will be gone for everyone within the reach of these monsters.' You are given these options:", 
                       {"Nuke the city": "FutureCityNuke", "Sneak in the roof of the AI headquarters, and destroy the mainframe": "FutureCityRoofPlan", "Sneak in the sewer of the AI headquarters, and destroy the mainframe":"FutureCitySewer"})
##Outcome Scene Int 1
FutureCityNuke = Scene("FutureCityNuke", "You nuke the AI capital of the world. The AI overlord has been destroyed. 3/4 of the population of the world dies and 3/4 of the land on Earth will be uninhabitable for at least 20 years. The sorrow and grief of your people will never be forgotten, but the human race will live on!", 
                       {"Press 1 to Continue":"Finish"})


FutureCityRoofPlan = Scene("FutureCityRoofPlan", "You're dropped from a flying car 1000 feet above the building. You parachute and land quietly on the building. You have a gun and your hacking equipment. You break your way into the mainframe. Just as you are about to upload the virus to corrupt the AI overlord, you are shot in the back and your life begins to slip out of your hands. What will you do?", 
                           {"Shoot back at the robots":"FutureCityDeath", "Continue uploading the virus":"FutureCityUploadedVirus"})

##Outcome Scene Int 2
FutureCityDeath = Scene("FutureCityDeath", "You hit 1, 2, 3 robots holding them off. You're in so much pain but you continue to turn around to upload the virus. You hear a gunshot and you fall lifelessly to the ground. As darkness surrounds you, a chilling silence falls, broken only by a distant, echoing voice.",
                        {"Press 1 to continue": "Death"})

FutureCityUploadedVirus = Scene("FutureCityUploadedVirus", "You turned and pushed execute on the virus just as you hear a gunshot. You can't help but fall to the ground. Unaware of what happened.", 
                                {"Press 1 to continue": "FutureCityVirusSuccess"})

##Outcome Scene Int 3
FutureCityVirusSuccess = Scene ("FutureCityVirusSuccess", "You slowly open your eyes to see darkness all around you. There are words slowly falling downwards before your eyes. They say, 'You sacrificed yourself to save mankind. The virus uploaded and began to eat away at the AI overlord. Your allies were able to shut down the power to the city, to ensure AI could never return. The human race still thrives to this day in a simpler, unplugged life. Everyone will keep you in their memory, for your bravery and their gratitude.'",
                                {"Press 1 to continue":"Finish"})

FutureCitySewer = Scene("FutureCitySewer", "You pop open the hatch and begin lowering yourself into the sewer. You begin walking forward barely being able to see. You know if you go back for a flashlight you might not have enough time", 
                        {"Return for a flashlight":"FutureCityReturn", "Press forward, you know you are close": "FutureCitySewerDeath"})

FutureCityReturn = Scene("FutureCityReturn", "You return to your team for a flashlight and reweigh your decisions before continuing.",
                         {"Nuke the city": "FutureCityNuke", "Sneak in the roof of the AI headquarters, and destroy the mainframe": "FutureCityRoofPlan", "Sneak in the sewer of the AI headquarters, and destroy the mainframe":"FutureCitySewerFlashlight"})

FutureCitySewerFlashlight = Scene("FutureCitySewerFlashlight", "You get further than last time in the tunnel before your flashlight runs out of batteries. What will you do?",
                                  {"Press forward, you know you are close": "FutureCitySewerDeath", "Return to find a new plan": "FutureCitySewerReturn"})

FutureCitySewerReturn = Scene("FutureCitySewerReturn", "You reweigh your decisions as a team.",
                         {"Nuke the city": "FutureCityNuke", "Sneak in the roof of the AI headquarters, and destroy the mainframe": "FutureCityRoofPlan"})

##Outcome Scene Int 4
FutureCitySewerDeath = Scene("FutureCitySewerDeath", "You kept walking until you are swept up by a large amount of flowing liquid, you fell down a large pit and died. The last of the humans either escaped Earth or became Artificial Intelligence slaves for the rest of their lives.",
                             {"Press 1 to continue":"Death"})






################Advanced's Scenes minimum of 3 decision points
StartAdv = Scene("StartAdv", "You are standing at the top of a mountain! You see a family hiding a cave behind you. You are dressed in nothing more than a piece of cloth draped over your shoulder and a large club in your hand. You immediately see a large Pterodactyl shrieking as it flies towards you opening its jaw. What will you do?",
                 {f"Dodge": "Damage", f"Attack": "DamagePterodactyl", f"Run": "Damage"})

DamagePterodactyl = Scene("DamagePterodactyl", "You successfully damaged the Pterodactyl and it disappeared! You're confused but more scared for your life than anything. There's more enemies coming at you! What will you do?", 
                     {"Keep fighting": "StartAdvVictory", "Escape": "Damage"})

StartAdvVictory = Scene("StartAdvVictory", "The Pterodactyls have been defeated! You fought with some other worldly strength. What will you do?",
                        {"Celebrate":"SpartanAdv", "Drop your weapons and check on the family":"Damage"})

##Spartan Era minimum of 3 decision points
SpartanAdv = Scene("SpartanAdv", "You close your eyes briefly and hear a voice saying, 'Commander, we are surrounded on all sides what should we do?' You notice you are covered head to toe in armor with a sword on your hip. You are stationed at the top of a mountain with seemingly no means of escape. What will you do?", 
                 {"Prepare the archers at each corner of our fortress with the majority covering the entrances.": "SpartanArchers", "Surrender": "Damage", "Escape through the less guarded side of the fortress and fight our way out!": "SpartanEscape"})

SpartanArchers = Scene("SpartanArchers", "Your men are in position to defend the fortress, it is an amazing battle and you are holding them off well. However, your arrows won't last forever. What will you do?", 
                     {"Send all available soldiers and some of the archers out to start fighting with swords.":"SpartanEscape", "Continue firing arrows":"Damage", "Move all archers to the main entrance":"Damage"})

SpartanEscape = Scene("SpartanEscape", "You are battling every inch, trying to get through this army to freedom! There seems to be no end in sight of these enemy soldiers. What will you do?", 
                    {"Fight On!": "Damage", "Tell your men to retreat to the fortress": "SpartanRetreat"})

SpartanRetreat = Scene("SpartanRetreat", "Your men retreated, the remaining archers at the fortress damaged the enemy as the infantry made it back to the fortress.", 
                     {"Circle your infantry around the backside and pinch the enemy": "SpartanVictory", "Hold the fortress with everything we can":"Damage"})

SpartanVictory = Scene("SpartanVictory", "They had nowhere to go. Victory is yours!", 
                     {"Press 1 to continue": "ZombiesBegin"})

##Zombie Era minimum of 3 decision points

ZombiesBegin = Scene("ZombiesBegin", "You open your eyes to see you are now in a new world. You are in the wreckage of a once booming city with large skyscrapers everywhere. Vehicles are wrecked everywhere and there is blood everywhere. You ask a man next to you, 'What happened here?' He replies the worst zombie outbreak imaginable. Nearly no one survived. The only known weakness is cold temperatures. He said it is up to you guys to hold one of the last civilizations.",
                     {"Barricade all the doors and windows with boards":"ZombiesWindows", "Setup pits and spikes all around the perimeter of your stronghold":"ZombiesSpikes", "Flee up north to get to a colder climate":"ZombiesEscape"})

ZombiesWindows = Scene("ZombiesWindows", "Night approaches and a huge horde of zombies starts approaching your stronghold. You bring out the heavy artillery and start shooting from the roof. They quickly get to your stronghold. Luckily your stronghold is secured. What will you do?", 
                       {"Stab spears throw cracks in boarded windows stopping them from entering":"ZombiesBoards","Throw bombs from the roof onto the zombies at your stronghold":"ZombiesBombs"})

ZombiesSpikes = Scene("ZombiesSpikes", "Night approaches and a huge horde of zombies starts approaching your stronghold. You bring out the heavy artillery and start shooting from the roof. They are slow to get to your stronghold due to your defenses. The Zombies have begun climbing over the zombies stuck on the spikes and the zombies in the pits. They have now made it to your stronghold. What will you do?", 
                      {"Stab spears throw cracks in boarded windows stopping them from entering":"ZombiesBoards","Throw bombs from the roof onto the zombies at your stronghold":"ZombiesBombs"})

ZombiesBoards = Scene("ZombiesBoards", "You are keeping the zombies at bay but you can't stop them from all angles simultaneously. They have breached through a side window. What will you do?",
                      {"Attack the zombies as you head to the basement to hide in the vault":"ZombiesStrongholdVictory", "Hold the zombies of as you head the roof. You plan to lower yourselves down and get to the vehicles.":"ZombiesDeath"})

ZombiesBombs = Scene("ZombiesBombs", "You are resisting the zombies back but you can't stop them from all angles at the same time. They have breached through a side window. What will you do?",
                   {"Attack the zombies as you head to the basement to hide in the vault":"ZombiesStrongholdVictory", "Hold the zombies of as you head the roof. You plan to lower yourselves down and get to the vehicles.":"ZombiesDeath"})

##Outcome Adv 1
ZombiesDeath = Scene("ZombiesDeath", "You successfully made it to the roof and are lowering everyone down. You are halfway done when some zombies have made it to your allies. You and your team fend most of them off as you get to the car. The car won't start. Your car slowly gets broken into and everyone is infected.",
                     {"Press 1 to continue":"Death"})

ZombiesStrongholdVictory = Scene("ZombiesStrongholdVictory", "You made it to the basement and to the vault. You have explosives in the basement. What will you do?",
                                 {"Hide in the vault until the coast is clear":"Damage","Sacrifice yourself to blow up the explosives while everyone else is in the vault":"ZombiesBlownUp","Ask someone else to volunteer to blow up the explosives":"Damage"})

##Outcome Adv 2
ZombiesBlownUp = Scene("ZombiesBlownUp", "The explosives went off and the house blew up. The zombie horde was killed. Your allies made it out safely and traveled by ship to find a northern civilization. They have a deep gratitude for what you have done for them.",
                       {"Press 1 to continue": "Finish"})

ZombiesEscape = Scene("ZombiesEscape", "You escape to the north and are able to get 1/2 of the stronghold to join you. How will you travel?", 
                      {"plane":"ZombiesPlane", "Ship":"ZombiesShip", "Vehicles":"Damage"})

ZombiesPlane = Scene("ZombiesPlane", "You travel to a small airport nearby. You are lucky to find one plane left at the airport. Your friend repairs it all day. It is getting darker and you know the zombies are close by. The pilot starts the engine and zombies are hording around. They blow past the zombies and it is smooth sailing from there. Until the warning signals begin going off. The plane is going down. What will you do?",
                     {"Aim the plane towards the ocean": "ZombiesPlaneDeath", "Aim the plane towards a forest":"ZombiesPlaneDeath"})

##Outcome Adv 3
ZombiesPlaneDeath = Scene("ZombiesPlaneDeath", "The pilot begins steering plane until one of the propellers stop working. The pilot is doing his best to manage the plane until it broke in half. No one survived the crash.",
                          {"Press 1 to continue": "Death"} )

ZombiesShip = Scene("ZombiesShip", "You and your allies make it to the dock. It's almost night. You get the ship working and push it full steam ahead. The zombies are alerted to the noise and start running towards you. The zombie leaps towards you hands and mouth open to grab you. Your ally shoots the zombie at the last second and saves your life. You continue on the ship and must decide where to go.", 
                    {"Go to Greenland":"Damage", "Go to Canada":"ZombieShipVictory"})

#Outcome Adv 4
ZombieShipVictory = Scene("ZombieShipVictory", "You and your allies made it to Canada safely and are relieved to finally be safe. As long as you live you and your team will do whatever it takes to stop this pandemic.",
                         {"Press 1 to continue": "Finish"} )




################Nightmare's Scenes minimum of 3 decision points
StartNig = Scene("StartNig", "You are standing at the top of a mountain! You see a small family hiding a cave behind you. You are dressed in nothing more than a piece of cloth draped over your shoulder and a large club in your hand. You immediately see a large Velociraptor screeching as it sprints towards you. What will you do?",
                 {f"Dodge": "Damage", f"Attack": "DamageVelociraptor", f"Run": "Damage"})

DamageVelociraptor = Scene ("DamageVelociraptor", "You successfully damaged the Velociraptor and it disappeared! You're confused but more scared for your life than anything. There's more enemies coming at you! What will you do?", 
                     {"Keep fighting": "StartNigVictory", "Escape": "Damage"})

StartNigVictory = Scene("StartNigVictory","The Velociraptors have been defeated! You fought with some other worldly strength. What will you do?",
                        {"Celebrate":"Damage", "Drop your weapons and check on the family":"PyramidsNig"})

##Pyramids Era minimum of 4 decision points
PyramidsNig = Scene("PyramidsNig", "You close your eyes briefly and the darkness all around you disappears as the light from your torch illuminates the room to display a tan stone hallway. You see a large pit at least 10 feet long with no bottom in sight. You hear a friendly telling you to hurry up from another room on the other side of the pit. It sounds like their voice is leaving you behind. What will you do?", 
                    {"Lower yourself into the pit to check the depth": "Damage", "Look around":"PyramidsWhip", "Jump across the pit":"Damage"})

PyramidsWhip = Scene("PyramidsWhip", "You look around and find a whip, a pair of gloves, and an old wood plank. What will you do?",
                        {"Try to Indian Jones your away across the pit with the branch above the pit":"PyramidsVictoryWhip", "Place the plank over the pit and walk across":"PyramidsPlank"})

PyramidsPlank = Scene("PyramidsPlank", "As you take your second step on the plank it begins to creak underneath you. What will you do?",
                      {"Retreat and try the whip":"PyramidsVictoryWhip", "Jump across the pit":"Damage", "Get on your hands and knees and scoot across the plank":"Damage"})

PyramidsVictoryWhip = Scene("PyramidsVictoryWhip", "You have no idea how you did it but you earned your real life Indiana Jones accomplishment, you that branch with your whip magically tying it up, swung across, landed safely, and flicked your whip magically releasing it. You reunite with your partner. You discover a room full of mummies. What will you do?", 
                           {"Will you open up mummy number 1": "PyramidsCorrectMummy", "Will you open up mummy number 2": "Damage", "Will you open up mummy number 3": "Damage", "Leave the mummies and run like a bat out of heck out of there": "Damage"})

PyramidsCorrectMummy = Scene("PyramidsCorrectMummy", "As you open up the mummy you discover a strange looking artifact in the mummy's hands. Your partner is relieved to know you found the heart of the pyramid. Great job!", 
                             {"Keep the heart of the pyramid for yourself and sprint out of there":"Damage", "Return as a team with the heart of the pyramid in hand": "PyramidsVictory"})

PyramidsVictory = Scene("PyramidsVictory","You both return in glory with heart of the pyramid in hand", 
                        {"Press 1 to continue": "Dystopian"})

#Dystopian Era minimum of 3 decision points

Dystopian = Scene("Dystopian", "You open your eyes to an amazing view of a city built so high most buildings are taller than the clouds. You walk into a meeting and see there is a group of people that have formed a rebellion. Each sector has their own colored uniformed. There is red, yellow, green, blue, and brown. What will you say?", 
                   {"What is the problem?":"DystopianProblem", "What's the plan?":"DystopianPlan"})

DystopianProblem = Scene("DystopianProblem", "The problem is our government. Everyone is assigned a job to do when they turn 18 and they have to perform that task and live in their sector until the day they die. This is wrong. We need to stop this. What will you say?",
                         {"What can we do to stop it?": "DystopianPlan", "Let's just go back home I'm sure it's not that bad to live here": "Damage"})

DystopianPlan = Scene("DystopianPlan", "You hear someone say, 'We are out of time. We need to act quick. They are planning to separate all of the sectors into different parts of the country. If they do that we have no hope. If we do not fix this by midnight, freedom as we know it will be gone for everyone within the reach of these monsters.' What do you suggest?", 
                       {"Sneak into the capitol dressed as a cop, and display our own message to stand up and fight to everyone": "DystopianMessage", "Sneak in the sewer of the capitol, and take out President Griffin.":"DystopianSewer"})

DystopianMessage = Scene("DystopianMessage", "We got the disguise now we need you to act as normal as possible, they will detect even the slightest nervousness. You go in talking about a routine inspection and how you need to check the security of the upper floors due to the recent threat received by the police. Once this is conveyed to the secretary it takes forever to get a response and your forehead starts sweating. She then tells you to wait for your escort. You are introduced to Agent Rose who will be accompanying you as you inspect the building. You play along searching each floor ensuring everything is secure trying to find a plan to get rid of her. Through your piece you are given a few options from your team",
                 {"Push agent rose out of a window":"Damage", "Kill agent Rose with a knife from the kitchen":"DystopianMurder", "Pretend like you are sick and lock her out of the office while you broadcast the message":"DystopianSick"})

##Outcome Nig 1
DystopianMurder = Scene("DystopianMurder", "You get the knife from the kitchen and conceal it in your pocket hoping she didn't notice. You get to the directing office and it is empty. You get in and begin clearing the room as normal, you go behind agent Rose and take her out without a sound. You lock up the room and begin displaying your message of rebellion all across the city excluding the capitol building. Shortly before the message is over security breaks into the office and arrests you. The message of the rebellion worked there were riots in every place of work. People began to stand up for themselves. The government crumbled and freedom was once more.",
                        {"Press 1 to continue":"Finish"})
##Outcome Nig 2
DystopianSick = Scene("DystopianSick", "You successfully locked Agent Rose out of the room and tried to get the broadcast running as quick as possible. The broadcast is working! Shortly after Agent Rose breaks into the room, you fight back but she gets the upper hand and cuffs you with your hands behind your back. The broadcast is stopped 30 seconds in. You ended up in jail and were killed for your crimes. Some people began to rebel as a result of the video but it wasn't enough. With discipline and sheer force they kept the people in line and the dystopian civilization lived on.",
                      {"Press 1 to continue":"Death"})

DystopianSewer = Scene("DystopianSewer", "You pop open the hatch and begin lowering yourself into the sewer. You begin walking forward with your flashlight in hand. You walk much farther than anticipated and are not sure if you missed the building. You come to a fork, go left or right What will you do?", 
                        {"Return to make sure you went the right way":"DystopianReturn", "Turn left, you know you are close": "DystopianLeft", "Turn right, you know you are close": "Damage"})

DystopianReturn = Scene("DystopianReturn", "You return and are told it was a left turn in the sewer. But your team wants to reconsider the plan. What will you do",
                        {"Sneak into the capitol dressed as a cop, and display our own message to stand up and fight to everyone": "DystopianMessage", "Sneak in the sewer of the capitol, and take out President Griffin.":"DystopianSewer"})

DystopianLeft = Scene("DystopianLeft", "You went left, unsure if you went the correct way. You soon stumble upon the base of capitol. There is a small maintenance elevator that you can access by going up the sewer grate inside of the garage but you need to ensure you pick the right one. What will you do?",
                      {"Go up sewer number 1":"DystopianSewerDeath", "Go up sewer number 2":"DystopianSuccess"})
##Outcome Nig 3
DystopianSewerDeath = Scene("DystopianSewerDeath", "You made it into what appears to be the garage. You open the nearest door. There is a room full of agents that take you out, deeming you a traitor of the government.",
                            {"Press 1 to continue":"Death"})

##Outcome Nig 4
DystopianSuccess = Scene("DystopianSuccess", "You made it into what appears to be the garage and you see the elevator. You change clothes to appear like a garbageman and begin your ascent in the elevator. Once you have made it to the right floor you go through the floor emptying all of the trash cans. Finally, you see Griffin's office. But you need a distraction. You pull a fire alarm and quickly hurry out of sight. Griffin is leaving the room last when you pull out your gun and tell him to stay behind. You were able to topple the government and bring freedom to all.",
                         {"Press 1 to continue":"Finish"})






################Impossible's Scenes
StartImp = Scene("StartImp", "You are standing at the top of a mountain! You see a small family hiding a cave behind you. You are dressed in nothing more than a piece of cloth draped over your shoulder and a large club in your hand. You immediately see a large T-rex roaring as it is running at you. What will you do?",
                 {f"Dodge": "Damage", f"Attack": "DamageTrex", f"Run": "Damage"})

DamageTrex = Scene ("DamageTrex", "You successfully damaged the T-rex and it disappeared! You're confused but more scared for your life than anything. There's more enemies coming at you! What will you do?", 
                     {"Keep fighting": "StartImpVictory", "Escape": "Damage"})

StartImpVictory = Scene("StartImpVictory","The T-rexes have been defeated! You fought with some other worldly strength. What will you do?",
                        {"Celebrate":"Damage", "Drop your weapons and check on the family":"AthensImp"})

##Athens Era
AthensImp = Scene("AthensImp", "You close your eyes briefly and hear a voice saying, 'Commander, we are surrounded on all sides what should we do?' You notice you are covered head to toe in armor with a sword on your hip. You are stationed at the top of a mountain with seemingly no means of escape. What will you do?", 
                 {"Prepare the archers at each corner of our fortress with the majority covering the entrances.": "AthensArchers", "Surrender": "Damage", "Escape through the less guarded side of the fortress and fight our way out!": "AthensEscape"})

AthensArchers = Scene("AthensArchers", "Your men are in position to defend the fortress, it is an amazing battle and you are holding them off well. However, your arrows won't last forever. What will you do?", 
                     {"Send all available soldiers and some of the archers out to start fighting with swords.":"AthensEscape", "Continue firing arrows":"Damage", "Move all archers to the main entrance":"Damage"})

AthensEscape = Scene("AthensEscape", "You are battling every inch, trying to get through this army to freedom! There seems to be no end in sight of these enemy soldiers. What will you do?", 
                    {"Fight On!": "Damage", "Tell your men to retreat to the fortress": "AthensRetreat"})

AthensRetreat = Scene("AthensRetreat", "Your men retreated, the remaining archers at the fortress damaged the enemy as the infantry made it back to the fortress.", 
                     {"Circle your infantry around the backside and pinch the enemy": "AthensVictory", "Hold the fortress with everything we can":"Damage"})

AthensVictory = Scene("AthensVictory", "They had nowhere to go. Victory is yours!", 
                     {"Press 1 to continue": "Doomsday"})

##Doomsday Era  3 minimum decision points
Doomsday = Scene("Doomsday", "Your eyes open to a room filled with people of power from all kinds of nationalities. You are dressed in a suit and seem to be a leader as well. You are informed that world is ending. What disaster do you desire?",
                 {"A meteorite is heading towards earth that is large enough to kill 1/2 the population if not knock Earth out of orbit":"DoomsdayMeteorite", "Pollution is devastating the human race. The population is down to 3 billion worldwide and diminishing daily. We need an answer": "DoomsdayPollution", "We received information Russia is launching a large scale Nuclear bomb to an unknown location":"DoomsdayNuke", "The polar ice caps are almost nonexistent and we are dealing with a worldwide tsunamis and flooding": "DoomsdayTsunamis"})

DoomsdayMeteorite = Scene("DoomsdayMeteorite", "There is a meteorite heading to earth, here are ways to neutralize the threat",
                          {"Prepare a nuclear bomb attached to a spaceship and launch it into the meteorite":"Damage","Land on it, drill to the core, and place explosives":"Armageddon"})

Armageddon = Scene("Armageddon", "We are going to land on the meteorite, drill to its core, and blow it up. We launch our spaceship. We are flying through space at this meteorite with little time to spare. You successfully landed the spaceship. How should we drill?",
                   {"Drill at Site 1":"Damage", "Drill at Site 2":"Damage", "Drill at Site 3": "DoomsdayDrill"})
##Outcome Imp 1
DoomsdayDrill = Scene("DoomsdayDrill", "The drilling is successful. It is taking longer than expected but we are getting through to the core of the meteorite. You deployed the bomb successfully. We only have 33 seconds until we need to detonate the bomb. We hurry back to the spaceship and launch immediately. We need to detonate the bomb but we're not sure if we are far enough away. The bomb is deployed. Debris hit the spaceship, we are hurrying back to Earth. The spaceship is falling apart as we enter the atmosphere. The parachute deployed successfully, we are going to be ok! Earth is saved!",
                      {"Press 1 to continue":"Finish"})

DoomsdayPollution = Scene("DoomsdayPollution", "Pollution is taking over the world and bad air quality is killing hundreds of people daily if not more. What can we do?",
                          {"Escape earth on a spaceship":"Damage", "Build an underground civilization":"DoomsdayUnderground"})

DoomsdayUnderground = Scene("DoomsdayUnderground", "In what country should we build our underground civilization?",
                            {"India":"Damage", "Estonia":"DoomsdayDig", "Bangladesh":"Damage"} )
##Outcome Imp 2
DoomsdayDig = Scene("DoomsdayDig", "Great idea, Estonia has some of the best air quality in the world and can support a large growth of nature to help regrow the planet. We need to act quick to get the resources to begin digging. During construction another 1 billion people have lost their lives to pollution. The entire country of Estonia and other costal islands with good air quality now have self-sustaining underground civilizations. Thank you for saving us!",
                    {"Press 1 to continue":"Finish"})

DoomsdayNuke = Scene("DoomsdayNuke", "Russia is launching a nuclear attack within the next week but we need to know when and where to evacuate as many people as possible. How can we find  more information?",
                     {"Go undercover as a spy": "Damage", "Hack into national broadcasts":"DoomsdayHack", "Start evacuating all major cities around the world":"Damage"})

DoomsdayHack = Scene("DoomsdayHack", "Great job! After tireless work of 10,000s of people day and night across the globe we have hacked into the Russian communication. The bad news is we only have 1 day to prepare for the attack and we still have three possible bombing sites. To which site should deploy the most resources to evacuating people?",
                     {"Shanghai,China":"DoomsdayBombSite", "Dhaka, Bangladesh":"Damage", "Delhi,India":"Damage"})
##Outcome Imp 3 
DoomsdayBombSite =Scene("DoomsdayBombSite", "We deployed all of the world's best resources to evacuate everyone from Shanghai, China. Russia began flying their bombers all over the world. There were too many planes to keep track of over Asia until the bomb was finally dropped on Shanghai. You saved the lives of over 28 million people. We are forever in your debt. Thank you for saving these lives!",
                        {"Press 1 to continue":"Finish"})

DoomsdayTsunamis = Scene("DoomsdayTsunamis", "The polar ice caps have melted and the water across the globe is completely out of control. California is now completely submerged in water and we need to know what to do to to save the planet.",
                         {"Refreeze the polar ice caps and reduce emissions":"DoomsdayFreeze", "Build flood protection for the most vulnerable coasts across the world and reduce emissions":"Damage", "Develop technology to remove greenhouse gases and stop all gas emitting devices and machinery":"Damage"})

DoomsdayFreeze = Scene("DoomsdayFreeze", "You have decided to refreeze the polar ice caps. We are working tirelessly day and night to develop the necessary technology. Several devastating effects of losing the polar ice caps are coming to fruition. Global warming is having devastating effects in dry climates and is making unbearable to be outside almost anywhere. Animals across the globe are losing their habitats. Over 500,000,000 homes and businesses have been destroyed. Tensions between nations for lack of help and resources are raging out of control. We need a solution. Where should we begin freezing?",
                       {"North pole":"Damage", "South Pole":"FreezeSouth"})
##Outcome Imp 4
FreezeSouth = Scene("FreezeSouth", "You have successfully lead the mission to refreeze the southern ice cap. We need to immediately begin on doing the same for the northern polar ice cap. There is still a lot of work to do, recovering sunken land, restoring homes, restoring businesses, restoring animal habitats, and minimizing greenhouse gases. Thank you for helping the planet!",
                    {"Press 1 to continue":"Finish"})

#run main
def main():
    player = start_adventure()

    # Scene map 
    scenes = {
        # Introduction Scene
        "Intro": Intro,
        # Beginner's Scenes
    #Caveman era
        "StartBeg": StartBeg,
        "DamageCaveman": DamageCaveman,
        "OtherWeaponBeg": OtherWeaponBeg,
        "StartBegVictory": StartBegVictory,
    #Greek Era
        "GreekBeg": GreekBeg,
        "GreekArchers": GreekArchers,
        "GreekEscape": GreekEscape,
        "GreekRetreat": GreekRetreat,
        "GreekVictory": GreekVictory,
    #Dragon Era
        "DragonsBegin": DragonsBegin,
        "DragonsCommander": DragonsCommander,
        "DragonsJanitor": DragonsJanitor,
        "DragonsSinks": DragonsSinks,
        "DragonsEliteTeam": DragonsEliteTeam,
        "DragonsAssassin": DragonsAssassin,
        "DragonsAssassinFear": DragonsAssassinFear,
        "DragonsLeader": DragonsLeader,
        "DragonsAssemble": DragonsAssemble,
        "DragonsSiege": DragonsSiege,
        "DragonsBruteForce": DragonsBruteForce,
        "DragonsLighten": DragonsLighten,
        "DragonsHorse": DragonsHorse,
        "DragonsInfantryPush": DragonsInfantryPush,
        "DragonsSearch": DragonsSearch,


    # Intermediate's Scenes
        # Jungle Era
        "StartInt": StartInt,
        "DamageBeetle": DamageBeetle,
        "OtherWeaponInt": OtherWeaponInt,
        "StartIntVictory": StartIntVictory,
        # Egyptian Era
        "EgyptianInt": EgyptianInt,
        "EgyptianWhipInt": EgyptianWhipInt,
        "EgyptianPlank": EgyptianPlank,
        "EgyptianVictoryInt": EgyptianVictoryInt,
        "EgyptianCorrectMummy": EgyptianCorrectMummy,
        "EgyptianVictory": EgyptianVictory,
        # Future Era
        "FutureCity": FutureCity,
        "FutureCityAI": FutureCityAI,
        "FutureCityPlan": FutureCityPlan,
        "FutureCityNuke": FutureCityNuke,
        "FutureCityRoofPlan": FutureCityRoofPlan,
        "FutureCityDeath": FutureCityDeath,
        "FutureCityUploadedVirus": FutureCityUploadedVirus,
        "FutureCityVirusSuccess": FutureCityVirusSuccess,
        "FutureCitySewer": FutureCitySewer,
        "FutureCityReturn": FutureCityReturn,
        "FutureCitySewerFlashlight": FutureCitySewerFlashlight,
        "FutureCitySewerReturn": FutureCitySewerReturn,
        "FutureCitySewerDeath": FutureCitySewerDeath,

        # Advanced's Scenes 
        "StartAdv": StartAdv, 
        "DamagePterodactyl": DamagePterodactyl, 
        "StartAdvVictory": StartAdvVictory, 
        "SpartanAdv": SpartanAdv, 
        "SpartanArchers": SpartanArchers, 
        "SpartanEscape": SpartanEscape, 
        "SpartanRetreat": SpartanRetreat, 
        "SpartanVictory": SpartanVictory, 
        "ZombiesBegin": ZombiesBegin, 
        "ZombiesWindows": ZombiesWindows, 
        "ZombiesSpikes": ZombiesSpikes, 
        "ZombiesBoards": ZombiesBoards, 
        "ZombiesBombs": ZombiesBombs, 
        "ZombiesDeath": ZombiesDeath, 
        "ZombiesStrongholdVictory": ZombiesStrongholdVictory, 
        "ZombiesBlownUp": ZombiesBlownUp, 
        "ZombiesEscape": ZombiesEscape, 
        "ZombiesPlane": ZombiesPlane, 
        "ZombiesPlaneDeath": ZombiesPlaneDeath, 
        "ZombiesShip": ZombiesShip, 
        "ZombieShipVictory": ZombieShipVictory,

        # Nightmare's Scenes 
        "StartNig": StartNig, 
        "DamageVelociraptor": DamageVelociraptor, 
        "StartNigVictory": StartNigVictory, 
        # Pyramids Era 
        "PyramidsNig": PyramidsNig, 
        "PyramidsWhip": PyramidsWhip, 
        "PyramidsPlank": PyramidsPlank, 
        "PyramidsVictoryWhip": PyramidsVictoryWhip,
        "PyramidsCorrectMummy": PyramidsCorrectMummy, 
        "PyramidsVictory": PyramidsVictory, 
        # Dystopian Era 
        "Dystopian": Dystopian, 
        "DystopianProblem": DystopianProblem, 
        "DystopianPlan": DystopianPlan, 
        "DystopianMessage": DystopianMessage,
        "DystopianMurder": DystopianMurder, 
        "DystopianSick": DystopianSick, 
        "DystopianSewer": DystopianSewer, 
        "DystopianReturn": DystopianReturn, 
        "DystopianLeft": DystopianLeft, 
        "DystopianSewerDeath": DystopianSewerDeath, 
        "DystopianSuccess": DystopianSuccess,

        # Impossible's Scenes 
        "StartImp": StartImp, 
        "DamageTrex": DamageTrex, 
        "StartImpVictory": StartImpVictory, 
        "AthensImp": AthensImp, 
        "AthensArchers": AthensArchers, 
        "AthensEscape": AthensEscape, 
        "AthensRetreat": AthensRetreat, 
        "AthensVictory": AthensVictory, 

        # Doomsday Era 
        "Doomsday": Doomsday, 
        "DoomsdayMeteorite": DoomsdayMeteorite, 
        "Armageddon": Armageddon, 
        "DoomsdayDrill": DoomsdayDrill, 
        "DoomsdayPollution": DoomsdayPollution, 
        "DoomsdayUnderground": DoomsdayUnderground, 
        "DoomsdayDig": DoomsdayDig, 
        "DoomsdayNuke": DoomsdayNuke, 
        "DoomsdayHack": DoomsdayHack, 
        "DoomsdayBombSite": DoomsdayBombSite, 
        "DoomsdayTsunamis": DoomsdayTsunamis, 
        "DoomsdayFreeze": DoomsdayFreeze, 
        "FreezeSouth": FreezeSouth,
    }





    # Game loop
    while player.lives > 0:
        current_scene = scenes[player.next_scene]
        next_scenes = current_scene.display()

        # Get player's choice
        try:
            choice = int(input("\nEnter your choice: ")) - 1
            if choice < 0 or choice >= len(next_scenes):
                raise ValueError("Invalid choice!")
        except ValueError:
            print("Invalid choice! Please try again.")
            continue

        # Determine next scene
        player.next_scene = next_scenes[choice]

        # Handle "Damage" case
        if "Damage" == player.next_scene:
            player.takeDamage()
            player.next_scene = current_scene.name  # Stay in the current scene to retry
        elif "Finish" == player.next_scene:
            player.finish()
            try_again()
        elif "Death" == player.next_scene:
            player.lives = 1
            player.takeDamage()

        

# run main when code is ran
if __name__ == "__main__":
    main()