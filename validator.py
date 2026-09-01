class QRValidator:

    def validate_data(self, data: str) -> bool:
        return bool(data.strip())