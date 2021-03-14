import bs4, requests

print("Developed by Michele Picciotti\n")

link_world = "https://news.google.com/covid19/map?hl=it&gl=IT&ceid=IT%3Ait"

response_world = requests.get(link_world)
response_world.raise_for_status()
soup_world = bs4.BeautifulSoup(response_world.text, 'html.parser') #I extract the html text from the web page (saved in the response variable)

####################WORLD####################

print("MONDO\n")


div_info_world = soup_world.find_all('div', class_='UvMayb')


world_cases = div_info_world[0]
print("Casi totali:", world_cases.get_text())

world_deaths = div_info_world[1]
print("Decessi:", world_deaths.get_text())

world_doses = div_info_world[2]
print("Dosi totali somministrate:", world_doses.get_text())

vaccinated_people_world = div_info_world[3]
print("Persone vaccinate:", vaccinated_people_world.get_text())

####################WORLD END####################

link_it = "https://lab24.ilsole24ore.com/coronavirus/"
response_it = requests.get(link_it)
response_it.raise_for_status()
soup_it = bs4.BeautifulSoup(response_it.text, 'html.parser')

####################TOTAL ITALY####################

print("\nITALIA TOTALE\n")


p_info_it_tot = soup_it.find_all('p', class_='count-text_total')

cases_tot_it = p_info_it_tot[0]
print("Casi totali:", cases_tot_it.get_text().replace("\n", "").replace("Totali", "").strip()) #I eliminate the unnecessary text and spaces contained in the paragraph
      
deaths_tot_it = p_info_it_tot[1]
print("Decessi:", deaths_tot_it.get_text().replace("\n", "").replace("Totali", "").strip())

healed_tot_it = p_info_it_tot[2]
print("Dimessi/guariti:", healed_tot_it.get_text().replace("\n", "").replace("Totali", "").strip())

currently_positive_tot_it = p_info_it_tot[3]
print("Attualmente positivi:", currently_positive_tot_it.get_text().replace("\n", "").replace("Totali", "").strip())

intensive_care_tot_it = p_info_it_tot[4]
print("Terapia intensiva:", intensive_care_tot_it.get_text().replace("\n", "").replace("Totali", "").strip())

'''
METTERE SECONDO LINK
doses_tot_it = p_info_it_tot[2]
print("Dosi totali somministrate:", doses_tot_it.get_text())

vaccinated_people_tot_it = p_info_it_tot[3]
print("Persone vaccinate:", vaccinated_people_tot_it.get_text())
'''

####################TOTAL ITALY END####################

h2_info_it_daily = soup_it.find_all('h2')

####################DAILY ITALY####################

print("\nITALIA OGGI\n")


daily_cases_it = h2_info_it_daily[0]
print("Casi totali:", daily_cases_it.get_text())

daily_deaths_it = h2_info_it_daily[1]
print("Decessi:", daily_deaths_it.get_text())

daily_healed_it = h2_info_it_daily[2]
print("Dimessi/guariti:", daily_healed_it.get_text())

currently_positive_it = h2_info_it_daily[3]
print("Attualmente positivi:", currently_positive_it.get_text())

daily_intensive_care_it = h2_info_it_daily[4]
print("Terapia intensiva:", daily_intensive_care_it.get_text()) 

'''
SECONDO LINK
daily_doses_it = strong_info_it_daily[3]
print("Dosi totali somministrate:", daily_doses_it.get_text())
'''

####################END PROGRAM####################
