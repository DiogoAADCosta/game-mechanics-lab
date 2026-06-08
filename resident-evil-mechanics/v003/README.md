# Game Mechanics Lab: Dynamic Vitality, Damage & Healing (Version 3.0)

Version 3.0 advances the core gameplay engine by transitioning from binary textual outcomes to an active, data-driven **Numerical Stat System**. This iteration introduces runtime damage tracking, character-specific defense modifiers, resource stack consumption, and the foundation for enemy AI interactions.

---

## 🕹️ Feature Overview
The simulation moves closer to a real-time game state engine. Characters now possess quantifiable health pools, react dynamically to physical threats, and can actively deploy consumable support structures to mitigate risks.

- **Quantifiable Vitality (HP Pools):** All player instances spawn with a dynamic health metric initializing at a baseline maximum of 100.
- **Scaled Damage Pipelines:** Integrated numerical damage triggers where character attributes actively scale incoming damage values.
- **Dynamic Scene Item Pools:** Introduces a decentralized storage tracking system (scene_items) to manage consumable resources separate from the fixed weapon arsenal.
- **Consumable Support Execution:** Players can actively consume localized inventory items (green_herb) to restore stats, protected by a logical safety clamp preventing numerical health overflow.
- **Active Enemy Archetype:** Introduces the base Zombie class, capable of interacting directly with player object methods to trigger damage loops.

---

## 🏗️ Architectural Decisions & Implementation

### 1. Hardcoded Configuration Dictionaries as Fake Databases
Instead of scattering game values inside class definitions, this version introduces clean config dictionaries (character_data, item_properties) at the top of the script. This design abstracts configurations from game execution logic, simulating how modern engines load game attributes from JSON or external databases.

### 2. Algorithmic Damage Calculations (Defense Modifiers)
When an entity attacks a player, the system triggers the take_damage(damage) method. Rather than a flat reduction, the script evaluates a mathematical formula using character context attributes where the multiplier factor is fetched directly from the defense dictionary and applied to reduce the total health pool. This enables specialized character attributes, such as Leon having a stronger armor defense modifier (0.9) compared to Claire (1.0).

### 3. State Clamping for Resource Consumption
To ensure structural integrity during healing actions, a logical boundary clamp was integrated into the Player class. The script safely extracts items from the object’s own instance array, increments health points, and guarantees stats never overflow past maximum thresholds by explicitly forcing the health attribute back to its max_health value if it exceeds the dynamic cap.

---

## 📈 Future Improvements (Achieved in Version 4.0)
Version 3.0 successfully established math-based attributes but operated on a flat, automated sequence. The next iteration implements:
- **Interactive Game Loop & Turn Systems:** Replacing automatic execution with a responsive input-driven loop, transforming the engine into a playable CLI turn-based game.
- **Dynamic Terminal UI Rendering:** Integrating operating system subprocesses (os.system) to wipe the console cache at the start of each turn, creating a clean, modern frame-by-frame presentation.
- **State-Driven Spatial Elements:** Laying down the infrastructure for tactical space constraints by managing real-time distances between enemies and players.
