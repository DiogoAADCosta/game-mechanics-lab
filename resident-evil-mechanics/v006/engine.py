import os
import random

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

    def extract_item(self, item, quantity):
        if item in self.scene_items:
            if self.scene_items[item] > 0:
                self.scene_items[item] -= quantity
                if self.scene_items[item] == 0:
                    del self.scene_items[item]
                return item
            else:
                print(f'No more {item} available.')
                return None


class Player:
    def __init__(self, environment, character_data, item_properties, weapon_properties):
        self.environment = environment
        self.character_data = character_data
        self.item_properties = item_properties
        self.weapon_properties = weapon_properties
        self.inventory = {}
        self.equipped_weapon = ''  # State placeholder tracking active equipment

    def collect_weapon(self, weapon):
        weapon_collected = self.environment.collect_weapon(weapon)
        if weapon_collected:
            self.inventory[weapon_collected] = 1
            print(f'{weapon_collected.replace("-", " ").capitalize()} collected.')
            _ = input()
    
    def collect_item(self, item, quantity):
        item_collected = self.environment.extract_item(item, quantity)
        if item_collected:
            if item_collected not in self.inventory:
                self.inventory[item_collected] = quantity
            else:
                self.inventory[item_collected] += quantity

    def turn_on_generator(self):
        self.environment.turn_on_generator()

    def take_damage(self, damage):
        multiplier_factor = self.character_data[self.name]['defense']
        self.health -= damage * multiplier_factor
        if self.health < 0:
            self.health = 0
            
    def use_herb(self, herb):
        # Version 6 Bugfix: Completely removed .remove() inheritance remnants to process dicts securely
        if herb in self.inventory:
            self.inventory[herb] -= 1
            if self.inventory[herb] == 0:
                del self.inventory[herb]
            self.health += self.item_properties[herb]['healing_power']
        if self.health > self.character_data[self.name]['max_health']:
            self.health = self.character_data[self.name]['max_health']

    def shoot(self):
        if self.weapon_properties[self.equipped_weapon]['ammo_count'] == 0:
            print(f'{self.equipped_weapon.replace("-", " ").capitalize()} is out of ammo.')
            input()
        else:
            zombie_list = [zombie for zombie in zombies_in_room]
            update_screen()
            for i, zombie in enumerate(zombies_in_room):
                print(f'{i + 1} - {zombie.replace("_", " ").capitalize()}')
            
            while True:
                try:
                    target_index = int(input('Shoot at whom? '))
                    if target_index not in list(range(1, len(zombies_in_room) + 1)):
                        print('Invalid target option.')
                        continue
                except ValueError:
                    print('Invalid option.')
                else:
                    break
            
            # Probability-based Critical Damage Calculation Mechanics
            critical_coefficient = random.random()
            weapon_entry = self.weapon_properties[self.equipped_weapon]
            is_critical = critical_coefficient <= weapon_entry['critical_chance'][0]
            critical_modifier = weapon_entry['critical_chance'][1] if is_critical else 1
            
            total_damage = weapon_entry['base_damage'] * critical_modifier
            target_zombie = zombies_in_room[zombie_list[target_index - 1]]
            
            target_zombie.take_damage(total_damage)
            self.weapon_properties[self.equipped_weapon]['ammo_count'] -= 1

    def reload_weapon(self, forced_ammo=''):
        if not self.inventory:
            print('Inventory is empty.')
            input()
        elif not self.equipped_weapon:
            print('No weapon equipped.')
            input()
        elif self.weapon_properties[self.equipped_weapon]['ammo_type'] not in self.inventory and forced_ammo == '':
            print(f"You don't have ammo for {self.equipped_weapon.replace('-', ' ')} in your inventory.")
            input()
        elif forced_ammo != self.weapon_properties[self.equipped_weapon]['ammo_type'] and forced_ammo != '':
            for weapon in self.weapon_properties:
                if self.weapon_properties[weapon]['ammo_type'] == forced_ammo:
                    print(f"You must equip the {weapon} to reload it with {forced_ammo.replace('_', ' ')}.")
                    input()
                    break
        else:
            has_ammo = False
            ammo_key = self.weapon_properties[self.equipped_weapon]['ammo_type']
            if ammo_key in self.inventory:
                current_ammo = self.weapon_properties[self.equipped_weapon]['ammo_count']
                reload_capacity = self.weapon_properties[self.equipped_weapon]['max_ammo'] - current_ammo
                
                if reload_capacity == 0:
                    print('Weapon already fully loaded.')
                    input()
                    return
                if self.inventory[ammo_key] <= reload_capacity:
                    reload_capacity = self.inventory[ammo_key]
                    
                self.inventory[ammo_key] -= reload_capacity
                self.weapon_properties[self.equipped_weapon]['ammo_count'] += reload_capacity   
                if self.inventory[ammo_key] == 0:
                    del self.inventory[ammo_key]
                has_ammo = True 

            if not has_ammo:
                print('You do not possess the required ammunition.')
                input()
    
    def push_zombie(self, zombie_key):
        target_zombie = zombies_in_room[zombie_key]
        push_power = self.character_data[self.name]['push_force']
        target_zombie.get_pushed(push_power)


