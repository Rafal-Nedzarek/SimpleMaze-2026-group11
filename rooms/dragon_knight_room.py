
import tkinter as tk
import math
import time


# ============================================================
# CONFIGURATION
# ============================================================

WIDTH = 900
HEIGHT = 600
PLAYER_SPEED = 5
MONSTER_SPEED = 1.5
BOSS_SPEED = 1.0
PLAYER_MAX_HEALTH = 10

# Add new keys here whenever you introduce another required key.
# The player must have EVERY key in this list.
REQUIRED_KEYS = [
    "warp key",
    "key shard",
    "crooked key",
]

SWORD_NAME = "Sword"
BUFF_NAME = "Dark Sun Buff"


# ============================================================
# INVENTORY AND GAME STATE
# ============================================================

def normalize_item(item):
    return str(item).strip().lower()


def has_required_keys(state):
    inventory = {
        normalize_item(item)
        for item in state.get("inventory", [])
    }

    return all(
        normalize_item(key) in inventory
        for key in REQUIRED_KEYS
    )


def show_inventory(state):
    print("\n========== INVENTORY ==========")

    inventory = state.setdefault("inventory", [])

    if not inventory:
        print("Your inventory is empty.")
    else:
        for item in inventory:
            print(f"- {item}")

    print("===============================")


def add_item(state, item):
    inventory = state.setdefault("inventory", [])

    if normalize_item(item) not in {
        normalize_item(existing) for existing in inventory
    }:
        inventory.append(item)


def use_dark_sun_buff(state):
    inventory = state.setdefault("inventory", [])

    for item in inventory:
        if normalize_item(item) == normalize_item(BUFF_NAME):
            inventory.remove(item)

            state["health"] = state.get("health", PLAYER_MAX_HEALTH) + 2

            return True

    return False


# ============================================================
# MAIN ROOM
# ============================================================

