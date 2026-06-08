# Game Mechanics Lab: Clean Code & Inventory Generalization (Version 2.0)

Version 2.0 refactors the initial Zapping System architecture by applying core **Clean Code** principles, introducing a proper class hierarchy, and establishing scalable validation rules for item management.

---

## 🕹️ Feature Overview
The scope expands from simple boolean triggers to an encapsulated inventory structure. Characters are no longer mere extensions of the global script; they are active entities bound by specific gameplay constraints.

- **Unified Resource Set:** The environment state now holds a collection (`set`) representing physically available weapons, natively preventing duplication bugs.
- **Generalized Item Collection:** Rigid, item-specific methods were completely replaced by a single polymorphic extraction function.
- **Strict Character Constraints:** Implements gameplay-driven business rules. Leon and Claire have strict access permissions to specific weapon types.
- **The Generator Event:** A new environment variable (`generator_power_on`) creates a cause-and-effect branching path for Claire's exploration logic (safe passage vs. taking damage).

---

## 🏗️ Architectural Decisions & Implementation

### 1. Object-Oriented Class Hierarchy (DRY Principle)
To adhere to the *Don't Repeat Yourself* (DRY) principle, a parent `Player` class was introduced. It centralizes inventory storage and common behaviors. The child classes (`Leon` and `Claire`) utilize `super().__init__(environment)` to inherit base properties while defining unique attributes like `allowed_weapons` and specialized character narrative checks.

### 2. Two-Way Validation Flow
Resource collection now requires a secure hand-shake between the actor and the environment:
1. The character checks if they have the specific proficiency to handle the weapon.
2. If verified, the request is sent to the `Environment`.
3. The item is only appended to the character's inventory if the environment confirms successful validation and physical removal from the scene pool.

---

## 📈 Future Improvements (Achieved in Version 3.0)
While Version 2.0 drastically cleaned up item handling, it operated on basic textual outcomes. The next iteration implements:
- **Dynamic Vitality & Damage Systems:** Moving away from binary triggers to an active numerical health tracker (`health`) driven by dynamic damage calculations and character-specific defense multipliers.
- **Support Items & Consumable Support:** Introducing a dedicated scene item pool (`scene_items`) capable of handling stacked supplies like healing herbs, integrated with inventory removal and health-cap safety clamps.
- **Introduction of AI Archetypes:** Establishing the initial foundation for enemy interaction with the creation of the `Zombie` class, capable of triggering direct damage methods against players.
