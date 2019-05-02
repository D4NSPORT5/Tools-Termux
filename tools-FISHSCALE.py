import os

print("""
Created by FI$H$CALE
Ver: 1.0
----------------------
TOOLS ONLY FOR TERMUX!
----------------------
""")
lang = input('Eng/Rus? ')

def menu():
	
	if (lang == "Eng") or (lang == "eng"):
		print("""
00. Turn your Android into Hacking Machine.
------------------------------------------
1. Install Nmap 
2. Install Hydra
3. Install SQLMap
4. Install Metasploit
5. Install ngrok
6. Install Kali Nethunter
7. Install angryFuzzer
8. Install Red_Hawk
9. Install Weeman
10. Install IPGeoLocation
11. Install Cupp
12. Instagram Bruteforcer (instahack)
13. Twitter Bruteforcer   (TwitterSniper)
14. Install Ubuntu
15. Install Fedora
16. Install viSQL
17. Install Hash-Buster
18. Install routersploit
------------------------------------------
99. Exit
""")
	elif (lang == "Rus") or (lang == "rus"):
		print("""
00. Сделать ваш Android хакерским.
------------------------------------------
1. Скачать Nmap 
2. Скачать Hydra
3. Скачать SQLMap
4. Скачать Metasploit
5. Скачать ngrok
6. Скачать Kali Nethunter
7. Скачать angryFuzzer
8. Скачать Red_Hawk
9. Скачать Weeman
10. Скачать IPGeoLocation
11. Скачать Cupp
12. Instagram брутофорсер (instahack)
13. Twitter брутофорсер   (TwitterSniper)
14. Скачать Ubuntu
15. Скачать Fedora
16. Скачать viSQL
17. Скачать Hash-Buster
18. Скачать routersploit
------------------------------------------
99. Выйти
""")

def suc(a, b):
	if (lang == "Rus") or (lang == "rus"):		
		print('=======================')
		print(a, 'успешна скачана!')
		print(b)
		print('Выйти из программы? (д/н)')
		print('=======================')
	else:
		print('=======================')
		print(a, 'successfully downloaded!')
		print(b)
		print('Quit the program? (y/n)')
		print('=======================')

loop = True

