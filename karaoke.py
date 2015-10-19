#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import urllib.request
import json

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler


class KaraokeLocal():
    def __init__(self, fichero):
        "Inicializador"
        parser = make_parser()
        cHandler = SmallSMILHandler()
        parser.setContentHandler(cHandler)
        try:
            parser.parse(open(fichero))
            self.lista = cHandler.get_tags()
        except IOError:
            sys.exit("Error del fichero")

    def __str__(self):
        "Cadenas"
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

    def do_local(self):
        "Descarga de ficheros"
        for atributos in self.lista:
            dic = atributos[1]
            for clave in dic.keys():
                if dic[clave].split(':')[0] == "http":
                    urllib.request.urlretrieve(dic[clave], dic[clave].split('/')[-1])
                    dic[clave] = dic[clave].split('/')[-1]

    def to_json(self, fichero):
        "Pasar fichero SMIL a JSON"
        new_json = json.dumps(self.lista)
        nombre_fichero = fichero.split('.')[0] + '.json'
        with open(nombre_fichero, 'w') as fichero_json:
            json.dump(new_json, fichero_json)


if __name__ == "__main__":

    if len(sys.argv) == 2:
        fichero = sys.argv[1]
        karaoke = KaraokeLocal(fichero)
        print(karaoke.__str__())
        karaoke.to_json(fichero)
        karaoke.do_local()
        karaoke.to_json("local.json")
        print(karaoke.__str__())
    else:
        sys.exit("Usage: python3 karaoke.py file.smil")
