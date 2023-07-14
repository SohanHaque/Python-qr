import sys
import qrcode
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QColorDialog, QFileDialog

class QRCodeGenerator(QWidget):
    def __init__(qr_gen):
        super().__init__()
        qr_gen.initUI()

    def initUI(qr_gen):
        qr_gen.setWindowTitle('QR Code Generator')
        qr_gen.setGeometry(300, 300, 400, 200)

        qr_gen.data_label = QLabel('Data:', qr_gen)
        qr_gen.data_label.move(20, 20)

        qr_gen.data_input = QLineEdit(qr_gen)
        qr_gen.data_input.setGeometry(100, 20, 200, 20)

        qr_gen.box_size_label = QLabel('Box Size:', qr_gen)
        qr_gen.box_size_label.move(20, 50)

        qr_gen.box_size_input = QLineEdit(qr_gen)
        qr_gen.box_size_input.setGeometry(100, 50, 200, 20)

        qr_gen.border_label = QLabel('Border:', qr_gen)
        qr_gen.border_label.move(20, 80)

        qr_gen.border_input = QLineEdit(qr_gen)
        qr_gen.border_input.setGeometry(100, 80, 200, 20)

        qr_gen.fill_color_button = QPushButton('Fill Color', qr_gen)
        qr_gen.fill_color_button.setGeometry(20, 110, 100, 25)
        qr_gen.fill_color_button.clicked.connect(qr_gen.select_fill_color)

        qr_gen.back_color_button = QPushButton('Background Color', qr_gen)
        qr_gen.back_color_button.setGeometry(130, 110, 150, 25)
        qr_gen.back_color_button.clicked.connect(qr_gen.select_background_color)

        qr_gen.generate_button = QPushButton('Generate QR Code', qr_gen)
        qr_gen.generate_button.setGeometry(20, 150, 150, 30)
        qr_gen.generate_button.clicked.connect(qr_gen.generate_qr_code)

        qr_gen.show()

    def select_fill_color(qr_gen):
        color = QColorDialog.getColor()
        if color.isValid():
            qr_gen.fill_color = color.name()

    def select_background_color(qr_gen):
        color = QColorDialog.getColor()
        if color.isValid():
            qr_gen.background_color = color.name()

    def generate_qr_code(qr_gen):
        data = qr_gen.data_input.text()
        box_size = int(qr_gen.box_size_input.text() or "40")
        border = int(qr_gen.border_input.text() or "3")
        fill_color = qr_gen.fill_color or "black"
        back_color = qr_gen.background_color or "white"

        image_path, _ = QFileDialog.getSaveFileName(qr_gen, 'Save QR Code', '', 'PNG files (*.png)')

        if image_path:
            qr_code = qrcode.QRCode(version=1, box_size=box_size, border=border)
            qr_code.add_data(data)
            qr_code.make(fit=True)

            qr_image = qr_code.make_image(fill_color=fill_color, back_color=back_color)
            qr_image.save(image_path)
            print("QR code image generated successfully.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QRCodeGenerator()
    sys.exit(app.exec_())