while loop == True:
	menu()
	kavo = int(input("#: "))
	#1==========================
	if kavo == 1:
		os.system("cd /data/data/com.termux/files/home")
		os.system("pkg update -y")
		os.system("pkg install -y nmap")
		os.system("cd /data/data/com.termux/files/home")
		if (lang == 'rus') or (lang == 'Rus'):
			suc('Nmap', 'Выйди из программы и напиши "cd", потом "Nmap"')
		elif (lang == 'eng') or (lang == 'Eng'):
			suc('Nmap', 'Exit the program and write "cd", after "Nmap"')
	#2===========================
	if kavo == 2:
		os.system("cd /data/data/com.termux/files/home")
		os.system("pkg update -y")
		os.system("pkg install -y hydra")
		os.system("cd /data/data/com.termux/files/home")
		if (lang == 'rus') or (lang == 'Rus'):
			suc('Hydra', 'Выйди из программы и напиши "cd", потом "Hydra"')
		elif (lang == 'eng') or (lang == 'Eng'):
			suc('Hydra', 'Exit the program and write "cd", after "Hydra"')
	#3===========================
	if kavo == 3:
		os.system("cd /data/data/com.termux/files/home")
		os.system("pkg update -y")
		os.system("pkg install -y git")
		os.system("pkg install python2")
		os.system("cd /data/data/com.termux/files/home && git clone https://github.com/sqlmapproject/sqlmap.git")
		os.system("cd /data/data/com.termux/files/home")
		if (lang == 'rus') or (lang == 'Rus'):
			suc('SQLmap', 'Выйдите из программы и напишите "cd", после "python2 sqlmap.py"')
		elif (lang == 'eng') or (lang == 'Eng'):
			suc('SQLmap', 'Exit the program and write "cd", after "python2 sqlmap.py"')
	#4===========================
	if kavo == 4:
		os.system("pkg install -y wget")
		os.system("cd /data/data/com.termux/files/home && wget https://Auxilus.github.io/metasploit.sh")
		os.system("cd /data/data/com.termux/files/home && bash metasploit.sh")
		os.system("cd /data/data/com.termux/files/home && cd metasploit-framework")
		os.system("cd /data/data/com.termux/files/home && gem install bundle --pre")
		os.system("cd /data/data/com.termux/files/home && bundle config build.nokogiri --use-system-libraries")
		os.system("cd /data/data/com.termux/files/home && bundle install")
		os.system("cd /data/data/com.termux/files/home")
		if (lang == 'rus') or (lang == 'Rus'):
			suc('Metasploit', 'Выйдите из программы и напишите "cd", после "msfconsole"')
		elif (lang == 'eng') or (lang == 'Eng'):
			suc('Metasploit', 'Exit the program and write "cd", after "msfconsole"')
	#5===========================
	if kavo == 5:
		os.system("pkg update -y")
		os.system("pkg install -y git")
		os.system("cd /data/data/com.termux/files/home && git clone https://github.com/themastersunil/ngrok.git")
		os.system("cd /data/data/com.termux/files/home")
		if (lang == 'rus') or (lang == 'Rus'):
			suc('Ngrok', 'Выйдите из программы и напишите "cd", после "./ngrok http 80"')
		elif (lang == 'eng') or (lang == 'Eng'):
			suc('Ngrok', 'Exit the program and write "cd", after "./ngrok http 80"')	
	#6===========================
	if kavo == 6:
		os.system("pkg update -y")
		os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Hax4us/Nethunter-In-Termux.git")
		os.system("cd /data/data/com.termux/files/home && cd Nethunter-In-Termux && chmod +x kalinethunter")
		os.system("cd /data/data/com.termux/files/home")
		if (lang == 'rus') or (lang == 'Rus'):
			suc('Nethunter', 'Выйдите из программы и напишите "cd", после "сd Nethunter-In-Termux", после этого "./kalinethunter"')
		elif (lang == 'eng') or (lang == 'Eng'):
			suc('Nethunter', 'Exit the program and write "cd", after "cd Nethunter-In-Termux", after that "./kalinethunter"')
	#7===========================
	if kavo == 7:
		os.system("pkg update -y")
		os.system("pkg install -y git")
		os.system("pkg install -y python2")
		os.system("cd /data/data/com.termux/files/home && git clone https://github.com/ihebski/angryFuzzer.git")
		os.system("cd /data/data/com.termux/files/home && cd angryFuzzer")
		os.system("cd /data/data/com.termux/files/home && pip2 install -r requirements.txt")
		os.system("cd /data/data/com.termux/files/home && pip2 install requests")
		os.system("cd /data/data/com.termux/files/home")
		if (lang == 'rus') or (lang == 'Rus'):
			suc('angryFuzzer', 'Выйдите из программы и напишите "cd", после "сd angryFuzzer", после этого "python2 angryFuzzer.py"')
		elif (lang == 'eng') or (lang == 'Eng'):
			suc('angryFuzzer', 'Exit the program and write "cd", after "cd angryFuzzer", after that "python2 angryFuzzer.py"')
	#8===========================
	if kavo == 8:
		os.system("pkg update -y")
		os.system("pkg install -y git")
		os.system("pkg install -y php")
		os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Tuhinshubhra/RED_HAWK")
		os.system("cd /data/data/com.termux/files/home")
		if (lang == 'rus') or (lang == 'Rus'):
			suc('RED_HAWK', 'Выйдите из программы и напишите "cd", после "сd RED_HAWK", после этого "php rhawk.php"')
		elif (lang == 'eng') or (lang == 'Eng'):
			suc('RED_HAWK', 'Exit the program and write "cd", after "cd RED_HAWK", after that "php rhawk.php"')
	#9===========================
	if kavo == 9:
		os.system("pkg update -y")
		os.system("pkg install -y python2")
		os.system("pkg install -y git")
		os.system("cd /data/data/com.termux/files/home && git clone https://github.com/evait-security/weeman.git")
		os.system("cd /data/data/com.termux/files/home && cd weeman")
		os.system("cd /data/data/com.termux/files/home && chmod +x weeman.py")
		os.system("cd /data/data/com.termux/files/home")
		if (lang == 'rus') or (lang == 'Rus'):
			suc('weeman', 'Выйдите из программы и напишите "cd", после "сd weeman", после этого "python2 weeman.py"')
		elif (lang == 'eng') or (lang == 'Eng'):
			suc('weeman', 'Exit the program and write "cd", after "cd weeman", after that "python2 weeman.py"')
	#10===========================
	if kavo == 10:
		os.system("pkg update -y")
		os.system("pkg install -y git")
		os.system("pkg install -y python")
		os.system("cd /data/data/com.termux/files/home && git clone https://github.com/maldevel/IPGeoLocation.git")
		os.system("cd /data/data/com.termux/files/home && cd IPGeoLocation")
		os.system("cd /data/data/com.termux/files/home && pip install -r requirements.txt")
		os.system("cd /data/data/com.termux/files/home")
		if (lang == 'rus') or (lang == 'Rus'):
			suc('IPGeoLocation', 'Выйдите из программы и напишите "cd", после "сd IPGeoLocation", после этого "python ipgeolocation.py"')
		elif (lang == 'eng') or (lang == 'Eng'):
			suc('IPGeoLocation', 'Exit the program and write "cd", after "cd IPGeoLocation", after that "python ipgeolocation.py"')
	#11===========================
	if kavo == 11:
		os.system("pkg update -y")
		os.system("pkg install -y git")
		os.system("pkg install -y python")
		os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Mebus/cupp.git")
		if (lang == 'rus') or (lang == 'Rus'):
			suc('Cupp', 'Выйдите из программы и напишите "cd", после "сd Cupp", после этого "python cupp3.py"')
		elif (lang == 'eng') or (lang == 'Eng'):
			suc('Cupp', 'Exit the program and write "cd", after "cd Cupp", after that "python cupp3.py"')
	#12===========================
	if kavo == 12:
		os.system("pkg update -y")
		os.system("pkg install -y git")
		os.system("pkg install -y python")
		os.system("pkg install -y nano")
		os.system("pip install requests")
		os.system("pip install beautifulsoup4")
		os.system("cd /data/data/com.termux/files/home && git clone https://github.com/avramit/instahack.git")
		if (lang == 'rus') or (lang == 'Rus'):
			suc('Instahack', 'Выйдите из программы и напишите "cd", после "сd Instahack", после этого "python hackinsta.py"')
		elif (lang == 'eng') or (lang == 'Eng'):
			suc('Instahack', 'Exit the program and write "cd", after "cd Instahack", after that "python hackinsta.py"')
	#13===========================
	if kavo == 13:
		os.system("pkg update -y")
		os.system("pkg install -y git")
		os.system("pkg install -y python")
		os.system("pip install mechanicalsoup")
		os.system("pkg install -y nano")
		os.system("cd /data/data/com.termux/files/home && git clone https://github.com/abdallahelsokary/TwitterSniper.git")
		if (lang == 'rus') or (lang == 'Rus'):
			suc('TwitterSniper', 'Выйдите из программы и напишите "cd", после "сd TwitterSniper", после этого "python TwitterSniper.py"')
		elif (lang == 'eng') or (lang == 'Eng'):
			suc('TwitterSniper', 'Exit the program and write "cd", after "cd TwitterSniper", after that "python TwitterSniper.py"')
	#14===========================
	if kavo == 14:
		os.system("pkg update -y")
		os.system("pkg install -y git")
		os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Neo-Oli/termux-ubuntu.git")
		os.system("cd /data/data/com.termux/files/home && cd termux-ubuntu && bash ubuntu.sh")
		if (lang == 'rus') or (lang == 'Rus'):
			suc('Ubuntu', 'Выйдите из программы и напишите "cd", после "сd termux-ubuntu", после этого "./start.sh"')
		elif (lang == 'eng') or (lang == 'Eng'):
			suc('Ubuntu', 'Exit the program and write "cd", after "cd termux-ubuntu", after that "./start.sh"')
	#15===========================
	if kavo == 15:
		os.system("pkg update -y")
		os.system("pkg install -y git")
		os.system("pkg install -y wget")
		os.system("apt update && apt install wget -y && /data/data/com.termux/files/usr/bin/wget https://raw.githubusercontent.com/nmilosev/termux-fedora/master/termux-fedora.sh")
		if (lang == 'rus') or (lang == 'Rus'):
			suc('Fedora', 'Выйдите из программы и напишите "cd", после этого "sh termux-fedora.sh f26_arm64" или "sh termux-fedora.sh f26_arm"')
		elif (lang == 'eng') or (lang == 'Eng'):
			suc('Fedora', 'Exit the program and write "cd", after that "sh termux-fedora.sh f26_arm64" or "sh termux-fedora.sh f26_arm"')
	#16===========================
	if kavo == 16:
		os.system("pkg update -y")
		os.system("pkg install -y git")
		os.system("pkg install -y python2")
		os.system("cd /data/data/com.termux/files/home && git clone https://github.com/blackvkng/viSQL.git")
		if (lang == 'rus') or (lang == 'Rus'):
			suc('viSQL', 'Выйдите из программы и напишите "cd", после "сd viSQL", после этого "python2 viSQL.py --help"')
		elif (lang == 'eng') or (lang == 'Eng'):
			suc('viSQL', 'Exit the program and write "cd", after "cd viSQL", after that "python2 viSQL.py --help"')
	#17===========================
	if kavo == 17:
		os.system("pkg update -y")
		os.system("pkg install -y git")
		os.system("pkg install -y python2")
		os.system("cd /data/data/com.termux/files/home && git clone https://github.com/UltimateHackers/Hash-Buster.git")
		if (lang == 'rus') or (lang == 'Rus'):
			suc('Hash-Buster', 'Выйдите из программы и напишите "cd", после "сd Hash-Buster", после этого "python2 hash.py"')
		elif (lang == 'eng') or (lang == 'Eng'):
			suc('Hash-Buster', 'Exit the program and write "cd", after "cd Hash-Buster", after that "python2 hash.py"')
	#18===========================
	#Здесь должен быть D-TECT
	#19===========================
	if kavo == 18:
		os.system("pkg update -y")
		os.system("pkg install -y git")
		os.system("pkg install -y python2")
		os.system("cd /data/data/com.termux/files/home && git clone https://github.com/reverse-shell/routersploit.git")
		os.system("cd /data/data/com.termux/files/home && cd routersploit")
		os.system("pip2 install -r requirements.txt")
		os.system("pip2 install -r requirements-dev.txt")
		os.system("pip2 install -r requests")
		if (lang == 'rus') or (lang == 'Rus'):
			suc('routersploit', 'Выйдите из программы и напишите "cd", после "сd routersploit", после этого "python2 rsf.py"')
		elif (lang == 'eng') or (lang == 'Eng'):
			suc('routersploit', 'Exit the program and write "cd", after "cd routersploit", after that "python2 rsf.py"')
	#99===========================
	if kavo == 99:
		if (lang == "eng") or (lang == "Eng"):	
			print("Bye! Happy Hacking)")
			loop = False
		elif (lang == "Rus") or (lang == "rus"):
			print("Пока! Счастливого хакинга)")
			loop = False
	if kavo == 99:
		loop = False
	else:
		otv = input("#: ")
		if (otv == "n") or (otv == "н"):	
			menu()
		elif (otv == "y") or (otv == "д"):
			loop = False