class Leon(Player):
    def __init__(self, environment):
        super().__init__(environment, character_data, item_properties, weapon_properties)
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
        super().__init__(environment, character_data, item_properties, weapon_properties)
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
    def __init__(self, name, character_data, distance):
        self.health = character_data['zombie']['max_health']
        self.name = name
        self.character_data = character_data
        self.distance = distance
        self.has_not_bitten = True  # Handles turn-based biting cooldown mechanics

    def attack(self, target, damage):
        target.take_damage(damage)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            update_screen()
            self.die()
    
    def die(self):
        del zombies_in_room[self.name]
        print(f'{self.name.replace("_", " ").capitalize()} has been eliminated.')
        input()

    def walk(self):
        if self.distance > 0:
            self.distance -= self.character_data['zombie']['step_size']
        else:
            self.distance = 0

    def bite(self):
        if self.has_not_bitten:
            print(f'{self.name.replace("_", " ").capitalize()} bit you!!!')
            character.take_damage(self.character_data['zombie']['attack'])
            input()
            update_screen()
        self.has_not_bitten = not self.has_not_bitten
    
    def get_pushed(self, force):
        self.distance = force


def update_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Health: {character.health}/{character_data[character.name]['max_health']}          ", end='')
    
    # Dynamic ECG/Vitals Rendering Engine utilizing ANSI Escape Codes
    if character.health > character_data[character.name]['max_health'] * 0.7:
        condition = 'FINE'
        ecg_line = '^-v-^-v-^-v-^'
    elif character.health > character_data[character.name]['max_health'] * 0.3:
        condition = 'CAUTION'
        ecg_line = '^-v^-v^-v^-v^'
    elif character.health > 0:
        condition = 'DANGER'
        ecg_line = '^v^v^v^v^v^v^'
    else:
        condition = 'DEATH'
        ecg_line = '-------------'
        
    print(f"{status_colors[condition]}{ecg_line + condition + ecg_line}{status_colors['RESET']}")
    
    if character.equipped_weapon:
        print(f"{character.equipped_weapon.replace('-', ' ').capitalize()}: {character.weapon_properties[character.equipped_weapon]['ammo_count']}/", end='')
        try:
            ammo_in_bag = character.inventory[character.weapon_properties[character.equipped_weapon]['ammo_type']]
        except KeyError:
            ammo_in_bag = 0
        finally:
            print(f"{ammo_in_bag}")
    print('\n')
    
    print(f"There are {len(zombies_in_room)} zombies in the room.")
    if len(zombies_in_room) > 0:
        print("Zombies distance:")
        for k, v in zombies_in_room.items():
            print(f" - {k.replace('_', ' ').capitalize()}: {v.distance:.1f}m - Health: {v.health:.0f}/{character_data['zombie']['max_health']}")
    print('\n')
    

# Configuration Databases (Fake registries)
environment_data = {
    'secret_door_locked': True, 
    'window_blocked': False, 
    'weapons_arsenal': ['magnum', 'flamethrower', 'grenade-launcher', 'submachine-gun'],
    'generator_power_on': False
}

scene_items = {
    'green_herb': 3,
    'magnum_ammo': 20,
    'flamethrower_ammo': 100,
    'grenade_launcher_ammo': 10,
    'submachine_gun_ammo': 150
}

item_properties = {
    'green_herb': {
        'healing_power': 40
    }
}

