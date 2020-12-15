import math
import re
import os
import sys
import time



####################################################################################################################################################################################################################################################################################################
#	1. Příklad (5 bodů) Hledání prvočísel. 
####################################################################################################################################################################################################################################################################################################

# Reseni se skládá z 2 funkce:
# 1) prvocislo_test(n), která umí jenom testovat 1 číslo a vrátí True v případě, že zadané číslo je prvočíslem a Falše když není.

# 2) sekvenci_prvocisel(minv,maxv) která generuje sekvence čísel podle vstupnych max/min hodnot, testuje každé číslo z sekvenci a vypíše do konzole sekvence prvočísel a procento prvočísel v sekvenci


def prvocislo_test(n):
    n = int(n) # vstupní argument musí být integer nabo se převádět k int
    if n < 2: # 0 a 1 nejsou prvočísla, vrátím False
        return False
    elif n == 2: # 2 je prvočíslo vrátím True
        return True

    # Při kontrole prvočísla stačí přepočítat děliče 2 až druhá odmocnina zkoumaného čísla. Takže cyklus začínáme dvojkou a končíme odmocninou vstupního čísla

    i = 2
    limit = int(math.sqrt(n))
    while i <= limit: # pomocí while ověřim zůstatek od dělení od 2 do odmocniny n
        if n % i == 0: # kdyby alespoň jedno zustetek byl 0, n není prvočíslo
            return False
        i += 1  # zvětšuju iterátor (a zároveň dělič)
    return True  # jinak ano


def sekvenci_prvocisel(minv: int, maxv :int):  # minv a maxv použito protože nelze užívat max a min jako jméno prom. je to funkce pythonu. Ukazuju, že ta funkce přijímá jenom celočíselné hodnoty pomocí varname: type

    try: # Používám try, protože int() v případě selhání nevrátí False ale hodí chybu a zároveň nejde podminkovat úspěšnost přiřazení. Jinak try v případě chyby splní except
        minv = int(minv) # převedení k int když je to možné a uživatel bych zedal něco jiného.
        maxv = int(maxv) 
    except:  # V případě, že převést do int není možné, vypsat hlášku
        quit("Chyba: minv nebo maxv nejsou integer")	

    if not maxv > minv: # validace minv a maxv
        quit('Chyba: max musí být vyšší než min')

    result = list()	# založím prázdný list pro výsledek
    
    for a in range(minv,maxv+1): # ygeneruju sekvenci čísel od minv do maxv+1. +1 protože for nebere poslední element.
        if prvocislo_test(a): # když v tom kole cyklu a je prvočíslo, dám jeho do vektoru výsledků pomocí append
            result.append(a)	
		
    total_count = maxv - minv + 1 # počítám kolik mám čísel k testování
    true_count = len(result) # podle délky listu (funkce len() vrátí délku) výsledků (pozitivních) zjistím počet prvočísel v sekvenci

    print('Sekvence prvočísel: ' + str(result)) # výpisu Sekvence prvočísel. Konkatenace je možná jenom pro řetězce, tak konvertuju list do řetězce pomocí str()
    print('Procento prvočísel: ', str(round(true_count/total_count*100,2))+'%') # spočítám a výpisu procento prvočísel. To číslo může být dost dlouhým, tak to zkrátím do 2 číslic po čárce pomocí round. Tak to vypadá pěkně

# Testování
#sekvenci_prvocisel(0,12)
#sekvenci_prvocisel(2.1,25)
#sekvenci_prvocisel('2',10)
#sekvenci_prvocisel('two',10)


####################################################################################################################################################################################################################################################################################################
#	2. Příklad 
####################################################################################################################################################################################################################################################################################################


# Reseni se skládá z 2 funkce:
# 1) validate(string, num) připravuje hodnoty. Kontroluje NA, když je číselná, očistí od textů, symbolů a mezer, ořízne mezery na začátku a konci
# 2) fotbaliste(text) rozdělí řetězec podle oddělovače na jednotlivá fotbalisté, pak rozdělí na jednotlivé vlastnosti. Vlastnosti připraví pomocí první funkce a vypíše do zadaného formátu



def validate(string, num=False):  # přijímá řetězec a bool hodnotu číselné/textove. Když druhý argument nezadávat, bude False
	if num: # když hodnota je číselná
		preres = re.findall("\d+", string) # oddělím regulárním výrazem jenom číslice
		
		if len(preres) == 0:  # estli číslice nejsou to znamená že je NA nebo nějaký text nebo vůbec nic
			return 'neznámé'  # v tom případě vrátím řetězec neznámé, který dál se použije abych nadřadit chybějící hdnoty
		else:
			return str(preres[0]) # pokud nějaké číslice tam jsou, převádím to do stringu (pro vhodnost konkatenace dál) a vrátím to
	if string.strip() == 'NA': # pokud není číselná, odstraním mezery a ověřím na NA
		return 'neznámé' # v tom případě vrátím řetězec neznámé, který dál se použije abych nadřadit chybějící hodnoty
	else:
		return string.strip() # jinak vrátím ten řetězec bez mezer na začátku a na konci

