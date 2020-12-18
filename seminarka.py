import math
import re
import os
import sys
import time



####################################################################################################################################################################################################################################################################################################
#	1. Příklad (5 bodů) Hledání prvočísel. 
####################################################################################################################################################################################################################################################################################################

# Řešení se skládá z 2 funkce:
# 1) prvocislo_test(n) umí jenom testovat 1 číslo a vrátí True v případě, že zadané číslo je prvočíslem a False pokud není.

# 2) sekvenci_prvocisel(minv,maxv) generuje sekvence čísel podle vstupných max/min hodnot, testuje každé číslo z sekvenci a vypíše do konzole sekvence prvočísel a procento prvočísel v sekvenci.


def prvocislo_test(n):
    n = int(n) # vstupní argument musí být integer nebo se převádět k int
    if n < 2: # 0 a 1 nejsou prvočísla, vrátím False
        return False
    elif n == 2: # 2 je prvočíslo vrátím True
        return True

    # Při kontrole prvočísla stačí přepočítat děliče 2 až druhá odmocnina zkoumaného čísla. Takže začínáme cyklus dvojkou a končíme odmocninou vstupního čísla.

    i = 2
    limit = int(math.sqrt(n))
    while i <= limit: # pomocí while ověřím zůstatek od dělení 2 až odmocniny n
        if n % i == 0: # kdyby aspoň jeden zůstatek byl 0, n není prvočíslo
            return False
        i += 1  # zvětšení iterátoru (a zároveň děliče)
    return True  # jinak ano


def sekvenci_prvocisel(minv: int, maxv :int):  # minv a maxv je použito protože nelze užívat max a min jako jméno prom. je to funkce pythonu. Ukazují, že tato funkce přijímá jenom celočíselné hodnoty pomocí varname: type

    try: # Používám try, protože int() v případě selhání nevrátí False ale hodí chybu a zároveň nejde podminkovat úspěšnost přiřazení. Jinak try v případě chyby splní except
        minv = int(minv) # převedení k int když je to možné a uživatel bych zadal něco jiného.
        maxv = int(maxv) 
    except:  # V případě, že převést k int není možné, vypsat hlášku
        quit("Chyba: minv nebo maxv nejsou integer")	

    if not maxv > minv: # validace minv a maxv
        quit('Chyba: max musí být vyšší než min')

    result = list()	# založím prázdný list pro výsledek
    
    for a in range(minv,maxv+1): # vygenerují sekvenci čísel od minv do maxv+1. +1 protože for nepoužívá poslední element.
        if prvocislo_test(a): # když v teto iterace cyklu prom. a je prvočíslo, přidám ji do vektoru výsledků pomocí append
            result.append(a)	
		
    total_count = maxv - minv + 1 # počítám kolik mám čísel k testování
    true_count = len(result) # podle délky listu (funkce len() vrátí délku) výsledků (pozitivních) zjistím počet prvočísel v sekvenci

    print('Sekvence prvočísel: ' + str(result)) # výpišu Sekvence prvočísel. Konkatenace je možná jenom pro řetězce, tak konvertuju list do řetězce pomocí str()
    print('Procento prvočísel: ', str(round(true_count/total_count*100,2))+'%') # spočítám a výpišu procento prvočísel. To číslo může být docela dlouhým, tak to zkrátím do 2 číslic po čárce pomocí round. Tak to vypadá hezké.

# Testování
#sekvenci_prvocisel(0,12)
#sekvenci_prvocisel(2.1,25)
#sekvenci_prvocisel('2',10)
#sekvenci_prvocisel('two',10)


####################################################################################################################################################################################################################################################################################################
#	2. Příklad 
####################################################################################################################################################################################################################################################################################################


# Řešení se skládá z 2 funkce:
# 1) validate(string, num) připravuje hodnoty. Kontroluje NA, když jsou číselná, očistí od textů, symbolů a mezer, ořízne mezery na začátku a na konci.
# 2) fotbaliste(text) rozdělí řetězec podle oddělovače na jednotlivá fotbalisté, pak rozdělí na jednotlivé vlastnosti. Vlastnosti připraví pomocí první funkce a vypíše do zadaného formátu.



