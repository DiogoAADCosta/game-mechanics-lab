# Game Mechanics Lab: Interactive Terminal Loop & UI Rendering (Version 4.0)

Version 4.0 marks a foundational shift in the project's execution model. The engine evolves from an automated, linear script execution into an interactive, user-driven **CLI Game Loop**. This version introduces state-driven choice matrices, automated terminal refresh pipelines, input exception handling, and real-time spatial positioning metrics.

---

## 🕹️ Feature Overview
The simulation now behaves like a fully functional text-based game. Control is handed directly to the player, who navigates options through structured numerical menus while the engine manages active scene metrics.

- **Persistent State Display:** The interface dynamically prints character vital stats (HP) and local environmental threats before presenting any option menu.
- **Interactive Choice Matrices:** Players make runtime decisions via input triggers (e.g., checking arsenals, interacting with the room, choosing to exit).
- **Dynamic Turn Loops:** Individual loops handle player interactions sequentially, allowing Leon to fully complete his turn and impact the scene data before passing execution context to Claire.
- **Active Refresh Pipeline:** Employs cross-platform console manipulation commands to wipe screen memory at the start of each action, simulating an updated "screen frame".
- **Runtime Input Validation:** Implements exception blocks (try-except) to prevent system crashes if the user inputs invalid text characters instead of expected integers.

---

## 🏗️ Architectural Decisions & Implementation

### 1. Cross-Platform Terminal Refresh Layers
To prevent the terminal from turning into an endless scrolling wall of text, a centralized layout updater was integrated. By checking the underlying operating system environment name string, the engine invokes the correct machine sub-process command to clean up previous print stacks:
os.system('cls' if os.name == 'nt' else 'clear')
This guarantees that the game window displays only the active parameters of the current state.

### 2. Defensive Programming with Error Handling
To insulate the game loop against unexpected user inputs, numerical menu fields are wrapped inside infinite operational evaluation blocks. By capturing ValueError flags natively, the engine traps improper typings before they propagate up the call stack, prompting the player to re-enter a correct selection without terminating the game thread.

### 3. Spatial Tracking Foundations
The architecture begins exploring tactical geography with the integration of an enemy distance dictionary tracking proximity in meters. While static in this prototype, this metric prepares the logic pipeline for future positional scaling, where character choices directly alter enemy distance steps.

---

## 📈 Future Improvements (Achieved in Version 5.0)
Version 4.0 successfully established the dynamic visual frame layouts but left room interaction systems as empty stubs. The next iteration implements:
- **Stackable Inventory & Resource Management:** Moving away from primitive array listings to dictionary-mapped key-value stores, allowing both players and rooms to manage real-time item quantities.
- **Dynamic Supply Extraction Pipelines:** Activating localized sub-menus capable of querying scenario database states, modifying remaining quantities, and safely executing database drops when stock reaches absolute zero.
- **Polymorphic Action Hooks:** Integrating deep transactional logic within menu operations to handle active dynamic item stacking and character state modifications.
