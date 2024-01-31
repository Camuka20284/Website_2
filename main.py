from flask import Flask
import random

app = Flask(__name__)

ras_fot = ["<img src=https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSPVHZVBdJIE-1Vjwdjf4Vsbocg5vZUqEUsxA&usqp=CAU height=642 widht=500 alt=404 Not Found>","<img src=https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR9bvY2ufZObLdApRIErq1K63Mc28jt4VSbgQ&usqp=CAU height=550 widht=550 alt=404 Not Found>","<img src=https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR0E3jXY1n5itX94Cz8WSqlXPV17xL3DWi99w&usqp=CAU height=632 widht=500 alt=404 Not Found>"]
ras_ger_tr = ["Her gün teknoloji bağımlılığının sayısı artmaktadır.","Her gün bir sürü karbondioksit atmosfere saçılıyor.","Teknoloji bağımlılığının çeşitleri; sosyal medya, alışveriş ve oyun bağımlılığıdır.","Teknoloji bağımlısı olan insanlar dijital araç olmazsa saldırganlaşabilirler.","Ozon Tabakası kırılırsa zararlı Güneş ışınları Dünya'ya gelebilir.", "Bence o telefonu bırakıp resim yapmak, futbol oynamak, yürüyüş yapmak... gibi şeyler yapmalısın. 5 dk yok, HEMEN!","Telefonunu elinden bırakmayan insanların dikkati, telefon kullanmayan insanların dikkatinden çok daha az. Sen bilirsin!","Teknolojik bağımlılıktan mustarip olan çoğu kişi, kendilerini şebeke kapsama alanı dışında bulduklarında veya cihazlarını kullanamadıkları zaman yoğun stres yaşarlar.","2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor.","Teknolojik bağımlılık çalışması, modern bilimsel araştırmanın en ilgili alanlarından biridir.","2019'da yapılan bir araştırmaya göre, insanların %60'ından fazlası akıllı telefonlarındaki iş mesajlarına işten ayrıldıktan sonraki 15 dakika içinde yanıt veriyor.","Teknolojik bağımlılıkla mücadele etmenin bir yolu, zevk veren ve ruh halini iyileştiren faaliyetler aramaktır.","Elon Musk, sosyal ağların içeriği görüntülemek için mümkün olduğunca fazla zaman harcamamız için bizi platformun içinde tutmak üzere tasarlandığını iddia ediyor.","Elon Musk ayrıca sosyal ağların düzenlenmesini ve kullanıcıların kişisel verilerinin korunmasını savunmaktadır. Sosyal ağların hakkımızda büyük miktarda bilgi topladığını ve bu bilgilerin daha sonra düşüncelerimizi ve davranışlarımızı manipüle etmek için kullanılabileceğini iddia ediyor.","Sosyal ağların olumlu ve olumsuz yanları vardır ve bu platformları kullanırken her ikisinin de farkında olmalıyız."]
cf_tr = ["Tura","Yazı"]

@app.route("/")
def anasayfa():
    return '<a href = /tr><h1>Türkçe</h1></a>' '<a href = /en><h1>English</h1></a>' '<a href = /es><h1>Español</h1></a>' '<a href = /it><h1>Italiano</h1></a>' '<a href = /de><h1>Deutsch</h1></a>' '<a href = /fr><h1>Francais</h1></a>'

@app.route("/tr")
def anasayfa_tr():
    return '<h1>Burası bir eğlence sitesi!</h1>''<a href = /tr_ras_ger><h1>Rastgele Gerçekler</h1></a>' '<a href = /tr_yazı_tura><h1>Yazı - Tura</h1></a>' '<a href = /tr_sür_res><h1>Sürpriz Resim</h1></a>'

@app.route("/tr_ras_ger")
def rastgele_gerçekler_tr():
    return f"<h3>{random.choice(ras_ger_tr)}    (Sayfayı Yenile)</h3>"

@app.route("/tr_yazı_tura")
def yazı_tura_tr():
    return f'<h3>{random.choice(cf_tr)}</h3>'

@app.route("/tr_sür_res")
def aslan_tr():
    return random.choice(ras_fot)

