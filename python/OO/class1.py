# Date: 2018/04/29
# Author: Sara Kammlade
# Purpose:
# Usage:

class Class1:
    __name=""
    __address=""
    phone="9705414684"
    def setname(self,newname):
        self.__name=newname
    def getname(self):
        return self.__name
    def setaddress(self,newaddress):
        self.__address=newaddress
    def getmailinglabel(self):
        return self.__name + " " + self.__address
