# IMDb İzleme Listesi Scraper

Bu **Python** projesi, **Selenium** ve **BeautifulSoup** kütüphanelerini kullanarak kullanıcıdan alınan bilgilerle IMDb'ye otomatik giriş yapar ve **İzleme Listenizdeki (Watchlist)** içerikleri puanlarıyla birlikte çekerek terminale yazdırır. Ayrıca olası Captcha doğrulamaları için manuel müdahale seçeneği sunar.

---

## Özellikler

* **Otomatik Hesap Girişi:** Belirtilen e-posta ve şifre ile sisteme otomatik olarak giriş yapar.
* **Captcha Algılama:** Giriş esnasında Captcha çıkması durumunda tespit eder ve:
  * İşlemi duraklatır.
  * Kullanıcıdan manuel çözüm bekler.
* **İçerik Ayrıştırma:** İzleme listesindeki verileri tarayarak şu bilgileri alır:
  * İçerik Başlığı (Film/Dizi Adı)
  * IMDb Puanı
* **Temiz Çıktı:** Çekilen verileri konsola düzenli bir liste halinde yansıtır.

---

## Kurulum ve Gereksinimler

Bu projenin çalışması için bilgisayarınızda **Python 3.x** ve **Google Chrome** tarayıcısının yüklü olması gerekmektedir. 

Proje dizininde terminali açıp aşağıdaki komutu çalıştırarak gerekli kütüphaneleri (`selenium` ve `beautifulsoup4`) kurabilirsiniz:

```bash
pip install -r requirements.txt

## Kullanım

1. İndirdiğiniz veya klonladığınız proje klasöründeki Python dosyasını bir kod editörüyle açın.
2. Kodun en alt kısmında bulunan `mail` ve `password` değişkenlerine kendi IMDb giriş bilgilerinizi girin:

```python
mail = "ornek_mail@gmail.com"
password = "sifreniz123"
```

3. Terminal üzerinden Python dosyasını çalıştırın:

```bash
python imdb_scraper.py
```
