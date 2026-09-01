class QRCode:
    def __init__(self, data: str, filename: str) -> None:
        self.data = data
        self.filename = filename

    def __str__(self) -> str:
        return f"QRCode(data='{self.data}', filename='{self.filename}')"