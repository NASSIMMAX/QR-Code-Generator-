import qrcode
import base64
import webbrowser
import time

#Dev by NASSSIMAX 
# NASSI% HIDOUCHE
#https://t.me/exppointer
textData = input('enter your text : '.capitalize())
fileName = input('filename : '.capitalize())
pathFile = f"imgQR/{fileName}.png"


def makeQR(data, name):
    codeQr = qrcode.make(data)
    codeQr.save(name)


makeQR(textData, pathFile)

with open(pathFile, "rb") as imgCodeQr:
    dataQR = base64.b64encode(imgCodeQr.read()).decode('utf-8')

    with open("webQR.html", "w") as FileHTML:
        FileHTML.write(f"""
                               <html>
                               <body>
                               <img src='data:image/png;base64,{dataQR}'/>
                               </body>
                               </html>
                               """)
        htmlFile = "webQR.html"
        webbrowser.open(htmlFile)
