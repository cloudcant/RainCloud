import itertools
from os import system, name
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
print("""\n\033[36m                                                                                                                                                 
                      ▒▒▒▒▒▒▒▒▒▒                
                    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒              
                  ▒▒▒▒          ▒▒▓▓            
                ▒▒▒▒              ▓▓██          
                ▒▒▒▒              ████          
                ▒▒▒▒                ▒▒▒▒▒▒▒▒    
            ████▒▒▒▒                ▒▒▒▒▒▒▒▒▒▒  
          ▓▓▓▓██▒▒                          ▒▒▒▒
          ▒▒▓▓                              ▒▒▒▒
          ▒▒▒▒                              ▒▒▒▒
          ▒▒▒▒▒▒▒▒    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  
            ▒▒▒▒▒▒    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒   

             ╔════════════════════════════╗
             ║RainCloud WordList Genorater║
             ╚════════════════════════════╝
   ╔═══════════════════════════════════════════════╗
   ║    [!] provide a word size scale [eg: 1:8]    ║
   ╚═══════════════════════════════════════════════╝
""")
                                                    
													
scale = input('\033[36m -> ')
start = int(scale.split(':')[0])
final = int(scale.split(':')[1])
clear()
use_nouse = str(input("""\n\033[36m
╔═══════════════════════════════════════════════╗
║[?] Do you want to enter personal data ? [y/N] ║
╚═══════════════════════════════════════════════╝
->
"""))
if use_nouse == 'y':
	clear()
	first_name = str(input("""\n\033[36m
	╔═══════════════╗
	║[*] Fist Name> ║
	╚═══════════════╝
	->
	"""))
	clear()
	last_name = str(input("""\n\033[36m
	╔═══════════════╗
	║[*] Last Name> ║
	╚═══════════════╝
	->
	"""))
	clear()
	birthday = str(input("""\n\033[36m
	╔═════════════════════════╗
	║[*] Day Of Birth (1-30)> ║
	╚═════════════════════════╝
	->
	"""))
	clear()
	month = str(input("""\n\033[36m
	╔═════════════════╗
	║[*] Birth Month> ║
	╚═════════════════╝
	->
	"""))
	clear()
	year = str(input("""\n\033[36m
	╔═══════════════╗
	║[*] Birth Year>║
	╚═══════════════╝
	->
	"""))
	clear()
	chrs = first_name + last_name + birthday + month + year
else:
	chrs = 'abcdefghijklmnopqrstuvwxyz'
	pass

chrs_up = chrs.upper()
chrs_specials = '!\][/?.,~-=";:><@#$%&*()_+\' '
chrs_numerics = '1234567890'
clear()
file_name = input("""\n\033[36m
╔═════════════════════════════════╗
║[?] Name For Wordlist test file? ║
╚═════════════════════════════════╝
->
""")
arq = open(file_name, 'w')
clear()
if input("""\n\033[36m
╔═══════════════════════════════════════════════════╗
║[?] Do you want to use uppercase characters? (y/n) ║
╚═══════════════════════════════════════════════════╝
->
""") == 'y':
	chrs = ''.join([chrs, chrs_up])
	clear()
if input("""\n\033[36m
╔═════════════════════════════════════════════════╗
║[?] Do you want to use special characters? (y/n) ║
╚═════════════════════════════════════════════════╝
->
""") == 'y':
	chrs = ''.join([chrs, chrs_specials])
	clear()
if input("""\n\033[36m
╔══════════════════════════════════════╗
║[?] Do you want to use Numbers? (y/n) ║
╚══════════════════════════════════════╝
->
""") == 'y':
	chrs = ''.join([chrs, chrs_numerics])
	clear()
for i in range(start, final+1):
	for j in itertools.product(chrs, repeat=i):
		temp = ''.join(j)
		print(temp)
		arq.write(temp + '\n')
arq.close()
