import sys
import os

DATA_FILE = "data.db"

class Entry:
    """
    A class representing a single entry in the database.
    """
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Database:
    def __init__(self):
        self.entries = []

    def set(self, name, value):
        """
        Set a value for a given name. If the name already exists, update its value.
        """
        for entry in self.entries:
            if entry.name == name:
                entry.value = value
                return
        self.entries.append(Entry(name, value))

    def get(self, name):
        """
        Get the value associated with a given name. Returns None if the name does not exist.
        """
        for entry in self.entries:
            if entry.name == name:
                return entry.value
        return None
    
    def load_from_disk(self):
        """
        Load entries from the data file on disk.
        """
        if not os.path.exists(DATA_FILE):
            return
        with open(DATA_FILE, 'r') as f:
            for line in f:
                line = line.strip()
                parts = line.split(" ", 2)

                if len(parts) == 3 and parts[0] == 'SET':
                    self.set(parts[1], parts[2])

    def append_to_disk(self, name, value):
        """
        Append a new entry to the data file on disk.
        """
        with open(DATA_FILE, 'a') as f:
            f.write(f'SET {name} {value}\n')
            f.flush()
            os.fsync(f.fileno())

    def main():
        db = Database()
        db.load_from_disk()

        for line in sys.stdin:
            line = line.strip()
            parts = line.split(' ', 2)

            if len(parts) == 0:
                continue

            command = parts[0].upper()

            if command == 'SET':
                if len(parts) != 3:
                    print("Usage: SET <name> <value>")
                    continue

                key = parts[1]
                value = parts[2]

                db.set(key, value)
                db.append_to_disk(key, value)
                print("OK")

            elif command == 'GET':
                if len(parts) != 2:
                    print("ERROR")
                    continue

                key = parts[1]
                value = db.get(key)
                if value is not None:
                    print(value)
                else:
                    print("NULL")

            elif command == 'EXIT':
                break

            else:
                print("ERROR")

if __name__ == "__main__":
    Database.main()