def enterDragonKnightRoom(state):
    """
    Main entry point for Dragon Knight Room.

    Controls:
        W, A, S, D or arrow keys - Move
        SPACE                    - Attack with sword
        E                        - Pick up nearby items
        I                        - Open / close inventory
        B                        - Use Dark Sun Buff
    """

    state.setdefault("inventory", [])
    state.setdefault("health", PLAYER_MAX_HEALTH)
    state.setdefault("room_states", {})

    room_state = state["room_states"].setdefault(
        "dragon_knight_room",
        {
            "completed": False,
            "sword_collected": False,
            "buff_collected": False,
        },
    )

    # --------------------------------------------------------
    # CHECK THE REQUIRED KEYS
    # --------------------------------------------------------

    if not has_required_keys(state):
        missing_keys = [
            key for key in REQUIRED_KEYS
            if normalize_item(key) not in {
                normalize_item(item)
                for item in state["inventory"]
            }
        ]

        print("\n======================================")
        print("       THE DRAGON'S DOOR IS LOCKED")
        print("======================================")
        print("You need all the following keys:")

        for key in missing_keys:
            print(f"- {key}")

        print("\nFind the missing keys in other rooms first.")
        return "corridor"

    if room_state["completed"]:
        print("\nYou have already defeated the Dragon Knight.")
        return "lobby"

    # --------------------------------------------------------
    # GAME WINDOW
    # --------------------------------------------------------

    root = tk.Tk()
    root.title("Dragon Knight Room")
    root.resizable(False, False)

    canvas = tk.Canvas(
        root,
        width=WIDTH,
        height=HEIGHT,
        bg="#171323",
        highlightthickness=0,
    )
    canvas.pack()

    # --------------------------------------------------------
    # GAME VARIABLES
    # --------------------------------------------------------

    player = {
        "x": 120,
        "y": 300,
        "radius": 17,
        "speed": PLAYER_SPEED,
    }

    keys_pressed = set()

    game = {
        "running": True,
        "inventory_open": False,
        "message": "Find the sword! Defeat the Dragon!",
        "attack_until": 0,
        "attack_cooldown": 0,
        "damage_cooldown": 0,
        "exit": "corridor",
    }

    enemies = [
        {
            "x": 430,
            "y": 150,
            "health": 2,
            "max_health": 2,
            "speed": MONSTER_SPEED,
            "radius": 15,
            "type": "monster",
            "alive": True,
        },
        {
            "x": 540,
            "y": 430,
            "health": 2,
            "max_health": 2,
            "speed": MONSTER_SPEED,
            "radius": 15,
            "type": "monster",
            "alive": True,
        },
        {
            "x": 680,
            "y": 170,
            "health": 2,
            "max_health": 2,
            "speed": MONSTER_SPEED,
            "radius": 15,
            "type": "monster",
            "alive": True,
        },
        {
            "x": 730,
            "y": 350,
            "health": 8,
            "max_health": 8,
            "speed": BOSS_SPEED,
            "radius": 30,
            "type": "boss",
            "alive": True,
        },
    ]

    sword = {
        "x": 220,
        "y": 300,
        "collected": room_state["sword_collected"],
    }

    buff = {
        "x": 300,
        "y": 300,
        "collected": room_state["buff_collected"],
    }

    # If the player already has a sword, it is equipped.
    sword["collected"] = sword["collected"] or any(
        normalize_item(item) == normalize_item(SWORD_NAME)
        for item in state["inventory"]
    )

    # --------------------------------------------------------
    # HEALTH
    # --------------------------------------------------------

    def get_health():
        return state.get("health", PLAYER_MAX_HEALTH)

    def set_health(value):
        state["health"] = max(0, value)

    # --------------------------------------------------------
    # DRAWING
    # --------------------------------------------------------

    def draw_room():
        canvas.delete("all")

        # Background floor
        canvas.create_rectangle(
            0, 0, WIDTH, HEIGHT,
            fill="#252036",
            outline="",
        )

        # Floor decorations
        for x in range(40, WIDTH, 80):
            canvas.create_line(
                x, 0, x, HEIGHT,
                fill="#302940",
                width=1,
            )

        for y in range(40, HEIGHT, 80):
            canvas.create_line(
                0, y, WIDTH, y,
                fill="#302940",
                width=1,
            )

        # Room walls
        canvas.create_rectangle(
            5, 5, WIDTH - 5, HEIGHT - 5,
            outline="#a18a60",
            width=8,
        )

        # Exit door
        canvas.create_rectangle(
            20, 250, 65, 350,
            fill="#654321",
            outline="#d5b56b",
            width=3,
        )
        canvas.create_text(
            43, 235,
            text="EXIT",
            fill="white",
            font=("Arial", 10, "bold"),
        )

        # Sword
        if not sword["collected"]:
            sx, sy = sword["x"], sword["y"]

            canvas.create_line(
                sx, sy - 15,
                sx, sy + 15,
                fill="#eeeeee",
                width=6,
            )
            canvas.create_line(
                sx - 9, sy + 5,
                sx + 9, sy + 5,
                fill="#b58b42",
                width=4,
            )
            canvas.create_text(
                sx, sy + 28,
                text="SWORD [E]",
                fill="white",
                font=("Arial", 9, "bold"),
            )

        # Dark Sun Buff
        if not buff["collected"]:
            bx, by = buff["x"], buff["y"]

            canvas.create_oval(
                bx - 12, by - 12,
                bx + 12, by + 12,
                fill="#ffb000",
                outline="#fff2a0",
                width=3,
            )
            canvas.create_text(
                bx, by + 27,
                text="DARK SUN BUFF [E]",
                fill="#ffd76a",
                font=("Arial", 9, "bold"),
            )

        # Enemies
        for enemy in enemies:
            if not enemy["alive"]:
                continue

            x = enemy["x"]
            y = enemy["y"]
            radius = enemy["radius"]

            if enemy["type"] == "boss":
                color = "#a51f36"
                label = "DRAGON"
            else:
                color = "#527d42"
                label = "MONSTER"

            canvas.create_oval(
                x - radius,
                y - radius,
                x + radius,
                y + radius,
                fill=color,
                outline="#f2d5a0",
                width=2,
            )

            canvas.create_oval(
                x - radius / 2,
                y - 5,
                x - 3,
                y,
                fill="yellow",
                outline="",
            )
            canvas.create_oval(
                x + 3,
                y - 5,
                x + radius / 2,
                y,
                fill="yellow",
                outline="",
            )

            canvas.create_text(
                x,
                y - radius - 15,
                text=f"{enemy['health']}/{enemy['max_health']}",
                fill="white",
                font=("Arial", 9, "bold"),
            )

            if enemy["type"] == "boss":
                canvas.create_text(
                    x,
                    y + radius + 13,
                    text=label,
                    fill="#ff7777",
                    font=("Arial", 10, "bold"),
                )

        # Player
        px = player["x"]
        py = player["y"]

        canvas.create_oval(
            px - player["radius"],
            py - player["radius"],
            px + player["radius"],
            py + player["radius"],
            fill="#3989e8",
            outline="white",
            width=2,
        )

        canvas.create_oval(
            px - 7, py - 7,
            px - 2, py - 2,
            fill="white",
            outline="",
        )
        canvas.create_oval(
            px + 2, py - 7,
            px + 7, py - 2,
            fill="white",
            outline="",
        )

        # Attack effect
        if time.time() < game["attack_until"]:
            canvas.create_oval(
                px - 48, py - 48,
                px + 48, py + 48,
                outline="#fff3a0",
                width=4,
            )

        # HUD
        canvas.create_rectangle(
            10, 10, 280, 82,
            fill="#100e19",
            outline="#a18a60",
            width=2,
        )

        canvas.create_text(
            25, 25,
            anchor="w",
            text=f"HEALTH: {get_health()}",
            fill="#ff7777",
            font=("Arial", 13, "bold"),
        )

        sword_status = "YES" if sword["collected"] else "NO"

        canvas.create_text(
            25, 49,
            anchor="w",
            text=f"SWORD: {sword_status}",
            fill="white",
            font=("Arial", 11),
        )

        canvas.create_text(
            25, 67,
            anchor="w",
            text="I: Inventory   B: Use Buff   E: Pick up",
            fill="#d5d0e0",
            font=("Arial", 9),
        )

        # Message
        canvas.create_rectangle(
            290, 10, 890, 48,
            fill="#100e19",
            outline="#a18a60",
        )

        canvas.create_text(
            590, 29,
            text=game["message"],
            fill="white",
            font=("Arial", 11, "bold"),
        )

        # Inventory overlay
        if game["inventory_open"]:
            canvas.create_rectangle(
                240, 110, 660, 490,
                fill="#100e19",
                outline="#e2c27a",
                width=4,
            )

            canvas.create_text(
                450, 145,
                text="YOUR GLOBAL INVENTORY",
                fill="#ffd76a",
                font=("Arial", 18, "bold"),
            )

            inventory = state.get("inventory", [])

            if not inventory:
                canvas.create_text(
                    450, 210,
                    text="Your inventory is empty.",
                    fill="white",
                    font=("Arial", 13),
                )
            else:
                for index, item in enumerate(inventory):
                    canvas.create_text(
                        290,
                        190 + index * 27,
                        anchor="w",
                        text=f"- {item}",
                        fill="white",
                        font=("Arial", 12),
                    )

            canvas.create_text(
                450, 455,
                text="Press I to close inventory",
                fill="#d5d0e0",
                font=("Arial", 10),
            )

    # --------------------------------------------------------
    # PICK UP ITEMS
    # --------------------------------------------------------

    def pick_up_item():
        px = player["x"]
        py = player["y"]

        if not sword["collected"]:
            distance = math.hypot(
                px - sword["x"],
                py - sword["y"],
            )

            if distance < 45:
                sword["collected"] = True
                room_state["sword_collected"] = True
                add_item(state, SWORD_NAME)

                game["message"] = (
                    "You picked up the sword! Press SPACE to attack."
                )
                return

        if not buff["collected"]:
            distance = math.hypot(
                px - buff["x"],
                py - buff["y"],
            )

            if distance < 45:
                buff["collected"] = True
                room_state["buff_collected"] = True
                add_item(state, BUFF_NAME)

                game["message"] = (
                    "Dark Sun Buff collected! Press B to use it."
                )

    # --------------------------------------------------------
    # ATTACK
    # --------------------------------------------------------

    def attack():
        if not sword["collected"]:
            game["message"] = "You need to pick up the sword first!"
            return

        now = time.time()

        if now - game["attack_cooldown"] < 0.4:
            return

        game["attack_cooldown"] = now
        game["attack_until"] = now + 0.18

        hit_something = False

        for enemy in enemies:
            if not enemy["alive"]:
                continue

            distance = math.hypot(
                player["x"] - enemy["x"],
                player["y"] - enemy["y"],
            )

            if distance < player["radius"] + enemy["radius"] + 38:
                enemy["health"] -= 1
                hit_something = True

                if enemy["health"] <= 0:
                    enemy["alive"] = False

                    if enemy["type"] == "boss":
                        game["message"] = (
                            "THE DRAGON HAS BEEN DEFEATED!"
                        )
                    else:
                        game["message"] = (
                            "You defeated a monster!"
                        )

        if not hit_something:
            game["message"] = "Your sword missed!"

    # --------------------------------------------------------
    # USE DARK SUN BUFF
    # --------------------------------------------------------

    def use_buff():
        if use_dark_sun_buff(state):
            game["message"] = (
                "Dark Sun Buff used! You gained 2 health!"
            )
        else:
            game["message"] = (
                "You do not have a Dark Sun Buff!"
            )

    # --------------------------------------------------------
    # ENEMY MOVEMENT
    # --------------------------------------------------------

    def move_enemies():
        px = player["x"]
        py = player["y"]

        for enemy in enemies:
            if not enemy["alive"]:
                continue

            dx = px - enemy["x"]
            dy = py - enemy["y"]

            distance = math.hypot(dx, dy)

            if distance > 1:
                enemy["x"] += (
                    dx / distance
                ) * enemy["speed"]

                enemy["y"] += (
                    dy / distance
                ) * enemy["speed"]

            # Keep enemies inside the room.
            enemy["x"] = max(35, min(WIDTH - 35, enemy["x"]))
            enemy["y"] = max(35, min(HEIGHT - 35, enemy["y"]))

    # --------------------------------------------------------
    # PLAYER DAMAGE
    # --------------------------------------------------------

    def check_enemy_collision():
        now = time.time()

        if now - game["damage_cooldown"] < 1:
            return

        for enemy in enemies:
            if not enemy["alive"]:
                continue

            distance = math.hypot(
                player["x"] - enemy["x"],
                player["y"] - enemy["y"],
            )

            if distance < player["radius"] + enemy["radius"]:
                set_health(get_health() - 1)
                game["damage_cooldown"] = now
                game["message"] = "An enemy hit you! You lost 1 health."
                break

        if get_health() <= 0:
            game["message"] = "You have been defeated!"
            game["running"] = False
            game["exit"] = "corridor"

    # --------------------------------------------------------
    # KEYBOARD CONTROLS
    # --------------------------------------------------------

    def key_down(event):
        key = event.keysym.lower()

        keys_pressed.add(key)

        if key == "i":
            game["inventory_open"] = not game["inventory_open"]

        elif key == "e":
            pick_up_item()

        elif key == "space":
            attack()

        elif key == "b":
            use_buff()

        elif key == "escape":
            game["running"] = False
            game["exit"] = "corridor"

    def key_up(event):
        key = event.keysym.lower()
        keys_pressed.discard(key)

    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    # --------------------------------------------------------
    # PLAYER MOVEMENT
    # --------------------------------------------------------

    def move_player():
        if game["inventory_open"]:
            return

        dx = 0
        dy = 0

        if "w" in keys_pressed or "up" in keys_pressed:
            dy -= 1

        if "s" in keys_pressed or "down" in keys_pressed:
            dy += 1

        if "a" in keys_pressed or "left" in keys_pressed:
            dx -= 1

        if "d" in keys_pressed or "right" in keys_pressed:
            dx += 1

        if dx != 0 and dy != 0:
            dx *= 0.707
            dy *= 0.707

        player["x"] += dx * player["speed"]
        player["y"] += dy * player["speed"]

        player["x"] = max(
            30,
            min(WIDTH - 30, player["x"]),
        )

        player["y"] = max(
            30,
            min(HEIGHT - 30, player["y"]),
        )

    # --------------------------------------------------------
    # GAME LOOP
    # --------------------------------------------------------

    def game_loop():
        if not game["running"]:
            root.destroy()
            return

        if not game["inventory_open"]:
            move_player()
            move_enemies()
            check_enemy_collision()

        # All enemies defeated?
        if not any(enemy["alive"] for enemy in enemies):
            game["message"] = (
                "Victory! You defeated the Dragon Knight!"
            )

            room_state["completed"] = True
            state.setdefault("completed", {})
            state["completed"]["dragon_knight_room"] = True

            game["exit"] = "lobby"
            game["running"] = False

            draw_room()
            root.after(1200, root.destroy)
            return

        draw_room()

        root.after(30, game_loop)

    # --------------------------------------------------------
    # WINDOW CLOSE
    # --------------------------------------------------------

    def close_window():
        game["running"] = False
        game["exit"] = "corridor"
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", close_window)

    # --------------------------------------------------------
    # START GAME
    # --------------------------------------------------------

    game_loop()
    root.mainloop()

    return game["exit"]
