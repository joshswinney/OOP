import CellPhoneClass as cp

def main():

    my_phone = cp.CellPhone

    manufact = input("Enter manufacturer: ")
    model = input("Enter model number: ")
    price = input("Enter retail price: ")

    my_phone.get_manufact()
    my_phone.get_model()
    my_phone.get_retail_price()

main()