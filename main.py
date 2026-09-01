from qr_code import QRCode
from encoder import QREncoder
from decoder import QRDecoder
from validator import QRValidator

print("QRCode Encoder and Decoder")

data = input("Enter the data/URL for the QR code: ")
filename = input("Enter the filename for the QR code image (e.g., 'qrcode.png'): ")

qr = QRCode(data, filename)
validator = QRValidator()
if not validator.validate_data(qr.data):
    print("Invalid QR code data")
    exit()

encoder = QREncoder()
result = encoder.encode(qr)

print(f"Encoded: {result}")

decoder = QRDecoder()
decoded_data = decoder.decode("generated_qr/hello.png")

print(f"Decoded: {decoded_data}")

validator = QRValidator()

print(validator.validate_data("Hello Python"))
print(validator.validate_data(""))
print(validator.validate_data("   "))
print(validator.validate_data("   Hello   "))

