# 🔐 Hash Hesaplayıcı

Modern ve kullanıcı dostu bir hash hesaplama uygulaması. Metinlerinizi farklı hash algoritmaları ile şifreleyin.

![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)

## 📸 Ekran Görüntüsü

![Hash Hesaplayıcı](screenshot.png)

## ✨ Özellikler

- 🎯 **5 Farklı Hash Algoritması**: MD5, SHA-1, SHA-256, SHA-384, SHA-512
- ⚡ **Otomatik Hesaplama**: Yazdıkça anında hash değerini görün
- 📊 **Detaylı Bilgi**: Hash uzunluğu, bit sayısı ve algoritma bilgisi
- 📋 **Panoya Kopyalama**: Tek tıkla hash değerini kopyalayın
- 🎨 **Modern Arayüz**: Kullanıcı dostu ve şık tasarım
- 🌍 **Türkçe Karakter Desteği**: UTF-8 encoding ile tam destek
- 💾 **Hafif ve Hızlı**: Sadece Python standart kütüphaneleri kullanır

## 🚀 Kurulum

### Gereksinimler

- Python 3.6 veya üzeri
- Tkinter (Python ile birlikte gelir)

### Adımlar

1. Repoyu klonlayın:
```bash
git clone https://github.com/salihoglueyup/hash-hesaplayici.git
cd hash-hesaplayici
```

2. Uygulamayı çalıştırın:
```bash
python hash_gui.py
```

**Not:** Herhangi bir ek kütüphane kurulumu gerekmez! 🎉

## 📖 Kullanım

1. **Metin Girin**: Ana metin alanına şifrenizi veya hash'lemek istediğiniz metni yazın
2. **Algoritma Seçin**: Üstteki radio butonlardan istediğiniz hash algoritmasını seçin
3. **Sonucu Görün**: Hash değeri otomatik olarak hesaplanır ve gösterilir
4. **Kopyalayın**: "Panoya Kopyala" butonuna tıklayarak hash'i kopyalayın

### Örnek Kullanım

```
Girdi: "Merhaba Dünya"
Algoritma: SHA-256
Çıktı: 6f77205f0d99e8b89c0c87a4e5dfa5e82c3e8e3c6f7f4b85d9e98f7e6d5c4b3a
```

## 🔒 Hash Algoritmaları Hakkında

### Hashing Nedir?

**Hashing**, herhangi bir boyuttaki veriyi alıp matematiksel bir algoritma ile sabit uzunlukta bir çıktıya dönüştüren tek yönlü bir şifreleme yöntemidir.

### Temel Özellikler

- **Deterministik**: Aynı girdi her zaman aynı hash'i üretir
- **Tek Yönlü**: Hash değerinden orijinal veriye geri dönemezsiniz
- **Çığ Etkisi**: Küçük bir değişiklik tamamen farklı hash üretir
- **Sabit Uzunluk**: Girdi boyutu ne olursa olsun hash uzunluğu sabittir

### Desteklenen Algoritmalar

| Algoritma | Bit Uzunluğu | Güvenlik | Kullanım Alanı |
|-----------|--------------|----------|----------------|
| MD5       | 128 bit      | ❌ Düşük | Dosya doğrulama (önerilmez) |
| SHA-1     | 160 bit      | ⚠️ Orta  | Eski sistemler (önerilmez) |
| SHA-256   | 256 bit      | ✅ Yüksek | Şifre hash'leme, blockchain |
| SHA-384   | 384 bit      | ✅ Yüksek | Hassas veriler |
| SHA-512   | 512 bit      | ✅ Çok Yüksek | Maksimum güvenlik |

## 🎯 Kullanım Alanları

- 🔐 **Şifre Saklama**: Veritabanında şifreleri güvenli şekilde saklama
- 📁 **Dosya Doğrulama**: İndirilen dosyaların bütünlüğünü kontrol etme
- ⛓️ **Blockchain**: Kripto para ve blockchain uygulamaları
- ✍️ **Dijital İmza**: Belge ve mesaj doğrulama
- 🔍 **Veri Tekilleştirme**: Aynı verinin tekrarını önleme

## 🛠️ Teknik Detaylar

### Kullanılan Teknolojiler

- **Python 3.6+**: Ana programlama dili
- **Tkinter**: GUI framework
- **hashlib**: Hash algoritmaları kütüphanesi

### Proje Yapısı

```
hash-hesaplayici/
│
├── hash_gui.py          # Ana uygulama dosyası
├── README.md            # Bu dosya
├── LICENSE              # MIT lisansı
└── screenshot.png       # Ekran görüntüsü
```

## 🤝 Katkıda Bulunma

Katkılarınızı bekliyoruz! Katkıda bulunmak için:

1. Bu repoyu fork edin
2. Yeni bir branch oluşturun (`git checkout -b feature/yeniOzellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik eklendi'`)
4. Branch'inizi push edin (`git push origin feature/yeniOzellik`)
5. Pull Request açın

## 📝 Yapılacaklar (TODO)

- [ ] Dosya hash'leme özelliği
- [ ] Hash karşılaştırma modu
- [ ] Toplu hash hesaplama
- [ ] Hash'leri dosyaya kaydetme
- [ ] Karanlık tema desteği
- [ ] Farklı diller için destek

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.

## 👨‍💻 Geliştirici

**[Eyüp Zeki Salihoğlu]** - [GitHub Profiliniz](https://github.com/salihoglueyup)

## 🙏 Teşekkürler

Bu projeyi kullandığınız için teşekkürler! Beğendiyseniz ⭐ vermeyi unutmayın!

## 📞 İletişim

Sorularınız için:
- 📧 Email: eyupzekisalihoglu@gmail.com
- 💼 LinkedIn: [Profiliniz](https://linkedin.com/in/eyupzekisalihoglu/)

---

⭐ **Projeyi beğendiyseniz yıldız vermeyi unutmayın!** ⭐
