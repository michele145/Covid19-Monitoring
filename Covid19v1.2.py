import bs4
import requests
import streamlit as st

st.title("Developed by Michele Picciotti\n")

link_world = "https://news.google.com/covid19/map?hl=it&gl=IT&ceid=IT%3Ait"

response_world = requests.get(link_world)
response_world.raise_for_status() #Check if the site responds
soup_world = bs4.BeautifulSoup(response_world.text, 'html.parser') #I extract the html text from the web page (saved in the response variable)

####################WORLD####################

st.header("WORLD")


div_info_world = soup_world.find_all('div', class_='UvMayb')


world_cases = div_info_world[0]
st.write("Casi totali:", world_cases.get_text())

world_deaths = div_info_world[2]
st.write("Decessi:", world_deaths.get_text())

world_doses = div_info_world[3]
st.write("Dosi totali somministrate:", world_doses.get_text())

vaccinated_people_world = div_info_world[4]
st.write("Persone vaccinate:", vaccinated_people_world.get_text())

####################WORLD END####################

first_link_it = "https://lab24.ilsole24ore.com/coronavirus/"
second_link_it = "https://news.google.com/covid19/map?hl=it&gl=IT&ceid=IT%3Ait&mid=%2Fm%2F03rjj" #link for vaccines

first_response_it = requests.get(first_link_it)
first_response_it.raise_for_status()
first_soup_it = bs4.BeautifulSoup(first_response_it.text, 'html.parser')


second_response_it = requests.get(second_link_it)
second_response_it.raise_for_status()
second_soup_it = bs4.BeautifulSoup(second_response_it.text, 'html.parser')

####################TOTAL ITALY####################

st.header("TOTAL ITALY")


p_info_it_tot = first_soup_it.find_all('p', class_='count-text_total')
div_info_it_tot = second_soup_it.find_all('div', class_='UvMayb')


cases_tot_it = p_info_it_tot[0]
st.write("Casi totali:", cases_tot_it.get_text().replace("\n", "").replace("Totali", "").strip()) #I eliminate the unnecessary text and spaces contained in the paragraph
      
deaths_tot_it = p_info_it_tot[1]
st.write("Decessi:", deaths_tot_it.get_text().replace("\n", "").replace("Totali", "").strip())

healed_tot_it = p_info_it_tot[2]
st.write("Dimessi/guariti:", healed_tot_it.get_text().replace("\n", "").replace("Totali", "").strip())

currently_positive_tot_it = p_info_it_tot[3]
st.write("Attualmente positivi:", currently_positive_tot_it.get_text().replace("\n", "").replace("Totali", "").strip())

intensive_care_tot_it = p_info_it_tot[4]
st.write("Terapia intensiva:", intensive_care_tot_it.get_text().replace("\n", "").replace("Totali", "").strip())

doses_tot_it = div_info_it_tot[2]
st.write("Dosi totali somministrate:", doses_tot_it.get_text())

vaccinated_people_tot_it = div_info_it_tot[3]
st.write("Persone con vaccinazione completata:", vaccinated_people_tot_it.get_text())

####################TOTAL ITALY END####################

h2_info_it_daily = first_soup_it.find_all('h2')
div_info_it_daily = second_soup_it.find_all('div', class_='UvMayb')

####################DAILY ITALY####################

st.header("ITALY TODAY")


daily_cases_it = h2_info_it_daily[0]
st.write("Casi totali:", daily_cases_it.get_text())

daily_deaths_it = h2_info_it_daily[1]
st.write("Decessi:", daily_deaths_it.get_text())

daily_healed_it = h2_info_it_daily[2]
st.write("Dimessi/guariti:", daily_healed_it.get_text())

currently_positive_it = h2_info_it_daily[3]
st.write("Attualmente positivi:", currently_positive_it.get_text())

daily_intensive_care_it = h2_info_it_daily[4]
st.write("Terapia intensiva:", daily_intensive_care_it.get_text()) 

daily_doses_it = div_info_it_daily[2]
st.write("Dosi totali somministrate:", daily_doses_it.get_text())

####################END PROGRAM####################