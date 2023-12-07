#pip install requests (to be able to get HTML pages and load them into Python)
#pip install bs4 (for beautifulsoup - python tool to parse HTML)


from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


##############FOR MACS THAT HAVE ERRORS LOOK HERE################
## https://timonweb.com/tutorials/fixing-certificate_verify_failed-error-when-trying-requests_html-out-on-mac/

############## ALTERNATIVELY IF PASSWORD IS AN ISSUE FOR MAC USERS ########################
##  > cd "/Applications/Python 3.6/"
##  > sudo "./Install Certificates.command"



url = 'https://www.worldometers.info/coronavirus/country/us'
# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

print(soup.title.text)


#SOME USEFUL FUNCTIONS IN BEAUTIFULSOUP
#-----------------------------------------------#
# find(tag, attributes, recursive, text, keywords)
# findAll(tag, attributes, recursive, text, limit, keywords)

#Tags: find("h1","h2","h3", etc.)
#Attributes: find("span", {"class":{"green","red"}})
#Text: nameList = Objfind(text="the prince")
#Limit = find with limit of 1
#keyword: allText = Obj.find(id="title",class="text")

table_rows = soup.findAll('tr')
table_columns = soup.findAll('tc')
state_death_ratio = ""
state_best_testing = ""
state_worst_testing = ""
highest_death_ratio = 0.0
highest_testing_ratio = 0.0
lowest_testing_ratio = 100.0
lowest_death_ratio = 100.0



# print(table_rows)
# print(table_columns)

for row in table_rows[2:52]:
    td = row.findAll("td")
    state = td[1].text
    total_cases = int(td[2].text.replace(",",""))
    total_deaths = int(td[4].text.replace(",",""))
    total_tests = int(td[10].text.replace(",",""))
    population = int(td[12].text.replace(",",""))

    # print(state, total_cases, total_deaths, total_tests, population)

    # print("state", state)
    # print("total cases", total_cases)
    # print("total deaths", total_deaths)
    # print("total tests", total_tests)
    # print("population", population)
    # input()

    death_ratio = total_deaths/total_cases
    test_ratio = total_tests/population

    if death_ratio > highest_death_ratio:
        highest_death_ratio = death_ratio
        state_death_ratio = state

    if test_ratio > highest_testing_ratio:
        highest_testing_ratio = test_ratio
        state_best_testing = state
    if test_ratio < lowest_testing_ratio:
        lowest_testing_ratio = test_ratio
        state_worst_testing = state





print("State with the highest death ratio is:",state_death_ratio)
print("Death Ratio", format(highest_death_ratio, ".2%"))
print()
print()
print("State with the highest testing ratio is:",state_best_testing)
print("Testing Ratio", format(highest_testing_ratio, ".2%"))
print()
print()
print("State with the lowset testing ratio is:",state_worst_testing)
print("Testing Ratio", format(lowest_testing_ratio, ".2%"))
print()
print()