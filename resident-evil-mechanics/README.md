# 🕹️ Game Mechanics Lab: Resident Evil Systems Prototype

Welcome to the **Resident Evil Mechanics Laboratory**. This repository serves as a progressive engineering environment dedicated to simulating, decomposing, and restructuring core retro survival horror game mechanics using clean Python programming and solid software architecture principles.

Instead of deploying a single monolith script, this project traces an incremental software evolution path across **6 developmental versions**, transforming basic procedural triggers into a playable, event-driven CLI Game Engine.

---

## 🚀 The Architectural Evolution

This repository provides a clear roadmap showing how raw code evolves into clean, maintainable software. Below is the structural progression of the engine:

### 📁 version-1/ : The Zapping Foundation (v1.0)
- **Core Concept:** Cause-and-effect data state persistence between separate game loops (Leon Scenario A directly altering Claire Scenario B).
- **Design Pattern:** First implementation of **Dependency Injection Over Global Coupling**, passing the local environment instance explicitly via constructors to encapsulate state references.

### 📁 version-2/ : Hierarchy & Clean Code (v2.0)
- **Core Concept:** Removing duplication patterns and implementing stricter object constraints.
- **Design Pattern:** Application of the **DRY (Don't Repeat Yourself) Principle** by introducing a generic `Player` parent class, leveraging inheritance structures, and refactoring reduntant collection behaviors into a polymorphic function wrapper.

### 📁 version-3/ : Numerical Pipelines & AI Spawning (v3.0)
- **Core Concept:** Transitioning from text-driven binary states to a dynamic math-driven pipeline.
- **Design Pattern:** Separating runtime configurations from core execution layers using hardcoded configuration tables (simulating JSON external datasets). Implementing dynamic damage modifiers and data clamps to trap health pools securely at maximum limits.

### 📁 version-4/ : Game Loop Mechanics & Frame Updates (v4.0)
- **Core Concept:** Evolving from automatic script sequencing into an interactive terminal turn loop.
- **Design Pattern:** Integrating cross-platform OS subprocess hooks to wipe console history and generate static interface frames. Implementation of **Defensive Programming via Exception Handling** to catch and insulate input crashes before propagation.

### 📁 version-5/ : Transactional Inventories & Upsert Maps (v5.0)
- **Core Concept:** Upgrading arrays into structural stack maps to handle item counts.
- **Design Pattern:** Migrating storage containers to dictionary structures (`dict`), implementing **Database-style Upsert Patterns** to control stack increments, and executing complete field deletions (`del`) upon stock resource exhaustion.

### 📁 version-6/ : Tactical Systems & Telemetry (v6.0 - Latest Stable)
- **Core Concept:** Activating a playable combat matrix, ballistic formulas, enemy movement vectors, and status UI arrays.
- **Design Pattern:** State pointer abstraction allowing unified rendering for separate player objects. Implementation of probabilistic math metrics tracking critical hits alongside dynamic ANSI escape code telemetry blocks tracking character vitals.

---

## 🏗️ Core Tech Stack & Software Highlights

- **Language:** Python 3.10+
- **Architectural Paradigms:** Object-Oriented Programming (OOP), Polymorphism, Inheritance, Encapsulation, and Dependency Injection.
- **Development Methodologies:** Defensive Programming (Input Trapping), Test-Driven Simulation Flows, and DRY refactoring metrics.
- **UI Architecture:** Cross-Platform CLI Rendering Engine (Wiped Frame Cache Execution) with color-coded ANSI diagnostics.

---

## 📈 Long-Term Backlog & Future Vision (Towards v7.0+)

The latest stable architecture provides a robust foundation for next-tier decoupled systems and game engine deployments:

- **Decoupled Item Execution Layer:** Replacing rigid evaluation chains with dictionary function pointers using `lambda` expressions to route dynamic item actions natively from data sheets.
- **Strict Inventories & Global Storage Boxes:** Enforcing localized player weight limits coupled with an interconnected global data cache to store item pools across distinct scenes.
- **Time-Cost Action Engine (Tick System):** Implementing multi-tick costs for premium actions (like reloading or using herbs), causing enemy entities to loop step cycles sequentially based on action weight.
- **Finite Utility Weaponry (Knife Durability):** Introducing a Combat Knife object that processes degradation statistics, completely fracturing the structural asset once integrity flags drop to zero.
- **Alchemical Mixing Modules:** Implementing combination processing rules capable of merging structural components (e.g., Green + Green herbs) into enhanced tier properties.
- **Finite State Machine (FSM AI Archetypes):** Refactoring scene managers to guide zombie entities across explicit state behaviors: `IDLE`, `PATROL`, `CHASE`, `STUNNED`, and `DEAD`.
- **Game Engine Graphical Visual Port (Godot / Pygame):** Stripping the CLI layer entirely to connect the fully decoupled backend Python logic directly to a graphic engine framework, mapping dictionaries to live 2D sprite telemetry and real-time screen components.