def validate(string, num=False):  # přijímá řetězec a bool hodnotu (číselné/textove). Když druhý argument nezadávat, bude False
	if num: # pokud hodnota je číselná
		preres = re.findall("\d+", string) # oddělím regulárním výrazem jenom číslice
		
		if len(preres) == 0:  # jestli číslice nejsou, to znamená že je NA nebo nějaký text nebo vůbec nic
			return 'neznámé'  # v tom případě vrátím řetězec "neznámé", který dál se použije aby nadřadit chybějící hodnoty
		else:
			return str(preres[0]) # pokud nějaké číslice tam jsou, převádím to do stringu (pro vhodnost konkatenace dál) a vrátím to
	if string.strip() == 'NA': # pokud není číselná, odstraním mezery a ověřím na NA
		return 'neznámé' # v tom případě vrátím řetězec "neznámé", který dál se použije aby nadřadit chybějící hodnoty
	else:
		return string.strip() # jinak vrátím ten řetězec bez mezer na začátku a na konci

def fotbaliste(text):
	rows = text.split(';') # rozdělím text na jednotlivé fotbalisté podle oddelvače ; pomocí metody split()
	for i in range(0,len(rows)): # cyklusem projdu fotbalisté
		hrac = rows[i].split(',') # rozdělím text na jednotlivé vlastnosti podle oddelvače , pomocí metody split()
		print("|{:-^38}|".format("Karta hráče ")) 
		print("|{:38}|".format("Jméno: "+validate(hrac[0].strip().split(' ')[0])))
		print("|{:38}|".format("Příjmení: "+validate(hrac[0].strip().split(' ')[1])))
		print("|{:38}|".format("Let: "+validate(hrac[1], True)))
		print("|Score:{:.>32}|".format(validate(hrac[2], True)+" bodů"))
		print("|Výhry: {: ^31}|".format(validate(hrac[3], True)))
		print("|Remíza:{: ^31}|".format(validate(hrac[4], True)))
		print("|Prohry:{: ^31}|".format(validate(hrac[5], True)))
		print("|{:-^38}|".format("<Hráč č. "+str(i+1)+">")+"\n\n")
		
# format používám pro formátování řádků, kde výrazem :-^38} nastavím pozice řetězce a zaplnění mezer. 38 je délka řádku | je jenom symbol. Tím "říkám" umisti hodnotu proměně uprostřed řádku, který mezi | a | bude mít 38 znaky, a zbytek doplň znakem -


# Testování
#fotbaliste("Karel Novak, 39 let, 1500, V:2,R:0,P:1; Jana Malá, 40 let, 2100, V:3, R:1,P:0; Pavel Mlady, 20 let, NA, V:1, R:NA, P:0")	
#fotbaliste("Igor Novy, 22 let, 999, V:2,R:1,P:2")			
#fotbaliste("NA NA, NA let, NA, V:NA,R:NA,P:NA")



####################################################################################################################################################################################################################################################################################################
#	3. Příklad 
####################################################################################################################################################################################################################################################################################################

# Řešení se skládá z 3 funkce:
# 1) visitfile(filepath, name) zkoumá soubor. Získává jeho jméno, sufix, velikost a poslední změnu. Printi řádek souboru.
# 2) walktree(mypath) rekursivně prochází adresář, vypisuje podadresáře, získává soubory v jednotlivém adresáři a volá visitfile pro každý soubor. Je wraperem funkce os.walk
# 3) get_me_info_about(mypath) přijímá cestu, printi hlavičku a patičku výstupné tabulky, v správním místě volá walktree()

def visitfile(filepath, name): 
    stats = os.stat(filepath) # získávám údaje souboru pomocí os.state
    try:   # některé soubory (minimálně v Unix systémech nemají sufix (extension). Pro takové subory metoda index('.') hodí chybu. Proto užívám try/except )
        index = name.index('.') # dělím název souboru na jméno a sufix
        print("|{: >19}|".format(name[:index][0:18])+"{: >16}".format(name[index:])+" |{: >18}|".format(round(stats.st_size / 1048576, 3))+"{: >26} |".format(time.ctime(stats.st_mtime))) # printim údaje suoboru z použitím metody format() jako v minulém příkladě. V proměně stat mám uložené různé údaje souboru. Zajímá mí velikost stats.st_size a poslední úprava. Velikost mám v bytes, pro MB dělím 1048576 a skratim do 3 deset. míst pomocí round. Pro formátování času z timestamp do našeho formátu používám ctime z balíčku time
    except:
        print("|{: >19}|".format(name[0:18])+"{: >16}".format('')+" |{: >18}|".format(round(stats.st_size / 1048576, 3))+"{: >26} |".format(time.ctime(stats.st_mtime)))


