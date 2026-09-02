from pathlib import Path

class QRValidator:

    def validate_data(self, data: str) -> bool:
        return bool(data.strip())

    def validate_filename(self, filename: str) -> bool:
        allowed_extensions = {".png", ".jpg", ".jpeg"}
        path = Path(filename)
        return path.suffix.lower() in allowed_extensions and bool(path.stem.strip())

    def validate_image_path(self, image_path: str) -> bool:
        path = Path(image_path)
        return path.exists() and path.is_file() and path.suffix.lower() in {".png", ".jpg", ".jpeg"}