#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    " Clase para manejar fichero smil"
    def __init__(self):

        self.tags = []
        self.diccetiquetas = {"root-layout": ['width', 'height',
                              'back-groundcolor'],
                              "region": ['id', 'top', 'bottom', 'left', 'right'],
                              "img": ['src', 'region', 'begin', 'dur'],
                              "audio": ['src', 'begin', 'dur'],
                              "textstream": ['src', 'region']}

    def startElement(self, etiqueta, attrs):
        if etiqueta in self.diccetiquetas:
            tmpdicc = {}
            for atributo in self.diccetiquetas[etiqueta]:
                tmpdicc[atributo] = attrs.get(atributo, "")
            self.tags.append([etiqueta, tmpdicc])

    def get_tags(self):
        return self.tags

if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    print(cHandler.get_tags())
