import math
import re
import os
import sys
import time



####################################################################################################################################################################################################################################################################################################
#	1. Příklad 
####################################################################################################################################################################################################################################################################################################

def prvocislo_test(n):
    n = int(n)
    if n < 2: # 0 a 1 najsou prvocisla
        return False
    elif n == 2: # 2 je prvocislo
        return True
    # proměnná-dělič, ktera bude se zvýšit o 1 v cyklu    
    i = 2
    # Limit, do kterého se zvýší i.
	# (Při kontrole prvocisla  stačí přepočítat děliče 2 až druhá odmocnina zkoumaného čísla.)
    limit = int(math.sqrt(n))

    while i <= limit:
        if n % i == 0:
            return False
        i += 1

    return True


def task1(minv: int, maxv :int):  

	if not maxv > minv:
		quit('max musi byt vice nez min')


	preresult = list()	

	for a in range(minv,maxv+1):
		if prvocislo_test(a):
			preresult.append(a)	
		
	total_count = maxv - minv + 1
	true_count = len(preresult)

	print('sekvenci prvočísel: ' + str(preresult))
	print('procento prvočísel: ', str(round(true_count/total_count*100,2))+'%')

#task1(25.1,35)

####################################################################################################################################################################################################################################################################################################
#	2. Příklad 
####################################################################################################################################################################################################################################################################################################

def validate(string, cut=False):
	if cut:
		preres = re.findall("\d+", string)
		if len(preres) == 0:
			return 'neznámé'
		else:
			return str(preres[0]).strip()
	if string == 'NA':
		return 'neznámé'
	else:
		return string.strip()

def task2():
	text="Karel Novak, 39 let, 1500, V:2,R:0,P:1; Jana Malá, 40 let, 2100, V:3, R:1,P:0; Pavel Mlady, 20 let, NA, V:1, R:NA, P:0"
	rows = text.split(';')
	for i in range(0,len(rows)):
		hrac = rows[i].split(',')
		print("|{:-^38}|".format("Karta hráče "))
		print("|{:38}|".format("Jméno: "+validate(hrac[0].strip().split(' ')[0])))
		print("|{:38}|".format("Příjmení: "+validate(hrac[0].strip().split(' ')[1])))
		print("|{:38}|".format("Let: "+validate(hrac[1])))
		print("|Score:{:.>32}|".format(validate(hrac[2])+" bodů"))
		print("|Výhry: {: ^31}|".format(validate(hrac[3], True)))
		print("|Remíza:{: ^31}|".format(validate(hrac[4], True)))
		print("|Prohry:{: ^31}|".format(validate(hrac[5], True)))
		print("|{:-^38}|".format("<Hráč č. "+str(i)+">")+"\n\n")
		

#task2()		


####################################################################################################################################################################################################################################################################################################
#	3. Příklad 
####################################################################################################################################################################################################################################################################################################


# Pro toto řešení nepoužívejte jiné moduly než: os, sys, time, path, math!!!


#def walktree(top, callback):
#
#    listd = os.listdir(top)
#    listd.sort()

#    for f in listd:
#        pathname = os.path.join(top, f)
#        if os.path.isdir(pathname):
#            print("|{:.<84}|".format(os.path.basename(pathname)))
#            walktree(pathname, callback)
#        elif os.path.isfile(pathname):
#            # It's a file, call the callback function
#            #callback(pathname,f)
#            pass
#        else:
#            # Unknown file type, print a message
#            print('Skipping %s' % pathname)

def visitfile(filepath, name):
	stats = os.stat(filepath)
	index = name.index('.')
	print("|{: >19}|".format(name[:index])+"{: >16}".format(name[index:])+" |{: >18}|".format(round(stats.st_size / 1048576, 3))+"{: >26} |".format(time.ctime(stats.st_mtime)))


def walktree(mypath):
	listd = os.walk(mypath)
	
	for f in listd:
		folderpath = os.path.basename(mypath) + ' / ' +os.path.basename(f[0]) if f[0] != mypath else os.path.basename(f[0])
		print("| {:.<83}| ".format(folderpath+':'))
		

		if len(f[2]) > 0:
			#print(f[2])
			f[2].sort()
			for file in f[2]:
				pathname = os.path.join(f[0], file)
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
	




#get_me_info_about('/home/pinguin/Documents/Unicorn2020/Interpretace seminarka/test_script')




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
testovani('dataframe.csv')



