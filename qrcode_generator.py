import qrcode

def generate_qrcode(text):

    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.ERROR_CORRECT_L,
        box_size = 10,
        border = 4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("google.png")
    print("Your QRcode has been Generated! Check your file.")
    print("")    #for spacing

url = input("Enter URL to generate QRcode: ")
print("")    #for spacing
generate_qrcode(url)