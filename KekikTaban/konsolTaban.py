# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyfiglet import Figlet
import os, platform, requests, datetime, pytz
from rich.console import Console

class KekikTaban(object):

    konsol = Console(log_path=False, highlight=False)

    try:
        kullanici_adi = os.getlogin()
    except OSError:
        import pwd
        kullanici_adi = pwd.getpwuid(os.geteuid())[0]

    bilgisayar_adi = platform.node()
    oturum = kullanici_adi + "@" + bilgisayar_adi                   # Örn.: "kekik@Administrator"

    isletim_sistemi = platform.system()
    bellenim_surumu = platform.release()
    cihaz = isletim_sistemi + " | " + bellenim_surumu               # Örn.: "Windows | 10"

    tarih = datetime.datetime.now(pytz.timezone("Turkey")).strftime("%d-%m-%Y")
    saat  = datetime.datetime.now(pytz.timezone("Turkey")).strftime("%H:%M")
    zaman = tarih + " | " + saat

    global_ip = requests.get('https://api.ipify.org').text

    ust_bilgi = f"[bright_red]{cihaz}[/]\t\t[bright_yellow]{zaman}[/]\n\n"
    ust_bilgi += f"[turquoise2]{oturum}[/]\n"
    ust_bilgi += f"[yellow2]{global_ip}[/]\n"

    def __init__(self, baslik:str, aciklama:str, banner:str, girinti:int=0, stil:str="stop"):
        self.pencere_basligi = baslik
        self.bildirim_metni  = aciklama
        self.logo = Figlet(font=stil).renderText(f"{' ' * girinti}{banner}")

        self.temizle
        self.bildirim
        self.konsol.print(self.logo,      width=70, style="green")
        self.konsol.print(self.ust_bilgi, width=70, justify="center")

    def logo_yazdir(self, renk:str="turquoise2"):
        self.temizle
        self.konsol.print(self.logo, style=renk)

    def bilgi_yazdir(self):
        self.konsol.print(self.ust_bilgi, justify="center")

    def log_salla(self, sol:str, orta:str, sag:str):
        sol  = f"{sol[:13]}[bright_blue]~[/]"   if len(sol)  > 14 else sol
        orta = f"{orta[:19]}[bright_blue]~[/]"  if len(orta) > 20 else orta
        sag  = f"{sag[:14]}[bright_blue]~[/]"   if len(sag)  > 15 else sag
        bicimlendir = '[bold red]{:14}[/] [green]||[/] [yellow]{:20}[/] {:>2}[green]||[/] [magenta]{:^16}[/]'.format(sol, orta, "", sag)
        self.konsol.log(bicimlendir)

    def hata_salla(self, hata:Exception):
        bicimlendir = f"\t  [bold yellow2]{str(type(hata).__name__)}[/] [bold magenta]||[/] [bold grey74]{str(hata)}[/]"
        self.konsol.print(f"{bicimlendir}", width=70, justify="center")

    @property
    def temizle(self):
        if self.isletim_sistemi == "Windows":
            os.system("cls")
        else:
            os.system("clear")

    @property
    def win_baslik(self):
        if self.isletim_sistemi == "Windows":
            try:
                import ctypes
            except ModuleNotFoundError:
                os.system('pip install ctypes')
                import ctypes

            ctypes.windll.kernel32.SetConsoleTitleW(f"{self.pencere_basligi}")

    @property
    def bildirim(self):
        if platform.machine() == "aarch64":
            return
        elif self.kullanici_adi == "gitpod":
            return
        elif self.bellenim_surumu.split('-')[-1] == 'aws':
            return
        elif self.isletim_sistemi == "Windows" and self.bellenim_surumu >= "10":
            try:
                from win10toast import ToastNotifier
            except ModuleNotFoundError:
                os.system('pip install win10toast')
                from win10toast import ToastNotifier

            self.win_baslik
            bildirim = ToastNotifier()
            bildirim.show_toast(f"{self.pencere_basligi}", f"{self.bildirim_metni}",
                icon_path=None, duration=10, threaded=True
            )
        elif self.isletim_sistemi == "Linux":
            try:
                import notify2
            except ModuleNotFoundError:
                os.system('pip install notify2')
                import notify2
            except Exception as hata:
                print(type(hata).__name__)
                return

            notify2.init(self.pencere_basligi)
            bildirim = notify2.Notification(f"{self.pencere_basligi}", f"{self.bildirim_metni}", "notification-message-im")
            bildirim.show()