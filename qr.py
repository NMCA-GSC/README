#QR Code generator for link to PAGES website.

import qrcode

data = "" #input link to README.md file for your project

img = qrcode.make(data)
 
img.save('GSC_QR.png')