def walktree(mypath): # přijímá mypath - cesta od / do zkoumané složky
	listd = os.walk(mypath) # rekursivně prochází adresář a ukládá do listd objekt "generator object walk"

	for root, dirs, files in listd: # listd se dá projít for cyklusem. Pro pohodlí používám 3 proměnný (protože jednotlivý objekt z listd má 3 objektů. 1 string a 2 listu) root je cesta od /, do složky v mypath (mypathfolder/slozka1/podslozka2). dirs má v sobě seznam název složek v složce root. files má v sobě názvy souborů v složce root
		basefolder = root.index(os.path.basename(mypath)) 
		basefolder = root[basefolder:]
		#  do basefolder ukládám cestu k aktuálně podsložce od složky mypath (Dokumenty / moje_slozka /slozka_v_slozce). Pro to získávám název zkoumané složky bez cesty pomocí basename. Pak pomocí index rozdělím cestu od /, do mypath a od mypath do aktuálně podslozky. Používám druhou
		folderpath = basefolder.replace('/', ' / ') # přidávám mezery mezi adresáři
		print("| {:.<83}| ".format(folderpath[0:65]+':')) # Printim cestu aktuálně složky
		if len(files) > 0: # ověřuji obsahuje-li aktualna složka v sobě soubory nebo ne
			files.sort() # pokud ano, seřadím jich podle názvu
			for file in files: # cyklusem projdu každý soubor
				pathname = os.path.join(root, file) # pomocí join slepím cestu od / do souboru a název souboru
				visitfile(pathname, file) # zavolám funkce visitfile pro výpis údaje o souboru

		

def get_me_info_about(mypath = os.getcwd()): # přijímá cestu od /, když není zadaná, argumentem bude aktuální složka (zjistím pomocí getcwd())
	# printim hlavičku
	print("|{:-^84}|".format(" get_me_info_about "))
	print("|{:-^84}|".format("Analyzovaná adresa:"))
	print("|{:-^84}|".format(mypath))
	print("|{:-^84}|".format(""))
	print("|{: ^19}|".format("Soubor")+"{: ^16}".format("Sufix")+"|{: ^19}|".format("Velikost v MB")+"{: ^27}|".format("Naposledy změněno"))
		
	# printim tělo	
	walktree(mypath)	
	
	# printim patičku
	print("|{:-^84}|".format(""))
	print("|{:-^84}|".format(" <"+time.ctime()+"> ")) # zjistím aktuální čas pomocí time.ctime()
	



# Testování
#get_me_info_about()
#get_me_info_about("/var/www/html/first-developer.com")
#get_me_info_about("/home/pinguin/Documents/Unicorn2020/Python-Unicorn/test_folder_task3")




####################################################################################################################################################################################################################################################################################################
#	4. Příklad 
####################################################################################################################################################################################################################################################################################################
# Řešení se skládá z 8 funkce:
# 1) parse(url) parsuje webovou stránku z argumentů url.
# 2) parseOkres(url, baseUrl) parsuje odkazy na jednotlivé obcí z stránky kraje.
# 3) parseObec(url,jObec,jOkres,kraj,cObec) parsuje daty o volbách v obci. Vrátí list z hodnoty. Tento list bude dál řádkem dataframu
# 4) create_dataframe(table) vytvoří dataframe z matice (numpy array) a formátuje číselné sloupci
# 5) analyze_obec(jObec, dataframe) provádí analýzu voleb v obci a printi do konzole statistiky obce
# 6) make_graphs(dataframe) kreslí grafy o volbách
# 7) parse_volby() je hlavní funkce zadání. Zpracova výsledky parsovani, vytvoří matice a volá dasli funkce toho zadání


# Pardubický kraj 


import requests
from lxml import html
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from plotnine import ggplot, aes, geom_point