ras_ger_en = ["The number of technology addictions is increasing every day.","A lot of carbon dioxide is scattered into the atmosphere every day.","Types of technology addiction are social media, shopping and gaming addiction.","People who are addicted to technology can become aggressive if they do not have digital tools.","Ozone If its layer breaks, harmful Sun rays may reach the Earth.", "I think you should put down that phone and do things like painting, playing football, walking... No 5 minutes, NOW!","The attention of people who don't put their phones down is the attention of people who don't use phones. much less than your attention. You know!","Most people who suffer from technological addiction experience intense stress when they find themselves out of network coverage or cannot use their devices.","According to a 2018 study, 50% of people aged 18-34 More than 60% of people consider themselves addicted to their smartphones.","The study of technological addiction is one of the most relevant areas of modern scientific research.","According to a 2019 study, more than 60% of people access work messages on their smartphones within 15 minutes of leaving work responds in.","One way to combat technological addiction is to seek activities that provide pleasure and improve mood.","Elon Musk claims that social networks are designed to keep us on the platform so that we spend as much time as possible viewing content." ,"Elon Musk also advocates the regulation of social networks and the protection of users' personal data. It claims that social networks collect large amounts of information about us, which can then be used to manipulate our thoughts and behavior.","Social networks have their positive and negative sides, and we should be aware of both when using these platforms."]
cf_en = ["Heads","Tails"]

@app.route("/en")
def anasayfa_en():
    return '<h1>This is an entertainment site!</h1>''<a href = /en_ras_ger><h1>Random Facts</h1></a>' '<a href = /en_yazı_tura><h1>Heads - Tails</h1></a>' '<a href = /en_sür_res><h1>Surprise Photo</h1></a>'

@app.route("/en_ras_ger")
def rastgele_gerçekler_en():
    return f"<h3>{random.choice(ras_ger_en)}    (Refresh the page)</h3>"

@app.route("/en_yazı_tura")
def yazı_tura_en():
    return f'<h3>{random.choice(cf_en)}</h3>'

@app.route("/en_sür_res")
def aslan_en():
    return random.choice(ras_fot)

ras_ger_es = ["El número de adicciones a la tecnología aumenta cada día.","Cada día se esparce una gran cantidad de dióxido de carbono en la atmósfera.","Los tipos de adicción a la tecnología son las redes sociales, las compras y los juegos.","Las personas que son adictas a la tecnología pueden volverse agresivos si no cuentan con herramientas digitales.","Ozono Si se rompe su capa, los dañinos rayos del Sol pueden llegar a la Tierra.", "Creo que deberías dejar ese teléfono y hacer cosas como pintar, jugar al fútbol, caminando... ¡No 5 minutos, AHORA!","La atención de la gente que no cuelga el teléfono es la atención de la gente que no usa el teléfono. Mucho menos que la tuya. ¡Ya sabes!","La mayoría Las personas que sufren adicción a la tecnología experimentan un estrés intenso cuando se encuentran fuera de la cobertura de la red o no pueden utilizar sus dispositivos. sus teléfonos inteligentes. responde en.","Una forma de combatir la adicción a la tecnología es buscar actividades que proporcionen placer y mejoren el estado de ánimo.","Elon Musk afirma que las redes sociales están diseñadas para mantenernos en la plataforma para que pasemos el mayor tiempo posible viendo contenido." ,"Elon Musk también aboga por la regulación de las redes sociales y la protección de los datos personales de los usuarios. Afirma que las redes sociales recopilan grandes cantidades de información sobre nosotros, que luego puede usarse para manipular nuestros pensamientos y comportamiento.","Redes sociales Tienen sus lados positivos y negativos, y debemos ser conscientes de ambos al utilizar estas plataformas."]
cf_es = ["Cara","Corona"]

@app.route("/es")
def anasayfa_es():
    return '<h1>¡Este es un sitio de entretenimiento!</h1>''<a href = /es_ras_ger><h1>Hechos Aleatorios</h1></a>''<a href = /es_yazı_tura><h1>Cara - Corona</h1></a>' '<a href = /es_sür_res><h1>Imagen Sorpresa</h1></a>'

@app.route("/es_ras_ger")
def rastgele_gerçekler_es():
    return f"<h3>{random.choice(ras_ger_es)}    (Recarga la página)</h3>"

@app.route("/es_yazı_tura")
def yazı_tura_es():
    return f'<h3>{random.choice(cf_es)}</h3>'

@app.route("/es_sür_res")
def aslan_es():
    return random.choice(ras_fot)

