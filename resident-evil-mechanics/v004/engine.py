import os

# Global databases acting as game configuration data registries
environment_data = {
    'secret_door_locked': True, 
    'window_blocked': False, 
    'weapons_arsenal': ['magnum', 'flamethrower', 'grenade-launcher', 'submachine-gun'],
    'generator_power_on': False
}

scene_items = {
    'green_herb': 3,
    'magnum_ammo': 20
}

item_properties = {
    'green_herb': {
        'healing_power': 40
    }
}

character_data = {
    'leon': {
        'defense': 0.9,
        'max_health': 100
    },
    'claire': {
        'defense': 1,
        'max_health': 100
    }, 
    'zombie': {
        'attack': 10,
        'max_health': 100
    }
}

# Real-time tactical tracking of enemy proximity inside the engine
zombies_in_room = {
    'zombie_1': 3,
    'zombie_2': 5,
    'zombie_3': 10
}


class Environment:
    def __init__(self, environment_data, scene_items):
        self.environment_data = environment_data
        self.scene_items = scene_items

    def unlock_secret_door(self):
        self.environment_data['secret_door_locked'] = False

    def collect_weapon(self, weapon):
        if weapon in self.environment_data['weapons_arsenal']:
            self.environment_data['weapons_arsenal'].remove(weapon)
            return weapon
        else:
            print('Weapon not available.')
            _ = input()
            return None
    
    def block_window(self):
        self.environment_data['window_blocked'] = True

    def turn_on_generator(self):
        self.environment_data['generator_power_on'] = True

    def extract_item(self, item):
        if item in self.scene_items:
            if self.scene_items[item] > 0:
                self.scene_items[item] -= 1
                return item
            else:
                print(f'No more {item} available in this room.')
                return None


class Player:
    def __init__(self, environment, character_data, item_properties):
        self.environment = environment
        self.character_data = character_data
        self.item_properties = item_properties
        self.inventory = []

    def collect_weapon(self, weapon):
        weapon_collected = self.environment.collect_weapon(weapon)
        if weapon_collected:
            self.inventory.append(weapon_collected)
            print(f'{weapon_collected.replace("-", " ").capitalize()} collected.')
            _ = input()
    
    def collect_item(self, item):
        item_collected = self.environment.extract_item(item)
        if item_collected:
            self.inventory.append(item_collected)

    def turn_on_generator(self):
        self.environment.turn_on_generator()

    def take_damage(self, damage):
        multiplier_factor = self.character_data[self.name]['defense']
        self.health -= damage * multiplier_factor

    def use_herb(self, herb):
        if herb in self.inventory:
            self.inventory.remove(herb)
            self.health += self.item_properties[herb]['healing_power']
        if self.health > self.character_data[self.name]['max_health']:
            self.health = self.character_data[self.name]['max_health']


class Leon(Player):
    def __init__(self, environment):
        super().__init__(environment, character_data, item_properties)
        self.allowed_weapons = {'magnum', 'flamethrower'}
        self.name = 'leon'
        self.health = character_data[self.name]['max_health']

    def collect_weapon(self, weapon):
        if weapon in self.allowed_weapons:
            super().collect_weapon(weapon)
        else:
            print(f'{self.name.capitalize()} does not know how to use this weapon.')
            _ = input()

    def unlock_door(self):
        self.environment.unlock_secret_door()

    def block_window(self):
        self.environment.block_window()


class Claire(Player):
    def __init__(self, environment):
        super().__init__(environment, character_data, item_properties)
        self.allowed_weapons = {'grenade-launcher', 'submachine-gun'}
        self.name = 'claire'
        self.health = character_data[self.name]['max_health']

    def collect_weapon(self, weapon):
        if weapon in self.allowed_weapons:
            super().collect_weapon(weapon)
        else:
            print(f'{self.name.capitalize()} does not know how to use this weapon.')

    def check_door(self):
        if self.environment.environment_data['secret_door_locked']:
            print('Claire could not enter the secret room.')
        else:
            print('Claire entered the secret room.')
 
    def pass_through_corridor(self):
        if self.environment.environment_data['window_blocked']:
            print('Claire passed through the corridor without any problems.')
        else:
            print('Claire was attacked by a zombie from the window!')

    def explore_generator_room(self):
        if self.environment.environment_data['generator_power_on']:
            print(f'{self.name.capitalize()} passed through safely.')
        else:
            print(f'The room is too dark. {self.name.capitalize()} fell into a pit!')


class Zombie:
    def __init__(self, character_data):
        self.health = character_data['zombie']['max_health']

    def attack(self, target, damage):
        target.take_damage(damage)


def update_screen():
    # Cross-platform screen clearing (Windows: cls, Mac/Linux: clear)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Health: {leon.health}/{character_data['leon']['max_health']}\n")
    print(f"There are {len(zombies_in_room)} zombies in the room.")
    print("Zombies distance:")
    for zombie, distance in zombies_in_room.items():
        print(f" - {zombie.replace('_', ' ').capitalize()}: {distance}m")
    print('\n')
    

# Object Initialization
environment = Environment(environment_data, scene_items)
leon = Leon(environment)
claire = Claire(environment)
zombie = Zombie(character_data)


def view_available_weapons(environment):
    while True:
        update_screen()
        print('Weapons Arsenal:')
        print(environment.environment_data['weapons_arsenal'])
        print('\n')
        
        while True:
            try:
                weapon_action = int(input('1 - Take weapon | 2 - Go back: '))
            except ValueError:
                print('Invalid option. Please enter a number.')
            else:
                if weapon_action in [1, 2]:
                    break
                else:
                    print('Invalid option.')
                    
        if weapon_action == 1:
            update_screen()
            for i, weapon in enumerate(environment.environment_data['weapons_arsenal']):
                print(f"{i + 1} - {weapon.replace('-', ' ').capitalize()}")
            print('\n')
            
            while True:
                try:
                    weapon_choice = int(input('Which weapon do you want to take? (0 to go back): '))
                except ValueError:
                    print('Invalid option. Please enter a number.')
                else:
                    break
                    
            if weapon_choice == 0:
                break
            elif 1 <= weapon_choice <= len(environment.environment_data['weapons_arsenal']):
                weapon = environment.environment_data['weapons_arsenal'][weapon_choice - 1]
                leon.collect_weapon(weapon)
            else:
                print('Invalid option.')
                input()
        else:
            break


# ==============================================================================
# MAIN GAME EXECUTION
# ==============================================================================
if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Leon entered the secret room...\n')
    input('Press Enter to continue...')
    
    # Leon's Interactive Turn Loop
    while True:
        update_screen()
        print('Actions:')
        print('1 - Check available weapons in the arsenal')
        print('2 - Check available items in the room')
        print('3 - Shoot the zombie')
        print('4 - Use item')
        print('5 - Do nothing')
        print('6 - Leave the room')
        print('\n')
        
        while True:
            try:
                action = int(input('What do you want to do? '))
                update_screen()
            except ValueError:
                print('Invalid action. Please enter a number.')
            else:
                if 1 <= action <= 6:
                    break
                else:
                    print('Invalid action. Select a valid menu option.')
                    continue
                    
        if action == 1:
            view_available_weapons(environment)            
        elif action == 2:
            pass
        elif action == 3:
            pass
        elif action == 4:
            pass
        elif action == 5:
            pass
        elif action == 6:
            break
