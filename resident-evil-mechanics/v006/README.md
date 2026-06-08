# Game Mechanics Lab: Tactical Combat Engine & Real-Time Proximity (Version 6.0)

Version 6.0 stands as the **Latest Stable Version** of the Resident Evil gameplay systems prototype. This major milestone transitions the engine into an interactive state machine featuring real-time turn tracking, modular weapon reloads, deterministic enemy movement rules, probabilistic calculations, and rich terminal interfaces using complex conditional workflows.

---

## 🕹️ Feature Overview
The terminal prototype transforms into a playable tactical simulation where player positioning, ammunition conservation, and status telemetry directly dictate survival.

- **Dynamic Vitals Engine:** Processes real-time health ratios to generate retro-style vitals monitors (FINE, CAUTION, DANGER, DEATH) mapped using custom ANSI color codes.
- **Probabilistic Critical Systems:** Integrates randomized float generations to evaluate weapon-specific critical damage spikes during runtime combat interactions.
- **Real-Time Proximity Pressure:** Spawns enemy objects with floating-point coordinate scales. Every spent turn causes monsters to automatically advance, triggering unique close-combat options like dynamic pushbacks.
- **Modular Ammunition Validation:** Implements multi-tier reloading logic, cross-checking weapon properties with stacked inventory resources before executing dynamic state updates.
- **Data Bug Resolution:** Refactored inherited array deletion bugs to natively support stacked dictionary inventory structures securely across all item consumption pipelines.

---

## 🏗️ Architectural Decisions & Implementation

### 1. Unified Game State Orchestration
To enable seamless character toggles, the engine abstracts the global simulation into an independent operational variable pointer. This allows functions like update_screen to dynamically resolve data structures for Leon or Claire uniformly, maximizing code reusability.

### 2. Probabilistic Attack Scaling
The shoot function isolates core damage mathematics from visual layout scripts. When a weapon discharges, the engine leverages random number generation to gauge critical success thresholds:
critical_coefficient = random.random()
is_critical = critical_coefficient <= weapon_entry[critical_chance][0]
This approach mirrors structural damage calculations used in commercial software to handle backend gameplay events efficiently.

### 3. State Cooldown and Enemy Sub-processes
The Zombie class controls its own AI step state. It evaluates spatial intervals dynamically; if distance integers drop to zero, it shifts from walking sub-routines to bite actions. To prevent unfair stack damage, a boolean toggle manages combat cooldowns, forcing the entity to alternate action beats predictably.

---

## 📈 Future Improvements (Backlog for Version 7.0+)

As the latest stable baseline, this architecture serves as a foundation for advanced decoupled systems, multi-file modularization, and deep survival horror gameplay expansions:

- **Decoupled Item Execution Layer (Adaptive Algorithms):** Refactor the rigid item evaluation conditional chains (if/elif) into an external dictionary map using Python lambda functions or function pointers. This applies dynamic action routing, allowing new consumables to be injected at runtime without modifying class core files.
- **Strict Inventory Constraints & Interconnected Storage Box:** Introduce localized slot maximums for character inventories, forcing tactical encumbrance choices. To balance this limitation, a persistent global StorageBox dataset will be implemented to securely cache resource overflows across independent active safezones.
- **Time-Cost Action Engine (Pacing Multipliers):** Replace flat action phases with a fluid Time-Tick cost matrix. High-commitment activities (e.g., reloading weapons or processing health compounds) will drain multiple operational ticks, forcing enemy proximity updates to loop consecutively and increasing combat tension.
- **Finite Utility Weaponry (Knife Durability Mechanics):** Expand close-quarter defense choices by introducing a Combat Knife class. Unlike standard infinite armaments, this utility item will execute dynamic durability consumption data tracking, fracturing the resource permanently when structural integrity metrics zero out.
- **Alchemical Resource Aggregations (Herb Combination Systems):** Implement inventory-layer combination algorithms. Merging separate resource entities (e.g., Green + Green or Green + Red) will purge initial keys and upsert a new customized chemical compound item featuring stacked potency modifiers.
- **Hierarchical Finite State Machine (FSM AI Archetypes):** Refactor enemy behaviors into an explicit State Pattern framework. Entities will evaluate runtime triggers to swap between decoupled behavior nodes: IDLE, PATROL, CHASE, STUNNED, and DEAD, drastically professionalizing logic handling inside scene managers.
- **Multi-Room Spatial Coordinates via Graphs:** Transition from a single mock room array into a multi-node Graph structure representing adjacent rooms, letting players move between distinct scenes with local threat persistence.
- **Data Serialization & File Persistence:** Integrate native json or database save-state mechanics to store and load player inventory pools, environmental zapping changes, and character status data dynamically from cold disk storage.
- **Decoupled Architecture & Multi-File Modularization:** Disassemble the monolith single-file design into clear architectural boundaries: models.py for configurations and core metrics registry, engine.py for transaction validation frameworks, and main.py dedicated exclusively to running the interactive frame loops.
- **Game Engine Visual Integration Layer (Frontend Decoupling):** Port the fully decoupled core Python engine into a graphical game engine environment (such as Godot via GDPython, or Pygame/Ursina). The existing console interface will be completely replaced by an independent visual rendering viewport, mapping the backend's dictionary states directly to real-time 2D sprite telemetry, dynamic audio triggers, and a graphic HUD.