weapon_properties = {
    'magnum': {
        'max_ammo': 6,
        'ammo_count': 6,
        'base_damage': 30,
        'critical_chance': (0.25, 1.5),  # 25% chance to do 50% extra damage
        'ammo_type': 'municao_magnum'
    }, 
    'flamethrower': {
        'max_ammo': 400,
        'ammo_count': 400,
        'base_damage': 20,
        'critical_chance': (0.1, 1.3),        
        'ammo_type': 'municao_lanca_chamas'
    }, 
    'grenade-launcher': {
        'max_ammo': 12,
        'ammo_count': 12,
        'base_damage': 50,
        'critical_chance': (0.05, 1.8),        
        'ammo_type': 'municao_lanca_granadas'
    }, 
    'submachine-gun': {
        'max_ammo': 60,
        'ammo_count': 60,
        'base_damage': 20,
        'critical_chance': (0.1, 1.3),        
        'ammo_type': 'municao_submetralhadora'
    } 
}

character_data = {
    'leon': {
        'defense': 0.9,
        'max_health': 100,
        'push_force': 3.0
    },
    'claire': {
        'defense': 1.0,
        'max_health': 150,
        'push_force': 1.5
    }, 
    'zombie': {
        'attack': 10,
        'max_health': 100,
        'step_size': 0.5
    }
}

status_colors = {
    'FINE': '\033[1;32;48m',
    'CAUTION': '\033[1;33;47m',
    'DANGER': '\033[1;31;43m',
    'DEATH': '\033[1;30;48m',
    'RESET': '\033[m'
}

# Object Spawning
environment = Environment(environment_data, scene_items)
leon = Leon(environment)
claire = Claire(environment)

zombie_1 = Zombie('zumbi_1', character_data, 3.0)
zombie_2 = Zombie('zumbi_2', character_data, 5.0)
zombie_3 = Zombie('zumbi_3', character_data, 0.0)

zombies_in_room = {
    'zumbi_1': zombie_1, 
    'zumbi_2': zombie_2, 
    'zumbi_3': zombie_3
}


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
                print('Invalid option.')
            else:
                if weapon_action in [1, 2]:
                    break
                else:
                    print('Invalid option.')
        if weapon_action == 1:
            update_screen()
            for i, weapon in enumerate(environment.environment_data['weapons_arsenal']):
                print(f'{i + 1} - {weapon.replace("-", " ").capitalize()}')
            while True:
                try:
                    weapon_choice = int(input('Which weapon do you want to take? (0 to go back): '))
                except ValueError:
                    print('Invalid option.')
                else:
                    break
            if weapon_choice == 0:
                break
            elif 1 <= weapon_choice <= len(environment.environment_data['weapons_arsenal']):
                weapon = environment.environment_data['weapons_arsenal'][weapon_choice - 1]
                character.collect_weapon(weapon)
            else:
                print('Invalid option.')
                input()
        else:
            break


def view_available_items(environment):
    while True:
        update_screen()
        available_items = [item for item in environment.scene_items]
        if not available_items:
            print('No more items left in this room.')
            input()
            break
        print('Items in the room: ')
        for i, (item, quantity) in enumerate(environment.scene_items.items()):
            print(f"{i + 1} - {item.replace('_', ' ').capitalize()}: {quantity}")
        while True:
            try:
                item_index = int(input('Which item do you want to take? (0 to go back): '))
                if item_index == 0:
                    break
                extracted_item = available_items[item_index - 1]
                requested_quantity = int(input('What quantity do you want to extract? '))
            except (ValueError, IndexError):
                print('Invalid option.')
                input()
                break
            else:
                if requested_quantity <= environment.scene_items[extracted_item]:
                    character.collect_item(extracted_item, requested_quantity)
                    print(f"{requested_quantity} {extracted_item.replace('_', ' ')} successfully extracted.")
                    input()
                    break
                else:
                    print('Requested quantity exceeds room availability.')
                    continue
        if item_index == 0:
            break


def activate_combat_mode():
    while True:
        valid_options = [1, 2, 3]
        zombies_to_push = []
        while True:
            update_screen()
            print('1 - Shoot | 2 - Reload | 3 - Go back', end='')
            counter = 4
            for monster, z_obj in zombies_in_room.items():
                if z_obj.distance == 0:
                    print(f' | {counter} - Push {monster.replace("_", " ").capitalize()}', end='')
                    valid_options.append(counter) 
                    zombies_to_push.append((counter, monster))
                    counter += 1
            try:
                combat_choice = int(input('\nWhat do you want to do? '))
                if combat_choice in valid_options:
                    pass
                else:
                    print('Invalid option.')
                    input()
                    continue
            except ValueError:
                print('Invalid option.')
                input()
            else:
                if combat_choice == 1:
                    if not character.equipped_weapon:
                        print(f'{character.name.capitalize()} has no weapon equipped.')
                        input()
                        break       
                    character.shoot()
                    break
                elif combat_choice == 2:
                    character.reload_weapon()
                    break
                elif combat_choice == 3:
                    break
                elif combat_choice > 3:
                    for counter, monster in zombies_to_push:
                        if combat_choice == counter:
                            character.push_zombie(monster)
                            zombies_to_push.remove((counter, monster)) 
                            break
                    break
        if combat_choice == 3:
            break
        move_enemies(zombies_in_room)


