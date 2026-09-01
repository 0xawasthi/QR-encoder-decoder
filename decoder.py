import cv2

class QRDecoder:

    def decode(self, image_path: str) -> str | None:
        # Load the image
        image = cv2.imread(image_path)

        # Check if image was loaded successfully
        if image is None:
            return None

        # Initialize the QRCode detector
        detector = cv2.QRCodeDetector()

        # Detect and decode the QR code
        data, points, _ = detector.detectAndDecode(image)

        if data:
            return data

        return None