ras_ger_it = ["Il numero delle dipendenze dalla tecnologia aumenta ogni giorno.","Ogni giorno nell'atmosfera viene dispersa molta anidride carbonica.","I tipi di dipendenza dalla tecnologia sono la dipendenza dai social media, dallo shopping e dai giochi.","Le persone dipendenti alla tecnologia può diventare aggressiva se non si hanno strumenti digitali.","L'ozono se il suo strato si rompe, i raggi solari dannosi potrebbero raggiungere la Terra.", "Penso che dovresti mettere giù quel telefono e fare cose come dipingere, giocare a calcio, camminando... No 5 minuti, ORA!","L'attenzione delle persone che non posano il telefono è l'attenzione delle persone che non usano il telefono. molto meno della tua attenzione. Lo sai!","La maggior parte le persone che soffrono di dipendenza tecnologica sperimentano uno stress intenso quando si trovano senza copertura di rete o non possono utilizzare i propri dispositivi.","Secondo uno studio del 2018, il 50% delle persone di età compresa tra 18 e 34 anni Oltre il 60% delle persone si considera dipendente da i propri smartphone.","Lo studio della dipendenza tecnologica è uno degli ambiti più rilevanti della ricerca scientifica moderna.","Secondo uno studio del 2019, più del 60% delle persone accede ai messaggi di lavoro sul proprio smartphone entro 15 minuti dall'uscita dal lavoro risponde.","Un modo per combattere la dipendenza tecnologica è cercare attività che diano piacere e migliorino l'umore.","Elon Musk sostiene che i social network sono progettati per mantenerci sulla piattaforma in modo da trascorrere quanto più tempo possibile guardando contenuto." ,"Elon Musk sostiene anche la regolamentazione dei social network e la protezione dei dati personali degli utenti. Afferma che i social network raccolgono grandi quantità di informazioni su di noi, che possono poi essere utilizzate per manipolare i nostri pensieri e comportamenti.","Social network hanno i loro lati positivi e negativi e dovremmo essere consapevoli di entrambi quando utilizziamo queste piattaforme."]
cf_it = ["Testa","Croce"]

@app.route("/it")
def anasayfa_it():
    return '<h1>Questo è un sito di intrattenimento!</h1>''<a href = /it_ras_ger><h1>Fatti casuali</h1></a>' '<a href = /it_yazı_tura><h1>Testa - Croce</h1></a>' '<a href = /it_sür_res><h1>Immagine a sorpresa</h1></a>'

@app.route("/it_ras_ger")
def rastgele_gerçekler_it():
    return f"<h3>{random.choice(ras_ger_it)}    (Ricarica la pagina)</h3>"

@app.route("/it_yazı_tura")
def yazı_tura_it():
    return f'<h3>{random.choice(cf_it)}</h3>'

@app.route("/it_sür_res")
def aslan_it():
    return random.choice(ras_fot)

ras_ger_de = ["Die Zahl der Technikabhängigkeiten nimmt täglich zu.", "Jeden Tag wird viel Kohlendioxid in die Atmosphäre gestreut." ,"Arten der Technologiesucht sind soziale Medien, Kaufsucht und Spielsucht." ,"Menschen, die süchtig sind.“ Der Umgang mit Technologie kann aggressiv werden, wenn sie nicht über digitale Werkzeuge verfügen." ,"Ozon Wenn seine Schicht bricht, können schädliche Sonnenstrahlen die Erde erreichen.", "Ich denke, Sie sollten das Telefon weglegen und Dinge wie Malen, Fußball spielen usw. tun zu Fuß... Keine 5 Minuten, JETZT!", "Die Aufmerksamkeit von Leuten, die ihre Telefone nicht weglegen, ist die Aufmerksamkeit von Leuten, die keine Telefone benutzen. viel weniger als deine Aufmerksamkeit. Du weißt schon!", "Die meisten. Menschen, die unter Techniksucht leiden, erleben starken stress, wenn sie keinen","Netzempfang haben oder ihre Geräte nicht nutzen können. „Laut einer Studie aus dem Jahr 2018 halten sich 50 % der Menschen im Alter von 18 bis 34 Jahren für mehr als 60 % süchtig","Die Untersuchung der Technologiesucht ist einer der relevantesten Bereiche der modernen wissenschaftlichen Forschung.", "Einer Studie aus dem Jahr 2019 zufolge greifen mehr als 60 % der Menschen innerhalb von 15 Minuten nach dem Verlassen der Arbeit auf geschäftliche Nachrichten auf ihren Smartphones zu antwortet in.","Eine Möglichkeit, die Technologiesucht zu bekämpfen, besteht darin, nach Aktivitäten zu suchen, die Freude bereiten und die Stimmung verbessern.","Elon Musk behauptet, dass soziale Netzwerke darauf ausgelegt sind, uns auf der Plattform zu halten, damit wir so viel Zeit wie möglich mit dem Ansehen verbringen","Außerdem setzt sich Elon Musk für die Regulierung sozialer Netzwerke und den Schutz der persönlichen Daten der Nutzer ein.","Darin wird behauptet, dass soziale Netzwerke große Mengen an Informationen über uns sammeln, die dann zur Manipulation unserer Gedanken und unseres Verhaltens genutzt werden können.","Soziale Netzwerke haben ihre positiven und negativen Seiten, und wir sollten uns bei der Nutzung dieser Plattformen beider bewusst sein."]
cf_de = ["Kopf","Zahl"]

