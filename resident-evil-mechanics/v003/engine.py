# Global databases acting as game configuration data registries
environment_data = {
    'secret_door_locked': True, 
    'window_blocked': False, 
    'weapons_arsenal': {'magnum', 'flamethrower', 'grenade-launcher', 'submachine-gun'},
    'generator_power_on': False
}

scene_items = {
    'green_herb': 3
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


class Environment:
    def __init__(self, environment_data, scene_items):
        self.environment_data = environment_data
        # Separating the structural scenario triggers from stackable consumable item counters
        self.scene_items = scene_items

    def unlock_secret_door(self):
        self.environment_data['secret_door_locked'] = False

    def collect_weapon(self, weapon):
        if weapon in self.environment_data['weapons_arsenal']:
            self.environment_data['weapons_arsenal'].remove(weapon)
            return weapon
        else:
            print('Weapon not available.')
            return None
    
    def block_window(self):
        self.environment_data['window_blocked'] = True

    def turn_on_generator(self):
        self.environment_data['generator_power_on'] = True

    def extract_item(self, item):
        # Numeric verification to manage stackable item consumption inside the room
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
    
    def collect_item(self, item):
        item_collected = self.environment.extract_item(item)
        if item_collected:
            self.inventory.append(item_collected)

    def turn_on_generator(self):
        self.environment.turn_on_generator()

    def take_damage(self, damage):
        # Scaled Damage: Applies a unique mathematical reduction factor based on character attributes
        multiplier_factor = self.character_data[self.name]['defense']
        self.health -= damage * multiplier_factor

    def use_herb(self, herb):
        # Consumable Logic: Safely handles item removal and applies healing value up to the cap limit
        if herb in self.inventory:
            self.inventory.remove(herb)
            self.health += self.item_properties[herb]['healing_power']
        
        # Health-Cap Safety Clamp: Prevents numerical overflow past max limits
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

    # Enemy Action Blueprint: Interacts directly with player instances to trigger damage pipelines
    def attack(self, target, damage):
        target.take_damage(damage)


# ==============================================================================
# EXECUTION FLOW (GAME SIMULATION)
# ==============================================================================

environment = Environment(environment_data, scene_items)
leon = Leon(environment)
claire = Claire(environment)
zombie = Zombie(character_data)

print(f"Before Leon unlocks the door - Permanent door locked state: {environment_data['secret_door_locked']}")
leon.unlock_door()
print(f"After Leon unlocks the door - Permanent door locked state: {environment_data['secret_door_locked']}")

print('Claire goes to check the door.')
claire.check_door()

leon.collect_weapon('magnum')
print(environment_data['weapons_arsenal'])
leon.collect_weapon('flamethrower')
print(environment_data['weapons_arsenal'])
print(f"Leon's Inventory: {leon.inventory}")

claire.collect_weapon('grenade-launcher')
print(environment_data['weapons_arsenal'])

leon.collect_weapon('submachine-gun')
leon.block_window()
claire.pass_through_corridor()

leon.turn_on_generator()
leon.collect_weapon('magnum')
print(f"Leon's Inventory: {leon.inventory}")

claire.explore_generator_room()

# Dynamic Status Check
print(f"Claire's Health before attack: {claire.health}")
print(f"Leon's Health before attack: {leon.health}")

# Zombie encounters and damage execution
zombie.attack(claire, character_data['zombie']['attack'])
zombie.attack(leon, character_data['zombie']['attack'])

print(f"Claire's Health after attack (1.0 defense multiplier): {claire.health}")
print(f"Leon's Health after attack (0.9 defense multiplier): {leon.health}")

print(f"Room items before collection: {scene_items}")
claire.collect_item('green_herb')
print(f"Claire's Inventory: {claire.inventory}")
print(f"Room items after collection: {scene_items}")

# Execution of healing mechanics and safety clamp check
claire.use_herb('green_herb')
print(f"Claire's Health after using green_herb (Capped at max): {claire.health}")
