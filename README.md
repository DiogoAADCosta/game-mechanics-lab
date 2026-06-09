# 🔬 Game Mechanics Lab: Architectural Explorations in Game Design

Welcome to the **Game Mechanics Lab**. This repository is an active, hands-on engineering environment designed to serve as a practical playground for my self-taught software engineering studies. 

Instead of just learning theory passively, I use these micro-labs to get my hands dirty, immediately translating newly acquired software engineering principles, design patterns, and architectural concepts into refactored, live-running code.

The primary objective of this laboratory is not just to make games that work, but to explore **Software Architecture, Object-Oriented Design Patterns, Clean Code Principles, and Structural Scalability** applied directly to game development challenges.

---

## 🧠 Development Philosophy & The "Black Box" Approach

A core constraint of this laboratory is **pure empirical reverse engineering**:

* **Zero Code References:** Every single mechanic, algorithm, and data structure in this repository was conceived and coded from scratch, without looking at external codebases, game engine templates, or tutorials.
* **Player-Driven Logic:** The technical specifications were derived exclusively from analyzing game systems as a player. The logic is the result of translating raw gameplay experiences directly into software architecture. 

This "black box" approach ensures that the focus remains entirely on raw problem-solving, structural design, and authentic mathematical modeling.

---

## 📂 Active Laboratories

This repository is organized into highly specialized directories, each focusing on a distinct era, genre, or core architectural pattern of game loop engineering:

### 🧟 [resident-evil-mechanics/](https://github.com/your-username/game-mechanics-lab/tree/main/resident-evil-mechanics)
* **Genre/Inspiration:** Retro Survival Horror (Resident Evil series).
* **Engineering Focus:** State persistence, resource depletion systems, and real-time tactical proximity math.
* **Architecture Progress:** 6 evolutionary versions tracking the transition from a primitive procedural global script to an interactive CLI turn-based game engine. Uses Dependency Injection, strict inheritance restrictions, cross-platform terminal refresh frame updating, and probabilistic critical-hit loops.
* **Current Baseline:** Version 6.0 (Latest Stable Version).

### ⚔️ [pokemon-battle-system/](https://github.com/your-username/game-mechanics-lab/tree/main/pokemon-battle-system) *(Upcoming Lab)*
* **Genre/Inspiration:** Turn-Based RPG (Classic Pokémon Game Boy series).
* **Engineering Focus:** State-driven combat structures, type-effectiveness matrices, and multi-tier action queues.
* **Architecture Vision:** Exploring structured state machines, decoupled battle log routing, and complex database lookups for moves, stats, and status ailments.

---

## 🏗️ Core Engineering Paradigms Explored

Across all laboratories, the development process prioritizes industry-standard backend software patterns over simple visual rendering:

* **Strict Decoupling (Core vs. View):** Designing engines where data processing, validation constraints, and combat mathematics live completely isolated from terminal printing functions or external frontend viewports.
* **Dependency Injection:** Enforcing strict class structures where actors and entities receive state contexts through constructors instead of manipulating the global scope directly.
* **Defensive Input Validation:** Wrapping dynamic user choices inside safe mathematical boundaries and exception-handling frameworks to prevent state corruption during runtime operations.
* **Data-Driven Architectures:** Abstracting engine properties (weapon stats, enemy attributes, healing factors) into centralized registries that act as local databases, simulating commercial game asset loading patterns.

---

## 📈 Long-Term Laboratory Roadmap

As this repository scales, future development sprints will move towards advanced software engineering patterns:

1. **Multi-File Modularization:** Disassembling monolithic architecture baselines into clean boundaries (e.g., separating models.py data structures from engine.py transaction rule processors).
2. **Behavioral Design Patterns:** Upgrading conditional systems (if/elif chains) to advanced structural patterns such as the State Pattern (for AI entities) and Command Pattern (for decoupled action mapping).
3. **Frontend Visual Porting:** Connecting fully functional Python logic backends directly to modern graphical rendering engines (such as Godot or Pygame), mapping data dictionaries into real-time visual telemetry, dynamic sprites, and graphic audio layouts.

---

"A good game engine is simply an incredibly well-architected data processor that captures the rules of a world, regardless of how it is rendered."
