#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler

class KaraokeLocal():
    def __init__(self, fichero):
        parser = make_parser()
        cHandler = SmallSMILHandler()
        parser.setContentHandler(cHandler)
        try:
            parser.parse(open(fichero))
            self.lista = cHandler.get_tags()
        except:
            sys.exit("Error del fichero")
    def __str__(self):
        cadena_total = ""
        for atributos in self.lista:
            dic = atributos[1]
            cadena = ""
            for clave in dic.keys():
                if dic[clave] != "":
                    cadena = cadena + "\t" + clave + '="' + dic[clave] + '"'
            cadena_total = cadena_total + atributos[0] + cadena
            if atributos != self.lista[-1]:
                cadena_total = cadena_total + "\n"
        return cadena_total

if __name__ == "__main__":

    if len(sys.argv) == 2:
        fichero = sys.argv[1]
        karaoke = KaraokeLocal(fichero)
        print(karaoke)
    else:
        sys.exit("Usage: python3 karaoke.py file.smil")
