

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

url = 'https://www.coingecko.com/'
# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

print(soup.title.text)

table_rows = soup.findAll('tr')
table_columns = soup.findAll('tc')
# state_death_ratio = ""
# state_best_testing = ""
# state_worst_testing = ""
# highest_death_ratio = 0.0
# highest_testing_ratio = 0.0
# lowest_testing_ratio = 100.0
# lowest_death_ratio = 100.0



# print(table_rows)
# print(table_columns)
name_crypto = []
ticker_crypto = []
current_price_crypto = []
percent_change_crypto = []
percent_change_sign = []
for row in table_rows[1:6]:
    td = row.findAll("td")
    # print(td[5])
    up_or_down = row.findAll("span", {"class":{"gecko-up", "gecko-down"}})
    # for i in range(len(up_or_down)):
    #     print(  [up_or_down[i]]  )
    # print(  [up_or_down[1]]  )
    # print(up_or_down[1])
    if "gecko-up" in str((up_or_down[1])):
        percent_change_sign.append(1)
    if "gecko-down" in str((up_or_down[1])):
        percent_change_sign.append(-1)
    # input()


#SOME USEFUL FUNCTIONS IN BEAUTIFULSOUP
#-----------------------------------------------#
# find(tag, attributes, recursive, text, keywords)
# findAll(tag, attributes, recursive, text, limit, keywords)

#Tags: find("h1","h2","h3", etc.)
#Attributes: find("span", {"class":{"green","red"}})
#Text: nameList = Objfind(text="the prince")
#Limit = find with limit of 1
#keyword: allText = Obj.find(id="title",class="text")


    name_and_ticker = td[2].text
    # crypto = crypto.replace('\n', "")
    name_and_ticker = name_and_ticker.replace(' ', "")
    name_and_ticker = name_and_ticker.splitlines()
    # print(crypto)
    x = ''
    #professor Bhojwani or Kinley: I **stumbled** (guess-and-checked) into this stupid yet effective way of making a proper list out of the output I got from CoinGecko.
    #Please enjoy by turning on the print statements below.
    for x in name_and_ticker:
        # print("0",name_and_ticker)
        name_and_ticker.remove('')
        # print("1",name_and_ticker)
        name_and_ticker.remove('')
        # print("2",name_and_ticker)
        name_and_ticker.remove('')
        # print("3",name_and_ticker)
    # print(crypto)
    # print( [crypto] )
    # print(crypto[0])
    # print(crypto[1])
    name_crypto.append(name_and_ticker[0])
    ticker_crypto.append(name_and_ticker[1])
    current_price = td[4].text.strip().replace("$", "").replace(",", "")
    # print(  [current_price]  )
    current_price_crypto.append(current_price)
    percent_change = float(td[6].text.strip().replace("%", ""))/100
    percent_change_crypto.append(percent_change)
    # print(  [percent_change]  )
# print(name_crypto)
# print(ticker_crypto)
# print(current_price_crypto)
# print(percent_change_crypto)
# print(percent_change_sign)
F = 0
print("Top 5 Cryptocurrencies in the Market Right Now!\n")
for i in name_crypto:
    print(f"Name: {name_crypto[F]}")
    print(f"Ticker: {ticker_crypto[F]}")
    print(f"Rank: {F+1}")
    print(f"Current Price: ${current_price_crypto[F]}")
    #the below code will help determine the sign and magnitude of the change in crypto prices
    print(f"Price Change (24h): {float(percent_change_crypto[F])*float(percent_change_sign[F])*100}%")
    print(f"Price Change (24h): ${round(float(current_price_crypto[F])*float(percent_change_sign[F])*float(percent_change_crypto[F]),2)}")
    if ticker_crypto[F] == "ETH" and float(current_price_crypto[F]) > 2000:
        print("YAY! Professor Bhojwani, you get to SELL ETH!")
    print("\n")
    F += 1
    # input()
    # total_cases = int(td[2].text.replace(",",""))
    # total_deaths = int(td[4].text.replace(",",""))
    # total_tests = int(td[10].text.replace(",",""))
    # population = int(td[12].text.replace(",",""))

    # print(state, total_cases, total_deaths, total_tests, population)

    # print("state", state)
    # print("total cases", total_cases)
    # print("total deaths", total_deaths)
    # print("total tests", total_tests)
    # print("population", population)
    # input()

    # death_ratio = total_deaths/total_cases
    # test_ratio = total_tests/population

    # if death_ratio > highest_death_ratio:
    #     highest_death_ratio = death_ratio
    #     state_death_ratio = state

    # if test_ratio > highest_testing_ratio:
    #     highest_testing_ratio = test_ratio
    #     state_best_testing = state
    # if test_ratio < lowest_testing_ratio:
    #     lowest_testing_ratio = test_ratio
    #     state_worst_testing = state





# print("State with the highest death ratio is:",state_death_ratio)
# print("Death Ratio", format(highest_death_ratio, ".2%"))
# print()
# print()
# print("State with the highest testing ratio is:",state_best_testing)
# print("Testing Ratio", format(highest_testing_ratio, ".2%"))
# print()
# print()
# print("State with the lowset testing ratio is:",state_worst_testing)
# print("Testing Ratio", format(lowest_testing_ratio, ".2%"))
# print()
# print()