# Volkswagen Yeni Passat Sentiment Analizi Senaryosu

## Senaryo Açıklaması

**X** adlı araç firması yeni bir **Y** modelini satışa çıkarmıştır. **Twitter**
gönderilerinden yeni çıkan bu model ile ilgili konum bazlı müşteri
memnuniyeti ölçümü yapılmak istenmektedir.
Sürecin nasıl ilerleyeceğini açıklayınız.

---

## Adım 1: Problem Tanımlama

- Müşteri yorumlarının anlık olarak mı takip edileceği yoksa periyotlar şeklinde
her gün/hafta/ay alınan tweetler toplanıp analiz edileceği belirlenmelidir.
- Ardından analiz edilecek veriden ne beklendiği tespit edilmelidir. Müşterinin
model hakkında yorumların pozitif veya negatif olduğunun belirlenmesi yeterli
olacak mıdır yoksa yorum pozitif ise modelin neyinin övüldüğü
negatif ise modelin neyin yerildiği de belirlenmeli midir?
- Yapay zeka problem dahiline alınmalı mıdır yoksa atılan yorumlar birkaç kural
ile sınıflandırılabilecek kadar basit midir? Hibrit bir sistem kurulması makul
müdür?
- Development Enviroment belirlenmelidir. [AWS](https://aws.amazon.com/tr/)
gibi bulut sağlayıcıları üstünde mi kodlama yapılacaktır yoksa lokal makineler
üstünde mi? Bulut sağlayıcılarının sağladıkları diğer servisler kullanılarak
daha hızlı bir sonuç alınabilir ancak lokal geliştirme daha az maliyetli
olacaktır.
- 3. parti servis sağlayıcıları problemi bünyede bulundurulan ya da yeni
kurulacak veri bilimi ekibinden daha hızlı ve daha ucuza çözebilir mi? Pazar
araştırılmalıdır.


## Adım 2: Veri Toplama

- Bu adımda firmanın geriye dönük araç modellerine ait müşteri yorumu
verilerinin kayıtlı olup olmadığı, bu verilerin ulaşılabilirliği, güvenilirliği
ve temizliği incelenmelidir.
- Analiz **Twitter** üzerinden yapılacağından **Twitter** üstündeki verileri
kazınması avantaj sağlayacaktır. Ayrıca rakip firmalara yazılan tweetlerde
veri kümesini zenginleştirmekte faydalı olur. Twitter kazınması için
[Tweepy](https://www.tweepy.org/) kullanılabilir. **Tweepy** tweetlerin içindeki
konum bilgisini de aldığından birçok probleme çözüm olabilir.
- 3. parti sitelerden veri çekilmesi faydalı olabilir.
[ŞikayetVar](https://www.sikayetvar.com/) gibi sitelerden etiketli sayılabilecek
veriler çekilebilir.

## Adım 3: Veri Temizliği

- Veri içindeki yazım bozuklukları, bağlam dışında kalan yorumlar, anlam ifade
etmeyen cümleler incelenelerek temizlenmelidir.
- Noktalama işaretleri, numaralar, emojiler vb. öğeler sürece katılmalı mı
belirlenmeli duruma göre çıkarılmalıdır.
- Yazım bozuklukları düzeltilebilir bir seviyede midir incelenmeli eğer
düzeltilebilecek durumdalarsa normalize edilmeli değil ise
veriden çıkarılmalılardır.
- Açık kaynak kütüphaneler kullanılarak verinin normalize edilmesi
kolaylaştırılabilir.Örneğin
[Zemberek](https://github.com/ahmetaa/zemberek-nlp/tree/master/normalization)
bu durum için uygun olabilir.
- Veri yapay zeka modelinin eğitimine ve etiketlenmeye hazır hale
getirilmelidir.

## Adım 4: Veri Etiketlenmesi

- Bu adım manuel şekilde yapılabilir. Yaz ya da kış dönemi stajyerleri
alınıp bu işe konulabilir. Açık kaynak bir etiketleme arayüzü etiketleme hızının
artmasında faydalı olacaktır. [Doccano](https://github.com/doccano/doccano)
daha önceden kullanmış olduğum etkili bir uygulamadır.
- Veriyi etiketleyecek kurallar yazılabilir. Örneğin yorum içerisinde
mutlu, memnun, iyi, :) vb. kelimeler geçiyorsa yorum pozitif olarak;
kötü, sıkıntı, :( vb. kelimeler geçiyorsa negatif olarak etiketlenebilir. Ancak
kurallar dikkatli yazılmalıdır. Zira bu yöntem ile veri çöplüğüne yol açmak
oldukça olasıdır.
- [AWS SageMaker Ground Truth](https://aws.amazon.com/tr/sagemaker/groundtruth/)
gibi 3. parti veri etiketleme yöntemleri kullanılabilir.
- Daha önce bünyede oluşturulmuş bir yapay zeka modeli ile veriler
etiketlenebilir. Ardından etiketlenen veri tarafından yeni bir model eğitilirek
süreç tekrarlanabilir.
- Yerel 3. parti yapay zeka servis sağlayıcıları kullanılarak veri
etiketlenebilir ve çoğunluk oylaması yapılarak daha sağlam bir sonuca
ulaşılabilir.
- Veri yabancı dile çevrilerek dünya çapındaki yapay zeka servis sağlayıcılarına
etiketlettirilebilir.

## Adım 5: Yapay Zeka Modeli Eğitimi

- Açıklamaya çok gerek olmayan bir bölüm. Etiketlenmiş veri alınarak farklı
yapay zeka algoritmaları denenir ve en iyi sonucu veren model seçilir.
- Verinin boyutuna ve alınan sonuca göre Deep Learning işin içine katılabilir.
- Modelin sınıflandırmakta zorluk çektiği yorumlar incelenerek kurallar
geliştirilebilir.
- Birden fazla model bir arada kullanılarak sonuç alınabilir.

## Adım 6: Yapay Zeka Modelinin Servisleştirilmesi

- Eğitilen yapay zeka modeli tercih edilen teknoloji ile ve kararlaştırılan
standartlar içinde web servisi haline dönüştürülür.
- Response şekli seçilir. XML/Json vb.
- Servis konteynırlaştırılıp sunucuda gerekli cluster'a taşınır.
- Cluster dahilinde yapay zeka servisine gelen request ve servisten çıkan
responseları loglayan bir servis olması önemli bir noktadır.
- Gelen requestler servise geçmeden önce bir API Gateway ile kontrol edilip,
loglanıp, duruma göre yönlendirilebilir.

## Adım 7: Güncelleme ve Geliştirme

- Modelin çıktıları incelenip modelin zorlandığı, başarısız olduğu noktalar
incelenir.
- Eksik noktalar kural tabanlı bir sistem ile tamamlanabilir.
Bu durum yeni bir model eğitme sürecine tercih edilebilir.
- Yeni etiketlenen veri, servis çıktıları ve mevcut halde kullanılan veri
ile tekrar bir model eğitilebilir.
- Servis problemi istenen şekilde çözüyor mu kontrol edilir. Duruma göre ek
servisler eklenebilir ya da başka bir çözüm yoluna gidilebilir.
- Servisin ölçeklenmesi ve performansı test edilir ve güncellenir.
- Tüm süreç tekrarlanır.