def fotbaliste(text):
	rows = text.split(';') # rozdělím text na jednotlivé fotbalisté podle oddelvace ; pomocí metody split()
	for i in range(0,len(rows)): # cyklusem projdu fotbalisté
		hrac = rows[i].split(',') # rozdělím text na jednotlivé vlastnosti podle oddelvace , pomocí metody split()
		print("|{:-^38}|".format("Karta hráče ")) 
		print("|{:38}|".format("Jméno: "+validate(hrac[0].strip().split(' ')[0])))
		print("|{:38}|".format("Příjmení: "+validate(hrac[0].strip().split(' ')[1])))
		print("|{:38}|".format("Let: "+validate(hrac[1], True)))
		print("|Score:{:.>32}|".format(validate(hrac[2], True)+" bodů"))
		print("|Výhry: {: ^31}|".format(validate(hrac[3], True)))
		print("|Remíza:{: ^31}|".format(validate(hrac[4], True)))
		print("|Prohry:{: ^31}|".format(validate(hrac[5], True)))
		print("|{:-^38}|".format("<Hráč č. "+str(i+1)+">")+"\n\n")
		
# formát používám pro formátování řádků, kde výrazem :-^38} nastavím pozice řetězce a zaplnění mezer. 38 je délka řádku | je prostě symbol. Tím "říkám" ulož mi hodnotu proměně uprostřed řádku, který mezi | a | bude mít 38 znaky, a zbytek doplň znakem -

#fotbaliste("Karel Novak, 39 let, 1500, V:2,R:0,P:1; Jana Malá, 40 let, 2100, V:3, R:1,P:0; Pavel Mlady, 20 let, NA, V:1, R:NA, P:0")	
#fotbaliste("Igor Novy, 22 let, 999, V:2,R:1,P:2")			
#fotbaliste("NA NA, NA let, NA, V:NA,R:NA,P:NA")



####################################################################################################################################################################################################################################################################################################
#	3. Příklad 
####################################################################################################################################################################################################################################################################################################

# Reseni se skládá z 3 funkce:
# 1) validate(string, num) připravuje hodnoty. Kontroluje NA, když je číselná, očistí od textů, symbolů a mezer, ořízne mezery na začátku a konci
# 2) fotbaliste(text) rozdělí řetězec podle oddělovače na jednotlivá fotbalisté, pak rozdělí na jednotlivé vlastnosti. Vlastnosti připraví pomocí první funkce a vypíše do zadaného formátu

def visitfile(filepath, name):
    stats = os.stat(filepath)
    try:
        index = name.index('.')
        print("|{: >19}|".format(name[:index][0:18])+"{: >16}".format(name[index:])+" |{: >18}|".format(round(stats.st_size / 1048576, 3))+"{: >26} |".format(time.ctime(stats.st_mtime)))
    except:
        print("|{: >19}|".format(name[0:18])+"{: >16}".format('')+" |{: >18}|".format(round(stats.st_size / 1048576, 3))+"{: >26} |".format(time.ctime(stats.st_mtime)))


def walktree(mypath):
	listd = os.walk(mypath)
	
	for root, dirs, files in listd:
		basefolder = root.index(os.path.basename(mypath))
		basefolder = root[basefolder:]
		folderpath = basefolder.replace('/', ' / ') if root != mypath else os.path.basename(root)
		print("| {:.<83}| ".format(folderpath[0:65]+':'))
		

		if len(files) > 0:
			#print(f[2])
			files.sort()
			for file in files:
				pathname = os.path.join(root, file)
				visitfile(pathname, file)

		


def get_me_info_about(mypath = "C:\\Users\\karel\\Documents"):

	print("|{:-^84}|".format(" get_me_info_about "))
	print("|{:-^84}|".format("Analyzovaná adresa:"))
	print("|{:-^84}|".format(mypath))
	print("|{:-^84}|".format(""))
	print("|{: ^19}|".format("Soubor")+"{: ^16}".format("Sufix")+"|{: ^19}|".format("Velikost v MB")+"{: ^27}|".format("Naposledy změněno"))
	#print("|{:.<84}|".format(os.path.basename(mypath)))
		
	
	walktree(mypath)	
	
	print("|{:-^84}|".format(""))
	print("|{:-^84}|".format(" <"+time.ctime(time.time())+"> "))
	




