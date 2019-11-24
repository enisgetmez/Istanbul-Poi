#!/usr/bin/env python
# -*- coding: utf-8 -*-
cascades = {"0":"cascades/yaya.xml", #yaya
			"1":"cascades/car.xml", #araba
			"2":"cascades/haarcascade_frontalface_default.xml",#yuz
			"3":"cascades/yumruk.xml", #yumruk
			"4":"cascades/haarcascade_fullbody.xml",#insan
			"5":"cascades/plate.xml", #plaka
			"6":"cascades/2tekerlek.xml"
}
cascade = str(input("Hangi işlemi yapmak istersiniz? \n(0)Yaya tespit\n(1)Araba Tespit \n(2)Yüz tespit\n(3)Yumruk Tespit\n(4)İnsan Tespit\n(5)Plaka Tespit\n(6)2 tekerlekli araç tespit\n"))
def secili():
		secilicascade = cascades[cascade]
		return secilicascade