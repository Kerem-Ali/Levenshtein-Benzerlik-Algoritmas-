from PyQt5 import QtWidgets,uic
import sys
from levenshtein_mesafesi_benzerlik_algoritmasi import *


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui,self).__init__()
        
        
        self.setUI()
        
        
        
        

    def setUI(self):
        uic.loadUi("myui.ui",self)
        self.buton.clicked.connect(self.hesapla)
        



    def hesapla(self):
        kelime_1=self.kelime_1.text()
        kelime_2=self.kelime_2.text()
        
        max_len=max(len(kelime_1),len(kelime_2))
        

        kelime_1=normalize(kelime_1,max_len)
        kelime_2=normalize(kelime_2,max_len)
        mesafe=LevenshteinMesafesi(kelime_1,kelime_2)
        benzerlik_oran=(max_len-mesafe)/max_len


        self.text_1.setText(f"'{kelime_1}' ve '{kelime_2}' arasındaki\nLevenshtein Mesafesi: {mesafe}")
        self.text_2.setText(f"Benzerlik Oranı:{benzerlik_oran}")
            
            


app=QtWidgets.QApplication(sys.argv)
window=Ui()
window.show()
app.exec_()
