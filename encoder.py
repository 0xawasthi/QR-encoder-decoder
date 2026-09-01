from qr_code import QRCode

import qrcode

from pathlib import Path


class QREncoder:

    def encode(self, qr_code: QRCode) -> str:
        qr = qrcode.make(qr_code.data)
        output_path = Path("generated_qr") / qr_code.filename
        output_path.parent.mkdir(parents=True, exist_ok=True)
        qr.save(output_path)

        return str(output_path)





































# class QREncoder:
#     def encode(self, qr_code: QRCode) -> str:
#         qr = qrcode.QRCode(
#             version=1,
#             error_correction=qrcode.constants.ERROR_CORRECT_L,
#             box_size=10,
#             border=4,
#         )
#         qr.add_data(qr_code.data)
#         qr.make(fit=True)

#         img = qr.make_image(fill_color="black", back_color="white")
#         img.save(qr_code.filename)

#         return f"QR code saved as {qr_code.filename}"