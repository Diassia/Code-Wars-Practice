# You are creating an "Escape the room" game. The first step is to create a hash table called rooms that contains all of the rooms of the game. There should be at least 3 rooms inside it, each being a hash table with at least three properties (e.g. name, description, completed).

rooms = {
    1: {"name": "Library", "description": "Where you begin your escape", "completed": True},
    2: {"name": "Living Room", "description": "The second room on your escape", "completed": True},
    3: {"name": "Conservatory", "description":  "The last room on your escape", "completed": False}
}

print(rooms)