def parse(url): # Přijímá url adresu webu pro parsovani. Vrátí html strukturu webu nebo False

	#page_response = requests.get('http://localhost/volbycz.html', timeout=5)
	page_response = requests.get(url) # pomocí get() z balíčku requests, stáhneme stránku
	if page_response.status_code == 200: # ověřím, že tato stránka se stáhla v pohodě. O tom mi říká kód 200. Pokud ten requests nemá cache, to stačí
		page_content = BeautifulSoup(page_response.text, 'lxml') # pomocí BeautifulSoup() z parserem lxml vytáhnu html web stránky
		return page_content 
	else:
		print('Error. Page returned  '+str(page_response.status_code)+' status') # Jestli stránka vrátila nějaký špatný kód, vypisuju hlášku a vrátím False
		return False


def parseOkres(url, baseUrl): # Přijímá url adresu okresů a hlavní stránky, vrátí slovník z seznamem odkazů na jednotlivé obcí a některé údaje obci
	okresPage = parse(url)  # parsuju stránku okresu
	if not okresPage: # kontrola úspěšnosti parsovani
		print('neni pristupna stranka '+odkaz)
		return False
	res = dict() # nadefinuju slovník pro ukládání výsledků prací funkce
	
	bodyTables = okresPage.find("div", id="inner").find_all('div', {'class': 't3'})  # z html stránky vytáhnu bloky z tabulkama (tři sloupci na webu) find() hlídám první div.inner a v tom div pomocí find_all všichni div které mají class t3
	for bodyTableDiv in bodyTables: # proházím bloky z tabulkama cyklusem
		bodyTable = bodyTableDiv.find('table', {'class': 'table'}).find_all('tr') # vytáhnu všichni řádky tabuky
		
		for row in bodyTable: # proházím cyklusem každý řádek
			if row.td: # kontriluju, ze je to řádek těla, není hlavička (v hlavičce se používá <th> a z nějakého důvodu netřídí se na <thead> a <tbody>)
				rowtds = row.find_all('td') # ukládám řádek do proměně
				if rowtds[0].a: # pokud není prázdný (jako v nějakém okresu poslední řádek)
					res[urljoin(baseUrl, rowtds[0].find('a').get('href'))] = {'id': rowtds[0].find('a').text, 'name': rowtds[1].text} # ukládám do slovníku odkaz (odkaz konkatenuju z adresou webu protože jsou relativní) 
	return res	

		

def parseObec(url,jObec='NULL', jOkres='NULL', kraj='NULL', cObec='NULL'): # Přijímá url adresu obce a údaje, které jsou na stránce okresů. Vrátí list, který bude řádkem ve výsledním dataframu
	obecPage = parse(url) # parsuju stránku obce
	if not obecPage: # kontrola úspěšnosti parsovani
		print('neni pristupna stranka '+odkaz)
		return False

	headTable = obecPage.find("table", id="ps311_t1").find_all('tr') # vytáhnu všichni řádky tabulky z datama o volicech

	# ''.join(obj.text.split()) používám pro odstranani mezer.
	pv = ''.join(headTable[2].find_all('td')[3].text.split()) # Počet voličů 
	poh = ''.join(headTable[2].find_all('td')[6].text.split()) # Počet odevzdaných hlasů				
	pph = ''.join(headTable[2].find_all('td')[7].text.split()) # Počet platných hlasů
	pvo = ''.join(headTable[2].find_all('td')[0].text.split()) # Počet volebních okrsků

	result = [jObec, jOkres, kraj, pv, poh, pph, pvo, cObec] # definuju list výsledků
	
	# dále stejně jako v minulé funkce
	bodyTables = obecPage.find("div", id="inner").find_all('div', {'class': 't2_470'})   
	
	for bodyTableDiv in bodyTables: 
		bodyTable = bodyTableDiv.find('table', {'class': 'table'}).find_all('tr') 
		
	
		for row in bodyTable: 
			if row.td:
				rowtds = row.find_all('td')
				result.append(''.join(rowtds[2].text.split()))

	if len(result) != 32: # ověřím, že počet stran je správný. Jinak pak by to nešlo uložit do matice
			print('Chyba!!! Obec '+ jObec + ' vratil spatne cislo vysledku')		
			print(result)
			print(len(result))
			return False
	else:
		return result			

