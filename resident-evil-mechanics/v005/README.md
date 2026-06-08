# Game Mechanics Lab: Stackable Resource Management & Sub-menus (Version 5.0)

Version 5.0 introduces structural scalability to data handling by migrating from flat primitive arrays to dictionary-mapped key-value pairs (`dict`). This architectural shift activates full inventory stacking, live structural item extraction sub-menus, and dynamic transactional databases that purge keys upon resource depletion.

---

## 🕹️ Feature Overview
The interactive environment scales to handle complex item management, allowing characters to query, extract, and stack multi-unit resources without triggering duplicate slots.

- **Dictionary-Mapped Inventories:** Both the character storage and the room database utilize hash maps to stack variable quantities of single item types natively.
- **Active Supply Sub-menus:** Option 2 of the Game Loop is fully operational, loading a dedicated sub-menu that queries live scenario data and lists current stock balances.
- **Transactional Depletion Handling:** Resource extraction features a dynamic check where item database fields are completely deleted from the memory pool once their numeric value hits zero.
- **Input Error Layering:** Exception wrappers (try-except blocks) handle compound potential crashes, catching ValueError and IndexError states simultaneously during runtime numerical selection.

---

## 🏗️ Architectural Decisions & Implementation

### 1. Stacking Logic via Key-Value Mapping (Upsert Patterns)
Instead of appending string entries indefinitely to a standard list, item collection now follows a clean data structure lookup. When an actor collects an item, the script runs a conditional validation check: if the key does not exist inside the character storage dictionary, it initializes it; if it does exist, it increments the value integer directly. This approach replicates standard database "upsert" operations used in commercial engines.

### 2. Safeguards Against Runtime Collection Exploits
The newly activated supply sub-menu utilizes strict logic boundaries to protect data integrity:
1. It creates a temporary runtime list tracking active dictionary keys to match terminal menu input integers.
2. It validates the user's requested extraction amount against physical environment limits.
3. If valid, the script decrements the global state value and hands the validated balance down to the character class wrapper.

### 3. Absolute State Purging
To prevent empty keys from populating menus, the extraction pipeline contains an explicit check that monitors zero balances. If a resource count drops to exactly zero, the engine executes a complete deletion command on that object property field, guaranteeing clean rendering for future state evaluations.

---

## 📈 Future Improvements (Achieved in Version 6.0)
Version 5.0 successfully managed dictionary inventory counters but lacked game simulation components. The final iteration implements:
- **Ballistic Combat Calculations:** Activating active shooting operations linked with multi-variable parameters (base damage multipliers and dynamic random critical hit triggers).
- **Spatial AI Behavior Systems:** Driving enemy proximity state increments (`walk`) at the end of every active turn phase, forcing direct defensive interactions like pushbacks (`push_zombie`).
- **Dynamic Contextual UI & ANSI Color Gradients:** Upgrading the visual interface with continuous layout updates that process structural entity values and modify terminal color telemetry representing retro vitals (FINE, CAUTION, DANGER, DEATH).
