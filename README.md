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
