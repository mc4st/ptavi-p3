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
            print(self.lista)
        except:
            sys.exit("Error del fichero")

if __name__ == "__main__":

    if len(sys.argv) == 2:
        fichero = sys.argv[1]
        karaoke = KaraokeLocal(fichero)
    else:
        sys.exit("Usage: python3 karaoke.py file.smil")