get_me_info_about('/home/pinguin/Documents/Unicorn2020/Python-Unicorn')




####################################################################################################################################################################################################################################################################################################
#	4. Příklad 
####################################################################################################################################################################################################################################################################################################


# okres Pardubický kraj 


import requests
from lxml import html
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
#from ggplot import *


def parse(url):
	
	#page_response = requests.get('http://localhost/volbycz.html', timeout=5)

	page_response = requests.get(url)
	page_content = BeautifulSoup(page_response.text, 'lxml')
	if page_response.status_code == 200:
		page_content = BeautifulSoup(page_response.text, 'lxml')
		return page_content
	else:
		print('Error. Page returned  '+str(page_response.status_code)+' status')	
		return False


def parseOkres(url, baseUrl):
	okresPage = parse(url)
	if not okresPage:
		print('neni pristupna stranka '+odkaz)
		return False
	res = dict()	
	
	bodyTables = okresPage.find("div", id="inner").find_all('div', {'class': 't3'})  #find('table', {'class': 'table'}).find_all('tr')
	
	for bodyTableDiv in bodyTables:
		bodyTable = bodyTableDiv.find('table', {'class': 'table'}).find_all('tr')
		
		for row in bodyTable:
			if row.td:
				rowtds = row.find_all('td')
				if rowtds[0].a:
					res[urljoin(baseUrl, rowtds[0].find('a').get('href'))] = {'id': rowtds[0].find('a').text, 'name': rowtds[1].text}		
	return res	

		

def parseObec(url,jObec='NULL', jOkres='NULL', kraj='NULL', cObec='NULL'):
	obecPage = parse(url)
	if not obecPage:
		print('neni pristupna stranka '+odkaz)
		return False

	headTable = obecPage.find("table", id="ps311_t1").find_all('tr')

	pv = ''.join(headTable[2].find_all('td')[3].text.split()) # Počet voličů
	poh = ''.join(headTable[2].find_all('td')[6].text.split()) # Počet odevzdaných hlasů				
	pph = ''.join(headTable[2].find_all('td')[7].text.split()) # Počet platných hlasů
	pvo = ''.join(headTable[2].find_all('td')[0].text.split())# Počet volebních okrsků

	result = [jObec, jOkres, kraj, pv, poh, pph, pvo, cObec]
	

	bodyTables = obecPage.find("div", id="inner").find_all('div', {'class': 't2_470'})
	
	for bodyTableDiv in bodyTables:
		bodyTable = bodyTableDiv.find('table', {'class': 'table'}).find_all('tr')
		
	
		for row in bodyTable:
			if row.td:
				rowtds = row.find_all('td')
				result.append(''.join(rowtds[2].text.split()))

	if len(result) != 32:
			print('Chyba!!! Obec '+ jObec + ' vratil spatne cislo vysledku')		
			print(result)
			print(len(result))
			return False
	else:
		return result			

def create_dataframe(strany):

	columns=['Jméno obce', 'Okres', 'Kraj', 'Počet voličů', 'Počet odevzdaných hlasů', 'Počet platných hlasů', 'Počet volebních okrsků', 'Číslo obce', 'Občanská demokratická strana', 'Řád národa - Vlastenecká unie', 'CESTA ODPOVĚDNÉ SPOLEČNOSTI', 'Česká str.sociálně demokrat.', 'Radostné Česko', 'STAROSTOVÉ A NEZÁVISLÍ', 'Komunistická str.Čech a Moravy', 'Strana zelených', 'ROZUMNÍ-stop migraci,diktát.EU', 'Strana svobodných občanů', 'Blok proti islam.-Obran.domova', 'Občanská demokratická aliance', 'Česká pirátská strana', 'Referendum o Evropské unii', 'TOP 09', 'ANO 2011', 'Dobrá volba 2016', 'SPR-Republ.str.Čsl. M.Sládka', 'Křesť.demokr.unie-Čs.str.lid.', 'REALISTÉ', 'SPORTOVCI', 'Dělnic.str.sociální spravedl.', 'Svob.a př.dem.-T.Okamura (SPD)', 'Strana Práv Občanů']

	df = pd.DataFrame(strany, columns = columns)
	print(df)
	df.to_csv('dataframe.csv', encoding='utf-8', index=False)	
	return df				

