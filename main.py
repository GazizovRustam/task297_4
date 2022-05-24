def main():
    priceOil = float(input('Please enter price- Oil: '))
    # pricePetrol = float(input('Please enter price- Petrol: '))
    # priceInsurance = float(input('Please enter price- Insurance: '))
    # priceTires = float(input('Please enter price- Tires: '))
    # priceMaintenance = float(input('Please enter prise- Maintenance: '))
    totalPriceOil = getMonthPriceOil(priceOil)
    return totalPriceOil

def getMonthPriceOil(priceOil):
    return priceOil / 12


print(main())
