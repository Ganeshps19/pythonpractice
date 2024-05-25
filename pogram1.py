import random

class Player:
    def __init__(self, name, health=100, attack=10, defense=5):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.inventory = []

    def take_damage(self, damage):
        self.health -= max(0, damage - self.defense)
        if self.health <= 0:
            print(f"{self.name} has been defeated!")

    def heal(self, amount):
        self.health += amount

    def attack_enemy(self, enemy):
        damage = random.randint(self.attack // 2, self.attack)
        print(f"{self.name} attacks {enemy.name} for {damage} damage!")
        enemy.take_damage(damage)

    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"{self.name} picks up {item}.")

    def __str__(self):
        return f"Name: {self.name}, Health: {self.health}, Attack: {self.attack}, Defense: {self.defense}, Inventory: {self.inventory}"

class Enemy:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has been defeated!")

    def attack_player(self, player):
        damage = random.randint(1, self.attack)
        print(f"{self.name} attacks {player.name} for {damage} damage!")
        player.take_damage(damage)

    def __str__(self):
        return f"Name: {self.name}, Health: {self.health}, Attack: {self.attack}"

class Room:
    def __init__(self, name, description, enemies=[], items=[]):
        self.name = name
        self.description = description
        self.enemies = enemies
        self.items = items

    def __str__(self):
        return f"Name: {self.name}, Description: {self.description}, Enemies: {self.enemies}, Items: {self.items}"

def main():
    player_name = input("Enter your name: ")
    player = Player(player_name)

    rooms = [
        Room("Room 1", "A dark room with a single door."),
        Room("Room 2", "You see a chest in the corner.", [Enemy("Goblin", 20, 5)]),
        Room("Room 3", "A long corridor stretches before you.", [Enemy("Skeleton", 15, 8)]),
        Room("Room 4", "You find yourself in a small chamber.", [Enemy("Orc", 30, 10)], ["Potion"]),
        Room("Room 5", "You see a treasure chest in the center of the room.", [], ["Sword"]),
        Room("Final Room", "The final showdown awaits!", [Enemy("Dragon", 50, 15)])
    ]

    current_room_index = 0
    while True:
        current_room = rooms[current_room_index]
        print("\n" + "="*20)
        print(f"You are in {current_room.name}: {current_room.description}")
        print("-"*20)
        print(player)
        if current_room.enemies:
            print("Enemies in the room:")
            for enemy in current_room.enemies:
                print(enemy)
        if current_room.items:
            print("Items in the room:")
            for item in current_room.items:
                print(item)
        print("="*20)

        action = input("What do you want to do? (explore / fight / move / quit): ").lower()
        if action == "quit":
            print("Thanks for playing!")
            break
        elif action == "explore":
            print("You explore the room...")
            if current_room.items:
                for item in current_room.items:
                    player.add_to_inventory(item)
                current_room.items = []
            else:
                print("You find nothing of interest.")
        elif action == "fight":
            if current_room.enemies:
                for enemy in current_room.enemies:
                    while enemy.health > 0 and player.health > 0:
                        player.attack_enemy(enemy)
                        if enemy.health > 0:
                            enemy.attack_player(player)
            else:
                print("There are no enemies to fight.")
        elif action == "move":
            if current_room_index < len(rooms) - 1:
                current_room_index += 1
            else:
                print("You have reached the end of the dungeon!")
                break
        else:
            print("Invalid action. Try again.")

if __name__ == "__main__":
    main()
