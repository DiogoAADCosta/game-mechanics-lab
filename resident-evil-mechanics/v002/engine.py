# Global database representing the game state. Weapon collection boolean keys
# from Version 1 were refactored into a unified collections set for better scaling.
environment_data = {
    'secret_door_locked': True, 
    'window_blocked': False, 
    'weapons_arsenal': {'magnum', 'flamethrower', 'grenade-launcher', 'submachine-gun'},
    'generator_power_on': False
}

class Environment:
    def __init__(self, environment_data):
        self.environment_data = environment_data

    def unlock_secret_door(self):
        self.environment_data['secret_door_locked'] = False

    # Generalized Mechanic: Specific item methods were eliminated. 
    # This single method dynamically manages the scene's resources.
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

class Player:
    def __init__(self, environment):
        self.environment = environment
        # Each character now manages their own encapsulated resource list
        self.inventory = []

    def collect_weapon(self, weapon):
        # The item is only added if the environment confirms successful removal
        weapon_collected = self.environment.collect_weapon(weapon)
        if weapon_collected:
            self.inventory.append(weapon_collected)

    def turn_on_generator(self):
        self.environment.turn_on_generator()

class Leon(Player):
    def __init__(self, environment):
        super().__init__(environment)
        # Business Rule: Strict validation constraints for weapon usage
        self.allowed_weapons = {'magnum', 'flamethrower'}
        self.name = 'Leon'

    def collect_weapon(self, weapon):
        if weapon in self.allowed_weapons:
            super().collect_weapon(weapon)
        else:
            print(f'{self.name} does not know how to use this weapon.')

    def unlock_door(self):
        self.environment.unlock_secret_door()

    def block_window(self):
        self.environment.block_window()
    

class Claire(Player):
    def __init__(self, environment):
        super().__init__(environment)
        # Business Rule: Strict validation constraints for weapon usage
        self.allowed_weapons = {'grenade-launcher', 'submachine-gun'}
        self.name = 'Claire'

    def collect_weapon(self, weapon):
        if weapon in self.allowed_weapons:
            super().collect_weapon(weapon)
        else:
            print(f'{self.name} does not know how to use this weapon.')

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

    # New State-Driven Narrative Consequence (The Generator Room)
    def explore_generator_room(self):
        if self.environment.environment_data['generator_power_on']:
            print(f'{self.name} passed through safely.')
        else:
            print(f'The room is too dark. {self.name} fell into a pit!')

    
# ==============================================================================
# EXECUTION FLOW (GAME SIMULATION)
# ==============================================================================

environment = Environment(environment_data)
leon = Leon(environment)
claire = Claire(environment)

print(f"Before Leon unlocks the door - Door locked: {environment_data['secret_door_locked']}")
leon.unlock_door()
print(f"After Leon unlocks the door - Door locked: {environment_data['secret_door_locked']}")

print('Claire goes to check the door.')
claire.check_door()

leon.collect_weapon('magnum')
print(environment_data['weapons_arsenal'])

leon.collect_weapon('flamethrower')
print(environment_data['weapons_arsenal'])
print(f"Leon's Inventory: {leon.inventory}")

claire.collect_weapon('grenade-launcher')
print(environment_data['weapons_arsenal'])

# Testing business rule constraints (Leon attempting to pick up Claire's weapon)
leon.collect_weapon('submachine-gun')

leon.block_window()
claire.pass_through_corridor()

leon.turn_on_generator()

# Testing resource depletion (Leon attempting to pick up an item already removed)
leon.collect_weapon('magnum')
print(f"Leon's Inventory: {leon.inventory}")

claire.explore_generator_room()
