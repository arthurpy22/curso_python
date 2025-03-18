import qrcode
import qrcode.constants

celular_numero = input("digite o numero do celular: ")
mensagem = input("digite a mensagem: ")

data = f'https://wa.me/5592{celular_numero}?text={mensagem}'

qr = qrcode.QRCode(
    version= 1,
    error_correction= qrcode.constants.ERROR_CORRECT_L,
    box_size= 5,
    border= 2
)


qr.add_data(data)

qr.make(fit= True)

imagem = qr.make_image(fill_color="black",back_color="white")

imagem.save("qrcode.png")




print(f"gerando qr code para o numero de {celular_numero} e a mensagem '{mensagem}'...")