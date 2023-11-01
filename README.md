## HashTable Implementation

This Python script contains an implementation of a hash table using singly linked lists to handle collisions. It is designed to store key-value pairs, where both the keys and values are strings. The implementation is encapsulated within a `HashTable` class, and it includes several methods for performing various operations on the hash table.

### Class Structure

- `HashTable`: The main class representing the hash table.
  - Constructor: `__init__(self, n=1000)` initializes a new hash table with a specified number of slots (default is 1000).
  - `__len__(self)` returns the number of keys stored in the hash table.
  - `__setitem__(self, key, value)` assigns a value to a specific key in the hash table.
  - `__getitem__(self, key)` retrieves the value associated with a given key.
  - `__contains__(self, key)` checks if a key is present in the hash table.
  - `__iter__(self)` allows iteration through the keys in the hash table.
  - `__repr__(self)` provides a string representation of the hash table.

- `Node`: A nested class representing nodes within the linked lists.
  - Constructor: `__init__(self, key, value, next=None)` initializes a node with a key, value, and an optional reference to the next node.

### Important Notes

- This implementation assumes that all keys and values are strings.
- The code handles collisions by using singly linked lists within each hash table slot.
- The hash table dynamically resizes itself to accommodate more elements.
- The script is designed to offer a basic understanding of hash tables and can be extended for more advanced use cases.

Feel free to use and modify this implementation in your projects.