def create_dataframe(table): # Funkce pro vytvoření dataframu a ukládání do něho výsledků parsovani. Argumentem je matice "tělo" dataframu. Vrátí dataframe

	columns=['Jméno obce', 'Okres', 'Kraj', 'Počet voličů', 'Počet odevzdaných hlasů', 'Počet platných hlasů', 'Počet volebních okrsků', 'Číslo obce', 'Občanská demokratická strana', 'Řád národa - Vlastenecká unie', 'CESTA ODPOVĚDNÉ SPOLEČNOSTI', 'Česká str.sociálně demokrat.', 'Radostné Česko', 'STAROSTOVÉ A NEZÁVISLÍ', 'Komunistická str.Čech a Moravy', 'Strana zelených', 'ROZUMNÍ-stop migraci,diktát.EU', 'Strana svobodných občanů', 'Blok proti islam.-Obran.domova', 'Občanská demokratická aliance', 'Česká pirátská strana', 'Referendum o Evropské unii', 'TOP 09', 'ANO 2011', 'Dobrá volba 2016', 'SPR-Republ.str.Čsl. M.Sládka', 'Křesť.demokr.unie-Čs.str.lid.', 'REALISTÉ', 'SPORTOVCI', 'Dělnic.str.sociální spravedl.', 'Svob.a př.dem.-T.Okamura (SPD)', 'Strana Práv Občanů']

	df = pd.DataFrame(table, columns = columns)
	for column in df.columns:
		if column not in ['Jméno obce', 'Okres', 'Kraj']:
			df[column] = df[column].apply(int)
	#df.to_csv('dataframe.csv', encoding='utf-8', index=False)	
	return df


def analyze_obec(jObec, dataframe): # Funkce analizy obce. Přijímá název obce a dataframe výsledků voleb
	
	# selektovami z dataframu daty voleb
	obec = dataframe[dataframe[dataframe.columns[0]] == str(jObec)] # vybírám 1 řádek z df pro naši obec podle jména
	iObce  = obec.index # zjistím jeho pořadové číslo v df
		
	kraj = dataframe.loc[iObce,'Kraj'].values[0] # kraj z řádku naši obci, řádek vybírám pomocí loc
	okres = dataframe.loc[iObce,'Okres'].values[0] # okres z radku naši obci
	krajeRows = dataframe[dataframe[dataframe.columns[2]] == kraj] # vybírám všichni řádky kde kraj je jako u naši obci
	okseryRows = dataframe[dataframe[dataframe.columns[1]] == okres] # vybírám všichni řádky kde okres je jako u naši obci
	pvObec = obec[dataframe.columns[3]].values[0] #  Počet voličů v obci
	pvOkres = okseryRows[dataframe.columns[3]].values.sum() # součet (sum()) počtu voličů v okresu, kde okres je jako u naši obci
	pvKraj = krajeRows[dataframe.columns[3]].values.sum() # součet (sum()) počtu voličů v kraje, kde kraj je jako u naši obci
	prcPvObec = round(pvObec/pvKraj*100, 2) # procento z kraje
	prcPvObec2 = round(pvObec/pvOkres*100, 2) # procento z okresu
	# analogicky pro Počet platných hlasů
	pphObec = obec[dataframe.columns[5]].values[0]
	pphOkres = okseryRows[dataframe.columns[5]].values.sum()
	pphKraj = krajeRows[dataframe.columns[5]].values.sum()
	prcPphObec = round(pphObec/pphKraj*100, 2)
	prcPphObec2 = round(pphObec/pphOkres*100, 2)

	strany = obec[dataframe.columns[8:32]] # vybírám sloupci 8-32, které mají v sobě info o počtu hlasů za každou stranu
	vyhrala = strany[strany.columns[np.argmax(strany)]].name # np.argmax vrátí element df z největší hodnotou. vytáhnu název strany z největším počtem hlasů
	dostala = strany[strany.columns[np.argmax(strany)]].values[0] # vytáhnu počet hlasů strany z největším počtem hlasů

	# Výpis výsledků
	print("Vysledky analyzy volby v obci "+str(jObec))
	print("Počet voličů v obci: "+str(pvObec))
	print("% od počtu okresu: " + str(prcPvObec2) + "%")
	print("% od počtu kraje: " + str(prcPvObec) + "%")
	print("Počet platných hlasů: "+str(pphObec))
	print("% od počtu okresu: " + str(prcPphObec2) + "%")
	print("% od počtu kraje: " + str(prcPphObec) + "%")

	print("V obci "+str(jObec)+" strana "+ str(vyhrala) + " a dostala "+ str(dostala)+" hlasu")


