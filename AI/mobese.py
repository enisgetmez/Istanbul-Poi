#!/usr/bin/env python
# -*- coding: utf-8 -*-

turistik = {"0":"https://livestream.ibb.gov.tr/ibb_live/anadoluhisarihq.stream/chunklist_w520532298.m3u8",
			"1":"https://livestream.ibb.gov.tr/ibb_live/bagdat1hq.stream/chunklist_w124414932.m3u8",
			"2":"https://livestream.ibb.gov.tr/ibb_live/bagdat2hq.stream/chunklist_w1900638056.m3u8",
			"3":"https://livestream.ibb.gov.tr/ibb_live/beyazitkulesi1hq.stream/chunklist_w1764978367.m3u8",
			"4":"https://livestream.ibb.gov.tr/ibb_live/beyazitmeydanihq.stream/chunklist_w206362085.m3u8",
			"5":"https://livestream.ibb.gov.tr/ibb_live/buyukcamlicahq.stream/chunklist_w1989551093.m3u8",
			"6":"https://livestream.ibb.gov.tr/ibb_live/dragoshq.stream/chunklist_w2082685272.m3u8",
			"7":"https://livestream.ibb.gov.tr/ibb_live/emirganhq.stream/chunklist_w1889662720.m3u8",
			"8":"https://livestream.ibb.gov.tr/ibb_live/galatahq.stream/chunklist_w1992867719.m3u8",
			"9":"https://livestream.ibb.gov.tr/ibb_live/hidivhq.stream/media_w1611798596_2635.ts",
			"10":"https://livestream.ibb.gov.tr/ibb_live/hidiv2hq.stream/chunklist_w634449414.m3u8",
			"11":"https://livestream.ibb.gov.tr/ibb_live/kadikoyhq.stream/chunklist_w197913577.m3u8",
			"12":"https://livestream.ibb.gov.tr/ibb_live/karakoyhq.stream/chunklist_w211960355.m3u8",
			"13":"https://livestream.ibb.gov.tr/ibb_live/kapalicarsihq.stream/chunklist_w1800530232.m3u8",
			"14":"https://livestream.ibb.gov.tr/ibb_live/ibb_live_kiz_kulesihq.stream/chunklist_w1351129564.m3u8",
			"15":"https://livestream.ibb.gov.tr/ibb_live/kucukcamlicahq.stream/chunklist_w758964126.m3u8",
			"16":"https://livestream.ibb.gov.tr/ibb_live/metrohanhq.stream/chunklist_w422027999.m3u8",
			"17":"https://livestream.ibb.gov.tr/ibb_live/misircarsisihq.stream/chunklist_w1672547810.m3u8",
			"18":"https://livestream.ibb.gov.tr/ibb_live/miniaturkhq.stream/chunklist_w120921941.m3u8",
			"19":"https://livestream.ibb.gov.tr/ibb_live/pierrelotihq.stream/chunklist_w290888003.m3u8",
			"20":"https://livestream.ibb.gov.tr/ibb_live/salacakhq.stream/chunklist_w1143889306.m3u8",
			"21":"https://livestream.ibb.gov.tr/ibb_live/sarachane2hq.stream/chunklist_w1585667999.m3u8",
			"22":"https://livestream.ibb.gov.tr/ibb_live/sepetcilerkasrihq.stream/chunklist_w466958370.m3u8",
			"23":"https://livestream.ibb.gov.tr/ibb_live/sultanahmet2hq.stream/chunklist_w495415802.m3u8",
			"24":"https://livestream.ibb.gov.tr/ibb_live/taksimhq.stream/chunklist_w1628467753.m3u8",
			"25":"https://livestream.ibb.gov.tr/ibb_live/ulusparkihq.stream/chunklist_w387102.m3u8",
			"26":"https://livestream.ibb.gov.tr/ibb_live/istiklalcadhq.stream/chunklist_w1452047006.m3u8",
			"27":"https://livestream.ibb.gov.tr/ibb_live/istiklalcad2hq.stream/chunklist_w669624866.m3u8"}


