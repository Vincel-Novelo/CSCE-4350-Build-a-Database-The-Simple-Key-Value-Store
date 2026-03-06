import sys
import os

DATA_FILE = os.path.join(os.getcwd(), "data.db")

class Entry:
    """
    Represents a key-value entry.
    """
    def __init__(self, name: str, value: str):
        self.name = name
        self.value = value


class Database:
    def __init__(self):
        self.entries = []

    def set(self, name: str, value: str) -> None:
        """Set or overwrite a value."""
        for entry in self.entries:
            if entry.name == name:
                entry.value = value
                return
        self.entries.append(Entry(name, value))

    def get(self, name: str):
        """Return value or None."""
        for entry in self.entries:
            if entry.name == name:
                return entry.value
        return None

    def load_from_disk(self) -> None:
        """Load database from file."""
        if not os.path.exists(DATA_FILE):
            return

        with open(DATA_FILE, "r") as f:
            for line in f:
                parts = line.strip().split(" ", 2)

                if len(parts) == 3 and parts[0] == "SET":
                    self.set(parts[1], parts[2])

    def append_to_disk(self, name: str, value: str) -> None:
        """Append SET operation to disk."""
        with open(DATA_FILE, "a") as f:
            f.write(f"SET {name} {value}\n")
            f.flush()
            os.fsync(f.fileno())


def main():
    db = Database()
    db.load_from_disk()

    for line in sys.stdin:
        line = line.strip()

        if not line:
            print("ERROR", flush=True)
            continue

        parts = line.split(" ", 2)
        command = parts[0].upper()

        if command == "SET":
            if len(parts) != 3:
                print("ERROR", flush=True)
                continue

            key, value = parts[1], parts[2]

            db.set(key, value)
            db.append_to_disk(key, value)

            print("OK", flush=True)

        elif command == "GET":
            if len(parts) != 2:
                print("ERROR", flush=True)
                continue

            key = parts[1]
            value = db.get(key)

            if value is None:
                print("NULL", flush=True)
            else:
                print(value, flush=True)

        elif command == "EXIT":
            break

        else:
            print("ERROR", flush=True)


if __name__ == "__main__":
    main()
