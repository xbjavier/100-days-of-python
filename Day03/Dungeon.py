import random

print("Welcome to the Dungeon of Despair!")
print("Your quest is to find the legendary Sword of Destiny and defeat the evil dragon that lurks within.")

win_condition = False
player = {
    "dead": False,
    "hp": 10,
    "inventory": {
        "rations": 10,
        "heal_potion": 10
    }
}

bonus_actions = {
    "search",
    "heal potion"
}

print('''        _
       (_)
       |=|
       |=|
   /|__|_|__|\\
  (    ( )    )
   \|\/\"/\/|/
     |  Y  |
     |  |  |
     |  |  |
    _|  |  |
 __/ |  |  |\\
/  \ |  |  |  \\
   __|  |  |   |
/\/  |  |  |   |\\
 <   +\ |  |\ />  \\
  >   + \  | LJ    |
        + \|+  \  < \\
  (O)      +    |    )
   |             \  /\ 
 ( | )   (o)      \/  )
_\\\\|//__( | )______)_/ 
        \\\|//        ''')

# Define a function for handling player choices
def get_player_choice(current_room):
    while True:
        choice = input("> ").lower()
        if choice.startswith("go") or choice in current_room["actions"]:
            return choice
        else:
            print("Invalid choice. Please try again.")


def action_success(failure_rate: float):
    rand_float = random.random()
    return rand_float > failure_rate;

def run_action(current_room, action, auto_success: False):
    
    if auto_success:
        action_completed_successfuly = True
    else:
        action_completed_successfuly = action_success(action["failure_rate"])

    failure = action["failure"]
    success = action["success"]
    remove_actions = None

    if not action_completed_successfuly:
        print(failure["description"])
        if "player_dead" in failure:
            player["dead"] = failure["player_dead"]

        if "remove_actions" in failure:    
            remove_actions =failure["remove_actions"]
    else:
        print(success["description"])
        if "damage" in success:
            player["hp"] -= success["damage"]
            print(f"damage received: {success["damage"]}")
            if "win_condition" in success:
                win_condition = success["win_condition"]
    
        if "remove_actions" in success:
            remove_actions = success["remove_actions"]
        if "unlocks" in success:
            current_room["exits"].update(success["unlocks"])

    if remove_actions:
        for action in remove_actions:
            del current_room["actions"][action]
            

def perform_bonus_action(current_room, action):
    if action not in bonus_actions or "bonus_actions_results" not in current_room:
        return
    
    results = current_room["bonus_actions_results"]
    if action.lower() == "search":
        for item in results["search"]:
            player["inventory"][item["item"]] = item["quantity"]
            print(f"You have found {item["item"]}...\n {item["description"]}")
            del item

    input("Press Any key to continue...")
    

