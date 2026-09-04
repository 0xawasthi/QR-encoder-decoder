from validator import QRValidator
from encoder import QREncoder
from decoder import QRDecoder
from qr_code import QRCode

class QRApplication:
    def __init__(self):
        self.encoder = QREncoder()
        self.decoder = QRDecoder()
        self.validator = QRValidator()

    def create_qr(self, data: str, filename: str) -> str:
        if not self.validator.validate_data(data):
            raise ValueError("Invalid QR code data")

        if not self.validator.validate_filename(filename):
            raise ValueError("Invalid filename")

        qr_code = QRCode(data, filename)

        return self.encoder.encode(qr_code)

    def decode_qr(self, image_path: str) -> str | None:
        if not self.validator.validate_image_path(image_path):
            raise ValueError("Invalid image path")

        return self.decoder.decode(image_path)

