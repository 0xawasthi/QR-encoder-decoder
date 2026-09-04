import json

class QRHistory:
    def __init__(self):
        self.history = []

    def add_entry(self, operation: str, data: str, filename: str) -> None:
        entry = {
            "operation": operation,
            "data": data,
            "filename": filename
        }
        self.history.append(entry)

    def get_history(self) -> list[dict]:
        return self.history

    def save_history(self, filename: str = "history.json") -> None:
        with open(filename, "w") as file:
            json.dump(self.history, file, indent=4)