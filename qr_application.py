from validator import QRValidator
from encoder import QREncoder
from decoder import QRDecoder

class QRApplication:
    def __init__(self):
        self.encoder = QREncoder()
        self.decoder = QRDecoder()
        self.validator = QRValidator()