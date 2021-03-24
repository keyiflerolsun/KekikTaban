# <img src="https://www.akashtrehan.com/assets/images/emoji/terminal.png" height="48" align="center"> KekikTaban

![Repo Boyutu](https://img.shields.io/github/repo-size/keyiflerolsun/KekikTaban) ![Views](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https://github.com/keyiflerolsun/KekikTaban&title=Profile%20Views) [![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/keyiflerolsun/KekikTaban)

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/KekikTaban)
![PyPI - Status](https://img.shields.io/pypi/status/KekikTaban)
![PyPI](https://img.shields.io/pypi/v/KekikTaban)
![PyPI - Downloads](https://img.shields.io/pypi/dm/KekikTaban)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/KekikTaban)
![PyPI - License](https://img.shields.io/pypi/l/KekikTaban)

**[@KekikAkademi](https://github.com/KekikAkademi)** *adına yazılmış Projelerin Terminal Tabanı ve Biraz Dahası*

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://GitHub.com/keyiflerolsun/)

## 🚀 Kurulum

```bash
# Yüklemek
pip install KekikTaban

# Güncellemek
pip install -U KekikTaban
```

## 📝 Proje İlerlemesi

- [x] `v0.0.1` *ile* **vira..**

### <img src="https://i.imgur.com/ETZ1ABF.png" height="48" align="center"> Kullanım

```python
from KekikTaban import KekikTaban

taban = KekikTaban(
    baslik   = "@KekikAkademi Userbot",
    aciklama = "kekikUserbot Başlatıldı..",
    banner   = "kekikUserbot",
    girinti  = 1
)

taban.log_salla('a', 'b', 'c')
taban.log_salla('sol', 'orta', 'sag')
taban.log_salla('@keyiflerolsun', '.nekover py', 'Kekik | Kahve')


test = "abcdefghijklmnopqrstuvwxyz"

konsol = taban.konsol
konsol.print(f"{len(test)}", justify="center", style="blink bold red underline on white")

from rich.style import Style
tehlike = Style(color="red", blink=True, bold=True)
konsol.print(f"{len(test)}", justify="center", style=tehlike)

taban.log_salla(test, test, test)

try:
    bakalim()
except Exception as hata:
    taban.hata_salla(hata)
```

## 💸 Bağış Yap

**[☕️ Kahve Ismarla](https://KekikAkademi.org/Kahve)**

## 🌐 Telif Hakkı ve Lisans

* *Copyright (C) 2021 by* [keyiflerolsun](https://github.com/keyiflerolsun) ❤️️
* [GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007](https://github.com/keyiflerolsun/keyifUserBot/blob/master/LICENSE) *Koşullarına göre lisanslanmıştır..*

## ♻️ İletişim

*Benimle iletişime geçmek isterseniz, **Telegram**'dan mesaj göndermekten çekinmeyin;* [@keyiflerolsun](https://t.me/keyiflerolsun)

##

> **[@KekikAkademi](https://t.me/KekikAkademi)** *için yazılmıştır..*