@app.route("/de")
def anasayfa_de():
    return '<h1>Dies ist eine Unterhaltungsseite!</h1>''<a href = /de_ras_ger><h1>Zufällige Fakten</h1></a>' '<a href = /de_yazı_tura><h1>Kopf - Zahl</h1></a>' '<a href = /de_sür_res><h1>Überraschungsbild</h1></a>'

@app.route("/de_ras_ger")
def rastgele_gerçekler_de():
    return f"<h3>{random.choice(ras_ger_de)}    (Lade die Seite neu)</h3>"

@app.route("/de_yazı_tura")
def yazı_tura_de():
    return f'<h3>{random.choice(cf_de)}</h3>'

@app.route("/de_sür_res")
def aslan_de():
    return random.choice(ras_fot)

ras_ger_fr = ["Le nombre de dépendances technologiques augmente chaque jour.","Chaque jour, une grande quantité de dioxyde de carbone est dispersée dans l'atmosphère.","Les types de dépendance à la technologie sont la dépendance aux médias sociaux, aux achats et aux jeux.","Les personnes qui sont accros à la technologie peuvent devenir agressives si elles n'ont pas d'outils numériques.","Si la couche d'ozone se brise, des rayons solaires nocifs peuvent atteindre la Terre.", "Je pense que tu devrais poser ce téléphone et faire des choses comme peindre, jouer au football, marcher... Pas 5 minutes, MAINTENANT !","L'attention des personnes qui ne lâchent pas leur téléphone est beaucoup moins que l'attention de ceux qui n'utilisent pas de téléphone. Tu sais !","La plupart des personnes qui souffrent de dépendance technologique ressentent un stress intense lorsqu'elles se trouvent hors de la couverture réseau ou ne peuvent pas utiliser leurs appareils.","Selon une étude de 2018, 50% des personnes âgées de 18 à 34 ans se considèrent comme dépendantes de leur smartphone. Plus de 60% des personnes répondent aux messages professionnels sur leur smartphone dans les 15 minutes suivant leur départ du travail.","L'étude de la dépendance technologique est l'un des domaines les plus pertinents de la recherche scientifique moderne.","Selon une étude de 2019, plus de 60% des personnes accèdent aux messages professionnels sur leurs smartphones dans les 15 minutes suivant leur départ du travail.","Une façon de lutter contre la dépendance technologique est de chercher des activités qui procurent du plaisir et améliorent l'humeur.","Elon Musk affirme que les réseaux sociaux sont conçus pour nous garder sur la plateforme afin que nous passions autant de temps que possible à consulter le contenu." ,"Elon Musk plaide également pour la régulation des réseaux sociaux et la protection des données personnelles des utilisateurs. Il prétend que les réseaux sociaux collectent de grandes quantités d'informations sur nous, qui peuvent ensuite être utilisées pour manipuler nos pensées et nos comportements.","Les réseaux sociaux ont leurs côtés positifs et négatifs, et nous devrions en être conscients lors de l'utilisation de ces plateformes."]
cf_fr = ["Pile", "Face"]

@app.route("/fr")
def anasayfa_fr():
    return '<h1>Ceci est un site de divertissement!</h1>' '<a href="/fr_ras_ger"><h1>Faits aléatoires</h1></a>' '<a href="/fr_yazı_tura"><h1>Pile - face</h1></a>' '<a href="/fr_sür_res"><h1>Photo surprise</h1></a>'

@app.route("/fr_ras_ger")
def rastgele_gerçekler_fr():
    return f"<h3>{random.choice(ras_ger_fr)}    (Rafraîchissez la page)</h3>"

@app.route("/fr_yazı_tura")
def yazı_tura_fr():
    return f'<h3>{random.choice(cf_fr)}</h3>'

@app.route("/fr_sür_res")
def aslan_fr():
    return random.choice(ras_fot)


app.run(debug=True)
