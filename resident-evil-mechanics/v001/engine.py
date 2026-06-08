# Global dictionary and list simulating a database for the game state
environment_data = {
    'secret_door_locked': True, 
    'flamethrower_collected': False, 
    'window_blocked': False, 
    'magnum_collected': False
}

weapons_arsenal = ['flamethrower', 'magnum']

class Environment:
    def __init__(self, environment_data, weapons_arsenal):
        # Dependency Injection: The environment encapsulates its own state references
        self.environment_data = environment_data
        self.weapons_arsenal = weapons_arsenal

    def unlock_secret_door(self):
        self.environment_data['secret_door_locked'] = False

    # Specific item methods (these will be unifed and generalized in future versions)
    def collect_flamethrower(self, weapon):
        self.environment_data['flamethrower_collected'] = True
        self.weapons_arsenal.remove(weapon)
    
    def collect_magnum(self, weapon):
        self.environment_data['magnum_collected'] = True
        self.weapons_arsenal.remove(weapon)

    def block_window(self):
        self.environment_data['window_blocked'] = True

class Leon:
    def __init__(self, environment):
        # Architecture Decision: Character receives the environment instance via constructor,
        # ensuring encapsulation and preventing direct global scope manipulation.
        self.environment = environment
    
    def unlock_door(self):
        self.environment.unlock_secret_door()

    def collect_weapon(self, weapon):
        if weapon == 'magnum':
            self.environment.collect_magnum(weapon)
        elif weapon == 'flamethrower':
            self.environment.collect_flamethrower(weapon)

    def block_window(self):
        self.environment.block_window()

class Claire:
    def __init__(self, environment):
        self.environment = environment

    # Verification Methods: Claire does not modify the environment state in this version;
    # she only reads and reacts to the consequences left behind by Leon.
    def check_door(self):
        if self.environment.environment_data['secret_door_locked']:
            print('Claire could not enter the secret room.')
        else:
            print('Claire entered the secret room.')

    def check_arsenal(self):
        if self.environment.weapons_arsenal:
            print(self.environment.weapons_arsenal)
        else:
            print('Arsenal is empty.')
    
    def pass_through_corridor(self):
        if self.environment.environment_data['window_blocked']:
            print('Claire passed through the corridor without any problems.')
        else:
            print('Claire was attacked by a zombie from the window!')

    
# ==============================================================================
# EXECUTION FLOW (GAME SIMULATION)
# ==============================================================================

# Instantiating objects and injecting dependencies correctly
environment = Environment(environment_data, weapons_arsenal)
leon = Leon(environment)
claire = Claire(environment)

print(f"Before Leon unlocks the door - Door locked: {environment_data['secret_door_locked']}")
leon.unlock_door()
print(f"After Leon unlocks the door - Door locked: {environment_data['secret_door_locked']}")

print('Claire goes to check the door.')
claire.check_door()

leon.collect_weapon('magnum')
leon.collect_weapon('flamethrower')

print('Claire goes to check the arsenal.')
claire.check_arsenal()

leon.block_window()
claire.pass_through_corridor()