# Create a dictionary for rooms
rooms = {
    "starting_room": {
        "description": "You find yourself in a dimly lit chamber with stone walls and a dusty floor. A narrow passage leads to the north.",
        "actions": None,
        "exits": {"north": "goblin_lair"},
        "ascii": '''88888888888888888888888888888888888888888888888888888888888888888888888
88.._|      | `-.  | `.  -_-_ _-_  _-  _- -_ -  .'|   |.'|     |  _..88
88   `-.._  |    |`!  |`.  -_ -__ -_ _- _-_-  .'  |.;'   |   _.!-'|  88
88      | `-!._  |  `;!  ;. _______________ ,'| .-' |   _!.i'     |  88
88..__  |     |`-!._ | `.| |_______________||."'|  _!.;'   |     _|..88
88   |``"..__ |    |`";.| i|_|MMMMMMMMMMM|_|'| _!-|   |   _|..-|'    88
88   |      |``--..|_ | `;!|l|MMoMMMMoMMM|1|.'j   |_..!-'|     |     88
88   |      |    |   |`-,!_|_|MMMMP'YMMMM|_||.!-;'  |    |     |     88
88___|______|____!.,.!,.!,!|d|MMMo * loMM|p|,!,.!.,.!..__|_____|_____88
88      |     |    |  |  | |_|MMMMb,dMMMM|_|| |   |   |    |      |  88
88      |     |    |..!-;'i|r|MPYMoMMMMoM|r| |`-..|   |    |      |  88
88      |    _!.-j'  | _!,"|_|M)(MMMMoMMM|_||!._|  `i-!.._ |      |  88
88     _!.-'|    | _."|  !;|1|MbdMMoMMMMM|l|`.| `-._|    |``-.._  |  88
88..-i'     |  _.''|  !-| !|_|MMMoMMMMoMM|_|.|`-. | ``._ |     |``"..88
88   |      |.|    |.|  !| |u|MoMMMMoMMMM|n||`. |`!   | `".    |     88
88   |  _.-'  |  .'  |.' |/|_|MMMMoMMMMoM|_|! |`!  `,.|    |-._|     88
88  _!"'|     !.'|  .'| .'|[@]MMMMMMMMMMM[@] \|  `. | `._  |   `-._  88
88-'    |   .'   |.|  |/| /                 \|`.  |`!    |.|      |`-88
88      |_.'|   .' | .' |/                   \  \ |  `.  | `._    |  88
88     .'   | .'   |/|  /                     \ |`!   |`.|    `.  |  88
88  _.'     !'|   .' | /                       \|  `  |  `.    |`.|  88
88888888888888888888888888888888888888888888888888888888888888888888888'''
    },
    "goblin_lair": {
        "description": "You enter a damp, moss-covered cavern filled with the stench of stale ale and burnt meat. Goblins huddle around a crackling fire, sharpening their rusty weapons.",
        "actions": {
            "attack": {
                "failure_rate": .2,
                "success":{
                    "description": "You engage in battle with the goblins, you're victorious but received some damage",
                    "damage": 2,
                    "unlocks": {"hidden_passage": "treasure_chamber"},
                    "remove_actions": ["sneak", "negotiate"]
                } ,
                "failure":{
                    "description": "Seems like you're not worthy of the sword, you lost agains some random Goblins...",
                    "damage": 100,
                    "player_dead": True
                }

            },
            "sneak": {
            "failure_rate": .5,
            "success": {
                "description": "You manage to slip past the goblins unnoticed, finding a hidden passage behind a pile of crates.",
                "unlocks": {"hidden_passage": "treasure_chamber"},
                "remove_actions": ["attack", "negotiate"]
            },
            "failure": {
                "description": "One of the goblins spots you! Prepare for battle!",
                "triggers": ["attack"],
                "remove_actions": ["negotiate"]  # Trigger the attack action if sneaking fails
            }
        },
            "negotiate": {
                "failure_rate": .75,
                "success": {
                    "description": "Through a combination of threats and bribes, you convince the goblins to let you pass. They reveal a hidden passage in exchange for some of your rations.",
                    "unlocks": {"hidden_passage": "treasure_chamber"},
                    "consumes": ["rations"],
                    "remove_actions": ["attack","sneak"],
                    "ascii": ''',      ,
            /(.-""-.)\\
        |\  \/      \/  /|
        | \ / =.  .= \ / |
        \( \   o\/o   / )/
         \_, '-/  \-' ,_/
           /   \__/   \\
           \ \__/\__/ /
         ___\ \|--|/ /___
       /`    \      /    `\\
   /       '----'       \\'''
                },
                "failure": {
                    "description": "The goblins laugh at your attempts to negotiate. They seem more interested in tasting your flesh than your words.",
                    "triggers": ["attack"],
                    "remove_actions": ["sneak"],
                    "ascii": ''',      ,
            /(.-""-.)\\
        |\  \/      \/  /|
        | \ / =.  .= \ / |
        \( \   o\/o   / )/
         \_, '-/  \-' ,_/
           /   \__/   \\
           \ \__/\__/ /
         ___\ \|--|/ /___
       /`    \      /    `\\
   /       '----'       \\'''
                }
            }
        },
        "exits": {
            }
    },
    "treasure_chamber": {
        "description": "You found a treasure chamber!",
        "exits":{
            "north": "dragon_chamber",
            "right": "tramp"
        },
        "bonus_actions_results":{
            "search": [{
                "item": "Sword of Destiny",
                "description": "You found the Sword of Destiny, you can slain the dragon now",
                "quantity": 1
            }]
        }
    },
    "dragon_chamber":{
        "actions": {
            "attack": {
                "failure_rate": .95,
                "success": {
                    "description": "You have slain the dragon! , you can return safe to your hometown",
                    "win_condition": True
                },
                "failure":{
                    "description": "Dragon had a good meal with you...",
                    "player_dead": True
                }
            }
        },
        "description": "You have found the dragon chamber, it's time to prove your skills"
    },
    "tramp":{
        "description": "You have fell into a tramp...",
        "game_over": {
            "description": "You fell into a tramp and died"
        }
    }
}

# Start the game in the starting room
current_room = rooms["starting_room"]
previous_room = None

# Main game loop
while True:

    if win_condition:
        print("You won!")
        break
    # Print ascii art
    if "ascii" in current_room and current_room != previous_room:
        print(current_room["ascii"])

    if "game_over" in current_room:
        print(f"{current_room["game_over"]["description"]}")
        break

    # Print the room description
    if current_room and current_room != previous_room:
        print(current_room["description"])
        print("bonus action options: ")
        for bonus in bonus_actions:
            print(f"{bonus}")
        print("or none to continue...")
        bonus_action = input("> ").lower()
        if bonus_action in bonus_actions:
            perform_bonus_action(current_room, bonus_action)

    previous_room = current_room

    print("options: ")
    if "actions" in current_room and current_room["actions"]:
        for action in current_room["actions"]:
            print(f"{action}")
    else:        
        for exit in current_room["exits"]:
            print(f"go {exit}")
        


    # Get player choice
    choice = get_player_choice(current_room)

    # Handle player movement
    if choice.startswith("go"):
        direction = choice.split()[1]
        if direction in current_room["exits"]:
            current_room = rooms[current_room["exits"][direction]]
        else:
            print("You cannot go that way.")
    elif choice.lower() in current_room["actions"]:
        action = current_room["actions"].pop(choice.lower(), None)
        auto_success = current_room == "dragon_chamber" and "Sword of Destiny" in player.items
        run_action(current_room, action, auto_success)
   
        

    if player["hp"] <= 0 or player["dead"]:
        print("Seems like your previous battle was also your last one, you're not worthy of the Sword of Destiny...")
        player["dead"] = True
        break