def parse_volby():

	baseUrl = 'https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ'
	kraj = 'Pardubický kraj'
	homepage = parse(baseUrl)
	if not homepage:
		quit('Příklad 4, Doslo k chybe parsovani homepage')

	
	tables = homepage.body.find("div", id="content").find("div", id="publikace").select("table.table")

	tablePardubicky = None

	for table in tables:
		if 'část '+kraj in table.caption.text:
			tablePardubicky = table
			break

	if not tablePardubicky:
		exit('Neni informace o '+kraj)	

	
	matice = np.array([])
	
	
	for row in tablePardubicky.select('tr'):
		cells = row.find_all('td')
		if cells:
			
			odkaz = urljoin(baseUrl, cells[3].a.get("href"))
			jOkres = cells[1].text

			okresy = parseOkres(odkaz, baseUrl)
			for url, data in okresy.items():
				jObec = data['name']
				cObec = data['id'].strip()
				
				resultRow = parseObec(url, jObec, jOkres, kraj, cObec)
				if resultRow:
					
					try:
						matice = np.vstack((matice, np.array(resultRow)))
					except:
						matice = np.hstack((matice, np.array(resultRow)))
					
					
	dataFR = create_dataframe(matice)
	return True	



def make_graphs(dataframe):
	
	strany = dataframe[dataframe.columns[8:32]].sum()
	strany = pd.to_numeric(strany)
	sortedStrany = strany.sort_values(ascending=False)
	top10 = sortedStrany[0:10]
	
	top10.plot.bar() #Sloupcový graf, který bude zobrazovat agregované údaje za celý kraj – počet získaných hlasů dle 10 nejúspěšnějších stran v kraji

	oskresyHlasy = dataframe[[dataframe.columns[1],dataframe.columns[4]]]
	oskresyHlasyGR = oskresyHlasy.groupby(dataframe.columns[1])
	kolecko_names = list()
	kolecko_values = list()
	for okres in oskresyHlasyGR.groups:
		kolecko_names.append(okres)
		kolecko_values.append(oskresyHlasyGR.get_group(okres).sum()[1])
		
	if len(kolecko_names) == len(kolecko_values):
		fig1, ax1 = plt.subplots()

		wedges, texts, autotexts = ax1.pie(kolecko_values, labels=kolecko_names, autopct='%1.2f%%')
		ax1.axis('equal')
		ax1.legend(loc='upper left', bbox_to_anchor=(-0.10, 0.5)) #Koláčový graf, který bude zobrazovat počet odevzdaných hlasů v jednotlivých okresech!

	
	pvPop = dataframe[[dataframe.columns[3],dataframe.columns[4]]]
	#ggplot(pvPop, aes(x='Počet voličů', y='Počet odevzdaných hlasů')) + geom_point()
	
	plt.show()
	



def analyze_obec(jObec, dataframe):
	
	#print(dataframe.columns)
	obec = dataframe[dataframe[dataframe.columns[0]] == str(jObec)]
	iObce  = obec.index
	kraj = dataframe.loc[iObce]['Kraj'][0]
	okres = dataframe.loc[iObce]['Okres'][0]
	krajeRows = dataframe[dataframe[dataframe.columns[2]] == kraj]
	okseryRows = dataframe[dataframe[dataframe.columns[1]] == okres]
	pvObec = obec[dataframe.columns[3]][0]
	pvOkres = okseryRows[dataframe.columns[3]].values.sum()
	pvKraj = krajeRows[dataframe.columns[3]].values.sum()
	prcPvObec = round(pvObec/pvKraj*100, 2)
	prcPvObec2 = round(pvObec/pvOkres*100, 2)

	pphObec = obec[dataframe.columns[5]][0]
	pphOkres = okseryRows[dataframe.columns[5]].values.sum()
	pphKraj = krajeRows[dataframe.columns[5]].values.sum()
	prcPphObec = round(pphObec/pphKraj*100, 2)
	prcPphObec2 = round(pphObec/pphOkres*100, 2)

	strany = obec[dataframe.columns[8:32]]
	strany = strany.astype(int)
	vyhrala = strany[strany.columns[np.argmax(strany)]].name
	dostala = strany[strany.columns[np.argmax(strany)]][0]

	print("Vysledky analyzy volby v obci "+str(jObec))

	print("Počet voličů v obci: "+str(pvObec))
	print("% od poctu okresu: " + str(prcPvObec2) + "%")
	print("% od poctu kraje: " + str(prcPvObec) + "%")
	print("Počet platných hlasů: "+str(pphObec))
	print("% od poctu okresu: " + str(prcPphObec2) + "%")
	print("% od poctu kraje: " + str(prcPphObec) + "%")

	print("V obci "+str(jObec)+" strana "+ str(vyhrala) + " a dostala "+ str(dostala)+" hlasu")


	

def testovani(filepath):
	dataFR = pd.read_csv(filepath, delimiter=',')
	analyze_obec('Běstvina' ,dataFR)
	make_graphs(dataFR)



#parse_volby()
#testovani('dataframe.csv')



