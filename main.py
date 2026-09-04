from qr_history import QRHistory

history = QRHistory()

history.add_entry("encode", "Hello OOP", "oop.png")
history.add_entry("decode", "Hello OOP", "oop.png")

print(history.get_history())

history.save_history()