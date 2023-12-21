import qrcode

data = "https://nmca-gsc.github.io/GSC-2023/?src=https://github.com/NMCA-GSC/GSC-2023/blob/main/README.md"

img = qrcode.make(data)
 
img.save('GSC_QR.png')