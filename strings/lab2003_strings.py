DOOR_LOCKED = ("\nThe door to Lab 2003 is locked.\n"
               "The door looks robust and high-tech. You'll need a special key...")
DOOR_UNLOCKED = "\nYou insert the lab2003 key into the lock and turn it."
DOOR_LOCKED_END = "You can't unlock the door anymore. The small screen next to the lock displays ERROR."
ENTER_ROOM = "As you enter the room, you're immediately enveloped with darkness."
RE_ENTER_ROOM = "You re-enter Lab 2003."
LIGHTS_OFF = "It's so dark in here that you can't see anything. Better turn the lights on first..."
LIGHTS_ON = ("You're dazzled by the bright lights. After a brief moment, your eyesight recovers.\n"
             "Time to take a look around...")
LOOK_AROUND = ("You look around the room and notice one desk placed exactly in the middle.\n"
              "Around the desk a group of small, tracked robots are busy placing candles around the place.\n"
              "It seems they're preparing some sort of ritual. Your attention moves onto the desk.\n"
              "You notice a hooded person sitting at the desk...")
NEW_ACTIONS = "- New action available: approach the person"
ROOM_SPECIFIC_COMMANDS = {
    "lights_on": "- lights on                : Turn on the lights.",
    "approach": "- approach the person                : See if the person is okay."
}
HANDLE_GO = {
    "valid": "You open the door and step back into the lobby.",
    "invalid": "You can't go to '{destination}' from here."
}
BOSS_FIGHT = {
    "enemy_attacks": "The enemy attacks you!",
    "player_punch": "You punch the enemy with your fist. Doesn't seem to do much...",
    "health_bars": ("------------\n"
                  "Boss HP: {boss_health}\n"
                  "Your HP: {player_health}\n"
                  "------------\n"),
    "player_lost": ("You've been defeated! You use your last strength to reach into your pocket.\n"
                      "You pop a paracetamol pill to revive yourself. After a while you wake up in the lobby."),
    "available_actions": "What do you do!?\nAvailable actions: punch, use <item>, rage quit\n> ",
    "player_heal": "You heal {heal} health points!",
    "item_attack": "Critical hit! Your enemy receives {special_weapon_dmg} damage!",
    "item_removed": "{item} has been removed from your inventory.",
    "item_useless": "This item is of no use here.",
    "item_not_found": "Item not found.",
    "rage_quit": ("You smash your keyboard repeatedly and then silently stare into the distance.\n"
                      "Take a deep breath. Better luck next time!"),
    "unknown_command": "Uh oh, you made a typo! Unknown command!",
    "boss_defeated": ("\nThe hooded figure falls to the ground.\n"
              "You can hear all their support systems grinding down to a halt.\n"
              "Next to the lifeless, robotic body you see a peculiar key.\n"
              "A label on the keychain reads \"EXIT\"...\n"
              "You head back to the lobby.")
}
BOSS_CONVERSATION = {
    "boss_desc":("You approach the hooded person. You notice they're wearing long, crimson robes.\n"
              "You can't clearly see their face, but you see some cables sticking out from beneath the robes.\n"
              "The pair of eyes glowing under the hood turns towards you. You hear what sounds like a question:"),
    "boss_question": "62656e206a696a2076696a616e64206f6620767269656e643f\n> ",
    "answer_correct": ("The person nods their hooded head. You could swear you hear the buzzing of servo motors under those robes.\n"
                  "The person extends their robotic hand with a key, you take it in silence.\n"
                  "Not sure what to make of all that, you quickly go back to the lobby."),
    "answer_wrong": ("Looks like the person didn't like your answer. They stand up and grab a two-handed axe that was hidden among the lab's hardware.\n"
              "The eyes under the hood glow ominously, the servo motors under the robes are abuzz. They're preparing to attack!")
}
