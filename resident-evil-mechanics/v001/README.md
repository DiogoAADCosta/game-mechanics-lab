# Game Mechanics Lab: Resident Evil Zapping System (Version 1.0)

This is the first project in a series of game mechanic simulations designed to explore object-oriented design, logic structures, and architectural patterns applied to game development. 

Version 1.0 focuses on the **Zapping System** (inspired by *Resident Evil 2*), simulating how a player's actions in one campaign directly alter the state of the game world for a subsequent campaign.

---

## 🕹️ Feature Overview
In this initial prototype, a persistent environment database keeps track of world states. Actions taken by the first character (**Leon**) cause a permanent ripple effect that the second character (**Claire**) must face during her playthrough.

- **Dynamic Environment State:** Tracks room conditions (locked doors, blocked windows) and available items.
- **Persistent Resource Depletion:** If Leon collects a weapon from the weapons arsenal, that resource is permanently removed from the world.
- **Conditional Reactive Logic:** Claire’s narrative and gameplay path dynamically change based on the structural choices left behind by Leon.

---

## 🏗️ Architectural Decisions & Implementation

### 1. Dependency Injection Over Global Coupling
Instead of letting the character classes directly access or manipulate variables in the global scope, the `Environment` instance is passed directly into the characters' constructors (`self.environment = environment`). This ensures encapsulation and prepares the engine for decoupled data management.

### 2. State-Driven Consequences
Claire's class acts as a reader of the state modified by Leon. The game loops evaluate conditions directly from the object's context, showcasing cause-and-effect mechanics without complex visual interfaces.

---

## 📈 Future Improvements (Achieved in Version 2.0)
This version established the core state-sharing logic but left several rigid architectural bottlenecks. The next iteration implements:
- **Unified Inventory & Collection Logic:** Replacing hardcoded weapon methods (`collect_magnum`, `collect_flamethrower`) with a single, generalized function using data structures (`set`) to eliminate redundancy and prevent item duplication.
- **Inheritance & Class Hierarchy:** Introducing a parent `Player` class to encapsulate shared mechanics (like inventory management), allowing `Leon` and `Claire` to specialize through strict business rule constraints.
- **Expanded Environment State:** Incorporating a new interactive trigger (`generator_power_on`) to create branching tactical outcomes and danger zones for characters down the line.
