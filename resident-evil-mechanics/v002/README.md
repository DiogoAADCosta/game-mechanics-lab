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

## 📈 Future Improvements (What's Next in Version 3.0)
While Version 2.0 drastically cleaned up item handling, it operates on structural assumptions:
- **Introduction of Dynamic Damage Systems:** Move from textual failure states (like falling into a pit) to active numeric health processing, damage scaling, and healing items.
- **Advanced State Management:** Transition from a single, isolated room mock-up into a complex dataset ready to handle multiple, independent rooms or items simultaneously.