sehir = {"0":"http://ibb-media1.ibb.gov.tr:1935/live/223.stream/chunklist_w1088399288.m3u8", #mecidiyeköy
	"1":"http://ibb-media1.ibb.gov.tr:1935/live/344.stream/chunklist_w1837373499.m3u8", #FSM Köprüsü
	"2":"http://ibb-media1.ibb.gov.tr:1935/live/338.stream/chunklist_w1878212776.m3u8", #268-s yolu asiyan
	"3":"http://ibb-media4.ibb.gov.tr:1935/live/43.stream/chunklist_w92679156.m3u8",#beşiktaş
	"4":"http://ibb-media1.ibb.gov.tr:1935/live/282.stream/chunklist_w1481500069.m3u8", #sirkeci
	"5":"http://ibb-media4.ibb.gov.tr:1935/live/66.stream/chunklist_w1412092558.m3u8", #Acıbadem Köprüsü
	"6":"hhttp://ibb-media1.ibb.gov.tr:1935/live/201.stream/chunklist_w1783199883.m3u8", #Kadıköy Rıhtım
	"7":"http://ibb-media1.ibb.gov.tr:1935/live/202.stream/chunklist_w2146144758.m3u8", #Kağıthane
	"8":"http://ibb-media2.ibb.gov.tr:1935/live/664.stream/chunklist_w814352611.m3u8",#Çavuşbaşı
	"9":"http://ibb-media2.ibb.gov.tr:1935/live/648.stream/chunklist_w109196455.m3u8", #dünya gazetesi
	"10":"http://ibb-media4.ibb.gov.tr:1935/live/13.stream/chunklist_w779799182.m3u8", #Atatürk Havalimanı
	"11":"http://ibb-media4.ibb.gov.tr:1935/live/81.stream/chunklist_w660600761.m3u8", # 15 temmuz şehitler köprüsü
	"12":"http://ibb-media1.ibb.gov.tr:1935/live/174.stream/chunklist_w1362957790.m3u8", #Bahçe Taksim
	"13":"http://ibb-media4.ibb.gov.tr:1935/live/45.stream/chunklist_w1312528785.m3u8", #Eyüp Feshane
	"14":"http://ibb-media4.ibb.gov.tr:1935/live/114.stream/chunklist_w957944218.m3u8", # harem ido
	"15":"http://ibb-media2.ibb.gov.tr:1935/live/1021.stream/chunklist_w1274393475.m3u8", #H.U Tuneli beykoz
}

kameraturu = int(input("Hangi kamera türünü kullanmak istiyorsunuz?\n (1)Turistik Kamera\n (2) Şehir ve Trafik Kameraları\n "))

def secili():
	if(kameraturu == 1):
		turkamsec  = str(input("İşlem yapmak istediğiniz Kamerayı Seçin\n(0)Anadolu Hisarı\n (1)Bağdat Caddesi \n(2)Bağdat Caddesi 2 \n(3)Beyazit Kulesi\n(4)Beyazit Meydan \n(5)Büyük Çamlıca \n(6)Dragos\n(7)Emirgan \n(8)Galata Kulesi\n(9)Hidiv Kasrı 1 \n(10)Hidiv Kasrı 2 \n(11)Kadıköy \n(12)Karaköy \n(13)Kapalı Çarşı \n(14)Kız Kulesi \n(15)Küçük Çamlıca\n(16)Metrohan \n(17)Mısır Çarşısı \n(18)Miniatürk \n(19)Pierre Loti \n(20)Salacak \n(21)Saraçhane \n(22)Sepetçiler Kasrı \n(23)Sultanahmet \n(24)Taksim \n(25)Ulus Parkı \n(26)İstiklal Caddesi 1\n(27)İstiklal Caddesi 2\n "))
		secilikamera = turistik[turkamsec]
		return secilikamera
	elif(kameraturu == 2):
		turkamsec = str(input("İşlem yapmak istediğiniz kamerayı seçin\n(0)Mecidiyeköy\n(1)FSM Köprüsü\n(2)268-s yolu asiyan\n(3)Beşiktaş\n(4)sirkeci\n(5)Acıbadem Köprüsü\n(6)Kadıköy Rıhtım\n(7)Kağıthane\n(8)Çavuşbaşı\n(9)Dünya Gazetesi\n(10)Atatürk Havalimanı\n(11)15 temmuz şehitler köprüsü\n(12)Taksim Bahçe\n(13)Eyüp Feshane\n(14)harem ido\n(15)H.U Tuneli Beykoz\n"))
		secilikamera = sehir[turkamsec]
		return secilikamera
