from BankAccount import BankAccount

accounts_list=[BankAccount("NL01BANK0123456789", 1000.00),BankAccount("BE68BANK12345678",500.00),BankAccount("NL03BANK1357924680",1200.50) ]

def transfer_funds(source_account: str, target_account: str, amount: float, accounts_list:list):
    if amount <= 0:
        return f"Bedrag moet groter zijn dan 0."

    #alle namen die in account_list zitten in een apparte lijst zetten om te checken of
    #de ingegeven account aanwezig zijn.
    lijst_namen =[]
    for i in range(len(accounts_list)):
        lijst_namen.append(accounts_list[i].account_number)
    assert source_account in lijst_namen and target_account in lijst_namen, "Geef accounts die aanwezig zijn in de lijst"

    #withdraw uitvoeren
    for i in range(len(accounts_list)):
        if accounts_list[i].account_number == source_account:
            assert accounts_list[i].balance > amount, "Onvoldoende saldo."

            assert accounts_list[i].amount_withdrawn_today < accounts_list[i].daily_limit, "Daglimiet overschreden."

            accounts_list[i].withdraw(amount)

    #depost uitvoeren
    for i in range(len(accounts_list)):
        if accounts_list[i].account_number == target_account:
            accounts_list[i].deposit(amount)
            return f"Overboeking geslaagd."

def new_day(accounts_list: list):
    for i in range(len(accounts_list)):
        accounts_list[i].reset_daily_limit()


#hieronder bevinden de testen, test 2 en 3 staan in commentaar gezien ze foutmeldingen zijn
#anders zorgen ze ervoor dat de resultaat van de andere testen niet gezien worden.

#test1
transfer_funds("NL01BANK0123456789","BE68BANK12345678",200.00,accounts_list)

#test2
#transfer_funds("NL01BANK0123456789","BE11111111111111",200.00,accounts_list)

#test3
accounts_list[2].withdraw(1100.0)
#transfer_funds("NL03BANK1357924680","NL01BANK0123456789",1.00,accounts_list)

#test4
new_day(accounts_list)






