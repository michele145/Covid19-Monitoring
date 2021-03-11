import bs4, requests

print("Developed by Michele Picciotti\n")

link_mondo = "https://news.google.com/covid19/map?hl=it&gl=IT&ceid=IT%3Ait"

response_mondo = requests.get(link_mondo)
response_mondo.raise_for_status()
soup_mondo = bs4.BeautifulSoup(response_mondo.text, 'html.parser') #estraggo dalla pagina web (salvata nella variabile response), il testo html

####################MONDO####################

print("MONDO\n")


div_info_mondo = soup_mondo.find_all('div', class_='UvMayb')


casi_mondo = div_info_mondo[0]
print("Casi totali:", casi_mondo.get_text())

decessi_mondo = div_info_mondo[2]
print("Decessi:", decessi_mondo.get_text())

dosi_mondo = div_info_mondo[3]
print("Dosi totali somministrate:", dosi_mondo.get_text())

persone_vaccinate_mondo = div_info_mondo[4]
print("Persone vaccinate:", persone_vaccinate_mondo.get_text())

####################FINE MONDO####################

link_it = "https://news.google.com/covid19/map?hl=it&gl=IT&ceid=IT%3Ait&mid=%2Fm%2F03rjj"
response_it = requests.get(link_it)
response_it.raise_for_status()
soup_it = bs4.BeautifulSoup(response_it.text, 'html.parser')

####################ITALIA TOTALE####################

print("\nITALIA TOTALE\n")


div_info_it_tot = soup_it.find_all('div', class_='UvMayb')

casi_tot_it = div_info_it_tot[0]
print("Casi totali:", casi_tot_it.get_text())

decessi_tot_it = div_info_it_tot[1]
print("Decessi:", decessi_tot_it.get_text())

dosi_tot_it = div_info_it_tot[0]
print("Dosi totali somministrate:", dosi_tot_it.get_text())

persone_vaccinate_tot_it = div_info_it_tot[3]
print("Persone vaccinate:", persone_vaccinate_tot_it.get_text())

####################FINE ITALIA TOTALE####################

div_info_it_oggi = soup_it.find_all('strong')

####################ITALIA GIORNALIERO####################

print("\nITALIA OGGI\n")


casi_oggi_it = div_info_it_oggi[0]
print("Casi totali:", casi_oggi_it.get_text())

decessi_oggi_it = div_info_it_oggi[2]
print("Decessi:", decessi_oggi_it.get_text())

dosi_oggi_it = div_info_it_oggi[3]
print("Dosi totali somministrate:", dosi_oggi_it.get_text())

####################FINE PROGRAMMA####################