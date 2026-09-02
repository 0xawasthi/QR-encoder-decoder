from qr_application import QRApplication

app = QRApplication()

# Create QR
qr_path = app.create_qr("Hello OOP", "oop.png")
print(f"QR created: {qr_path}")

# Decode QR
data = app.decode_qr(qr_path)
print(f"Decoded: {data}")