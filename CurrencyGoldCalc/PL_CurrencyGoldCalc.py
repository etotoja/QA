from requests import get


print("Witaj w kalkulatorze kursu walut/złota CurrencyGoldCalc")
print("Program pobiera dane o aktualnym kursie (w PLN) wybranej waluty bądź złota w danym dniu wykorzystując dane NBP.")


print("Wpisz 1 by przejść do kursu walut")
choice = input(print("Wpisz 2 by przejść do kursu złota"))

if choice == "1":
    currency_code = input("Podaj 3 literowy kod waluty, np USD, EUR, CHF, etc: ")
    
    currency_selected = currency_code

    currency_code_request = get(f"http://api.nbp.pl/api/exchangerates/rates/a/{currency_code}/?format=json")

    api_currency_code = currency_code_request.json()

    print(f'Wybrana waluta: {api_currency_code["currency"]}')
    print(f'Obecny kurs: 1 {api_currency_code["code"].upper()} = {api_currency_code["rates"][0]["mid"]} PLN')

    currency_date = input(f'Wybierz inną datę dla waluty {api_currency_code["currency"]} (RRRR-MM-DD): ')

    request = get(f"http://api.nbp.pl/api/exchangerates/rates/a/{currency_code}/{currency_date}/?format=json")

    api_data = request.json()


    ##dodatkowy komunikat na wypadek bledu 404 (albo innego niz 200)??


    currency_rate = api_data["rates"][0]["mid"]
    print(f'Kurs dla waluty {currency_code.upper()}  ({api_data["currency"]}) w dniu {currency_date}:')
    print(f'1 {currency_code.upper()} = {currency_rate:.2f} PLN')
    x = input("Wcisnij dowolny klawisz aby zakończyć program.")

elif choice == "2":
    print("Wybrano kurs złota")
    gold_request = get("http://api.nbp.pl/api/cenyzlota/?format=json")
    api_gold_request = gold_request.json()
    
    print(f'Aktualny, na dzień {api_gold_request[0]["data"]} kurs złota 1g o próbie 1000 to: {api_gold_request[0]["cena"]} PLN')

    gold_date = input("Wybierz inną datę kursu złota (RRRR-MM-DD): ")

    date_gold_request = get(f"http://api.nbp.pl/api/cenyzlota/{gold_date}/?format=json")

    api_date_gold_request = date_gold_request.json()


    ##dodatkowy komunikat na wypadek bledu 404 (albo innego niz 200)??
            #if response.status_code != 200:
                #continue


    print(f'Kurs 1g złota o próbie 1000 w dniu {api_date_gold_request[0]["data"]}: {api_date_gold_request[0]["cena"]} PLN')
    x = input("Wcisnij dowolny klawisz aby zakończyć program.")