def make_graphs(dataframe): # Funkce kreslení grafů. Prijma dataframe, vykreslí 3 grafů
	
	strany = dataframe[dataframe.columns[8:32]].sum() # vyfiltruju jenom sloupci z statistiky stran
	strany = pd.to_numeric(strany) # převedu do číselného formátu
	sortedStrany = strany.sort_values(ascending=False) # seřadím od většího k menšímu
	top10 = sortedStrany[0:10] # výběru top 10
	
	top10.plot.bar() # Sloupcový graf, který bude zobrazovat agregované údaje za celý kraj – počet získaných hlasů dle 10 nejúspěšnějších stran v kraji

	oskresyHlasy = dataframe[[dataframe.columns[1],dataframe.columns[4]]] # vyfiltruju z df jenom název okresu a počet hlasů
	oskresyHlasyGR = oskresyHlasy.groupby(dataframe.columns[1]) # třídím daty podle okresu
	kolecko_names = list() 
	kolecko_values = list()
	for okres in oskresyHlasyGR.groups: # projdu jednotlivé okresy
		kolecko_names.append(okres) # přidám název okresu
		kolecko_values.append(oskresyHlasyGR.get_group(okres).sum()[1]) # přidám součet hlasů v okresu
	
	if len(kolecko_names) == len(kolecko_values): # zkontroluju, že minulý krok byl úspěšný
		# Koláčový graf, který bude zobrazovat počet odevzdaných hlasů v jednotlivých okresech
		fig1, ax1 = plt.subplots() # definice
		ax1.pie(kolecko_values, labels=kolecko_names, autopct='%1.2f%%')
		ax1.axis('equal') # forma kolečka
		ax1.legend(loc='upper left', bbox_to_anchor=(-0.10, 0.5)) # pozice kolečka

	
	pvPop = dataframe[[dataframe.columns[3],dataframe.columns[4]]] # vyfiltruju jenom sloupci ze statistiky počtem voličů a počtem odevzdaných hlasů
	print(ggplot(pvPop, aes(x='Počet voličů', y='Počet odevzdaných hlasů')) + geom_point()) # zobrazím ggplot
		
	plt.show() # zobrazím grafy matplotlib
	

def parse_volby(obec = 'Běstvina'): # hlavní funkce. Přijímá název obce

	baseUrl = 'https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ' # url webu z vysledkama voleb
	kraj = 'Pardubický kraj'
	homepage = parse(baseUrl) # parsovani 1 stránky z statistiky státu
	if not homepage: # kontrola úspěšnosti parsovani
		quit('Příklad 4, Doslo k chybe parsovani homepage')

	tables = homepage.body.find("div", id="content").find("div", id="publikace").select("table.table") # získání tabulek z kraje

	tableMyKraj = None 


	for table in tables: # cyklusem procházím tabulky
		if 'část '+kraj in table.caption.text: # pokud tabulka má v caption můj kraj přidám ji do tableMyKraj a skončím cyklus break
			tableMyKraj = table
			break

	if not tableMyKraj: # pokud taková tabulka neexistuje, skončím skript z hláškou
		exit('Není informace o '+kraj)	
	
	matice = np.array([]) # nadefinuju matice pro výsledky
	
	for row in tableMyKraj.select('tr'): # získám všichni řádky z tabulky
		cells = row.find_all('td') # uložím a ověřím buňky
		if cells:
			
			odkaz = urljoin(baseUrl, cells[3].a.get("href")) # získám odkaz na jednotlivý okres
			jOkres = cells[1].text # získám název obce

			okresy = parseOkres(odkaz, baseUrl) # získám data ze stránky okresu
			for url, data in okresy.items(): # projdu cyklusem výsledek parseOkres()
				jObec = data['name']
				cObec = data['id'].strip()
				
				resultRow = parseObec(url, jObec, jOkres, kraj, cObec) # získám data ze stránky okraje
				if resultRow:
					try: # do prázdné matice nedá se provést vstack, do neprázdné potřebuju uložit další řádek, nedoplnit ten (vstack)
						matice = np.vstack((matice, np.array(resultRow)))
					except:
						matice = np.hstack((matice, np.array(resultRow)))
					
					
	dataFR = create_dataframe(matice) # zkonvertuju matice do dataframe
	analyze_obec(obec ,dataFR) # spustím analýzu obce
	make_graphs(dataFR) # vykreslím grafy
	return True	


#parse_volby('Běstvina')
#parse_volby('Bučina')








