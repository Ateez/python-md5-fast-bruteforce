#usr/bin/python
import time
import itertools, string
import hashlib
import sys
import signal
import threading

info = """
  Name            : Python Md5 Brute-force
  Created By      : Sefa Said Deniz
  Blog            : sefasaiddeniz.com
  Documentation   : https://github.com/sefasaid/python-md5-bruteforce/
  License         : Completely Free
  Thanks to       : Agus Makmun (Summon Agus)-bloggersmart.net - python.web.id
  Fixed by        : Ateez
"""

done = False
def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    global done
    done=True
    sys.exit(0)

def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done==True:
            break
        
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.2)
        
    

def _attack(chrs, inputt):
    print("[+] Start Time: ", time.strftime('%H:%M:%S'))
    start_time = time.time()
    t = threading.Thread(target=animate)
    t.start()
    total_pass_try=0
    for n in range(1, 31+1):
      characterstart_time = time.time()
      
      for xs in itertools.product(chrs, repeat=n):
          saved = ''.join(xs)

          stringg = saved
          m = hashlib.md5()
          m.update(bytes(saved, encoding='utf-8'))
          total_pass_try +=1
          if m.hexdigest() == inputt:
              #time.sleep(10) # ¯\_(ツ)_/¯ 
              global done
              done = True

              print("\r\r _ _ _ _ _ _ _ _ _ _\n\n", stringg+'\n _ _ _ _ _ _ _ _ _ _')
              print("\n[-] End Time: ", time.strftime('%H:%M:%S'),"(%s sec)" % round((time.time() - start_time),1))
              print("\n[-] Total Keyword attempted: ", total_pass_try)
              sys.exit("\nThank You !\n")
        
      print("\r[!]",n,"-character finished in %s sec\r" % round((time.time() - characterstart_time),1))

def main():
    print(info)
    
    inp_usr = input("Paste MD5 here:\n")
    chrs = string.printable.replace(' \t\n\r\x0b\x0c', '')

    #comment line below for full (Slow) bruteforce
    chrs='0123456789abcdefghijklmnopqrstuvwxyz' 

    #uncomment line below for Russian letters
    #chrs=chrs+'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' #uncomment for Russian letters

    print('\nCharacter list:\n'+chrs+'\n')
    signal.signal(signal.SIGINT, signal_handler)
    return _attack( chrs,inp_usr.lower())

if __name__ == "__main__":
    main()
   
   
   