def equip_weapon(forced_weapon=''):
    weapons_to_equip = ['magnum', 'flamethrower', 'grenade-launcher', 'submachine-gun']
    equip_list = []
    counter = 1
    if character.inventory:
        while True:
            if forced_weapon:
                character.equipped_weapon = forced_weapon
                break
            for item in weapons_to_equip:
                if item in character.inventory:
                    equip_list.append(item)
                    print(f'{counter} - {item.replace("-", " ").capitalize()}')
                    counter += 1
            else:
                while True:
                    try:
                        weapon_option = int(input('Which weapon do you want to equip? (0 to exit): '))
                        if weapon_option == 0:
                            break
                        character.equipped_weapon = equip_list[weapon_option - 1]
                    except (ValueError, IndexError):
                        print('Invalid option.')
                        input()
                    else: 
                        print(f'{character.equipped_weapon.replace("-", " ").capitalize()} equipped.')
                        input()
                        break
                if weapon_option == 0 or character.equipped_weapon:
                    break
    else:
        print('Inventory is empty.')
        input()


def use_item_menu():
    if not character.inventory:
        print('Inventory is empty.')
        input()
        return
    else:
        for i, (item, quantity) in enumerate(character.inventory.items()):
            print(f"{i + 1} - {item.replace('_', ' ').replace('-', ' ').capitalize()}: {quantity}")
        inventory_items = [item for item in character.inventory]
    while True:
        try:
            chosen_index = int(input('Which item do you want to use? '))
            if chosen_index > len(character.inventory) or chosen_index <= 0:
                print('Invalid option.')
                input()
                continue
        except ValueError:
            print('Invalid option.')
        else:
            break
            
    chosen_item = inventory_items[chosen_index - 1]
    if chosen_item == 'green_herb':                                      # TODO: External dictionary with the actions of each item, using lambda functions
        character.use_herb('green_herb')
    elif chosen_item == 'municao_magnum':
        character.reload_weapon(chosen_item)
    elif chosen_item in weapon_properties:
        equip_weapon(chosen_item)


def move_enemies(zombies_dict):
    for z_obj in list(zombies_dict.values()): 
        z_obj.walk()
        update_screen()
        if z_obj.distance <= 0:
            z_obj.bite()


# ==============================================================================
# MAIN GAME INTERACTIVE INITIALIZATION
# ==============================================================================
if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Who do you want to play with? ')
    while True:
        try:
            character_index = int(input('1 - Leon | 2 - Claire: '))
        except ValueError:
            print('Invalid option.')
        else:
            if character_index in [1, 2]:
                if character_index == 1:
                    character = leon
                else:
                    character = claire
            else:
                print('Invalid option.')
                continue
            break

    print(f'\n{character.name.capitalize()} entered the secret room...\n')
    input('Press Enter to start...')
    
    # Core Global Game Loop Processing
    while True:
        update_screen()
        move_enemies(zombies_in_room)
        
        if character.health <= 0:
            update_screen()
            print('YOU DIED!')
            break 
            
        update_screen()
        print('Actions:')
        print('1 - Check available weapons in the arsenal')
        print('2 - Check available items in the room')
        print('3 - Combat Mode')
        print('4 - Equip Weapon')
        print('5 - Use Item')
        print('6 - Do Nothing')
        print('7 - Leave the Room')
        print('\n')
        
        while True:
            try:
                action = int(input('What do you want to do? '))
                update_screen()
            except ValueError:
                print('Invalid action.')
            else:
                if 1 <= action <= 7:
                    break
                else:
                    print('Invalid action.')
                    continue
                    
        if action == 1:
            view_available_weapons(environment)            
        elif action == 2:
            view_available_items(environment)
        elif action == 3:
            activate_combat_mode()
        elif action == 4:
            equip_weapon()
        elif action == 5:
            use_item_menu()            
        elif action == 6:
            pass
        elif action == 7:
            break

    print('Game Over.')
