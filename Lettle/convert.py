import time
WORDLIST_FILENAME = "words.txt"
delimiter="\n" #REPLACE "\N" WITH YOUR DELIMITER OR SEPARATOR
def Convert(string):
    ls=list(string.split(delimiter)) #delimiter
    return ls
with open("wordlist.py", "w+") as external_file:
    rawfile = open("words.txt", "r")
    z=rawfile.read()
    print("Loading words...")
    time.sleep(1)
    print("words = ",Convert(z),file=external_file)
    print(len(Convert(z)),"words successfully loaded into converted.txt!\nYou may close this window.")
    input()
    


