"""Convert the currencies based on the exchange rate."""


def main():
    usd = eval(input("Please enter the amount in U.S. Dollars:"))


    Euros = usd * 0.8815
    China_Yuan = usd * 6.3385
    India_Rupees = usd * 74.3827
    UK_Pounds = usd * 0.7376
    Canada_Dollars = usd * 1.2581

    print()
    print(usd, 'in U.S. Dollars may be exchanged for:')
    print(Euros,'Euros')
    print(China_Yuan, 'China Yuan')
    print(India_Rupees, 'India Rupees')
    print(UK_Pounds, 'UK Pounds')
    print(Canada_Dollars, 'Canada Dollars')



main()