from flask import Flask
import random
import time

app = Flask(__name__)

ras_ger = ["Her gün teknoloji bağımlılığının sayısı artmaktadır.","Her gün bir sürü karbondioksit atmosfere saçılıyor.","Teknoloji bağımlılığının çeşitleri; sosyal medya, alışveriş ve oyun bağımlılığıdır.","Teknoloji bağımlısı olan insanlar dijital araç olmazsa saldırganlaşabilirler.","Ozon Tabakası kırılırsa zararlı Güneş ışınları Dünya'ya gelebilir.", "Bence o telefonu bırakıp resim yapmak, futbol oynamak, yürüyüş yapmak... gibi şeyler yapmalısın. 5 dk yok, HEMEN!","Telefonunu elinden bırakmayan insanların dikkati, telefon kullanmayan insanların dikkatinden çok daha az. Sen bilirsin!","Teknolojik bağımlılıktan mustarip olan çoğu kişi, kendilerini şebeke kapsama alanı dışında bulduklarında veya cihazlarını kullanamadıkları zaman yoğun stres yaşarlar.","2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor.","Teknolojik bağımlılık çalışması, modern bilimsel araştırmanın en ilgili alanlarından biridir.","2019'da yapılan bir araştırmaya göre, insanların %60'ından fazlası akıllı telefonlarındaki iş mesajlarına işten ayrıldıktan sonraki 15 dakika içinde yanıt veriyor.","Teknolojik bağımlılıkla mücadele etmenin bir yolu, zevk veren ve ruh halini iyileştiren faaliyetler aramaktır.","Elon Musk, sosyal ağların içeriği görüntülemek için mümkün olduğunca fazla zaman harcamamız için bizi platformun içinde tutmak üzere tasarlandığını iddia ediyor.","Elon Musk ayrıca sosyal ağların düzenlenmesini ve kullanıcıların kişisel verilerinin korunmasını savunmaktadır. Sosyal ağların hakkımızda büyük miktarda bilgi topladığını ve bu bilgilerin daha sonra düşüncelerimizi ve davranışlarımızı manipüle etmek için kullanılabileceğini iddia ediyor.","Sosyal ağların olumlu ve olumsuz yanları vardır ve bu platformları kullanırken her ikisinin de farkında olmalıyız."]
cf = ["Tura","Yazı"]

@app.route("/")
def anasayfa():
    return '<h1>Burası bir eğlence sitesi ama bu adrese tıklayarak gerçek şeyler öğrenebilirsin!</h1>''<a href = /ras_ger><h1>Rastgele Gerçekler</h1></a>','<p>ne vr</p>'

@app.route("/ras_ger")
def rastgele_gerçekler():
    return f"<h3>{random.choice(ras_ger)}    (Sayfayı Yenile)</h3>"

@app.route("/yazı_tura")
def yazı_tura():
    return f'<h3>{random.choice(cf)}</h3>'

@app.route("/sür_res")
def köpek():
    return "<img src=https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSPVHZVBdJIE-1Vjwdjf4Vsbocg5vZUqEUsxA&usqp=CAU height=742 widht=600 alt=404 Not Found>"

app.run(debug=True)
