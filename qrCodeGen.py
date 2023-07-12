import qrcode
from tkinter import filedialog, Tk

data = input("Enter the data for the QR code: ")                                                        #User input
box_size = int(input("Enter box size (default 40): ") or "40")
border = int(input("Enter border size (default 3): ") or "3")
fill_color = input("Enter fill color (default black): ") or "black"
back_color = input("Enter background color (default white): ") or "white"

image_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])  #Select path

if not image_path:
    print("No file path selected.")
    exit()

qr_code = qrcode.QRCode(version=1, box_size=box_size, border=border)                                    #Generate qrcode
qr_code.add_data(data)
qr_code.make(fit=True)

qr_code.make_image(fill_color=fill_color, back_color=back_color).save(image_path)                       #Save image
print("QR code image generated successfully.")
