# the following software have to be downloaded first
#  http://www.datasymbol.com/download/BarcodeScanner.exe


import win32com.client  #download from https://sourceforge.net/projects/pywin32/
import pythoncom
import time

class EvHandler:
    def OnBarcodeIn(self, _1):
        print(_1);

scanner = win32com.client.DispatchWithEvents("BarcodeScanner.Reader",EvHandler)
scanner.Visible = True

while 1:
    pythoncom.PumpWaitingMessages()
    time.sleep(10)
