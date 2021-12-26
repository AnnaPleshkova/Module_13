ticket = int(input("Сколько билетов хотите приобрести?\n"))
price = []
for i in range(1, ticket + 1):
    age = int(input(f"Возраст {i} участника?\n"))
    if age < 18:
        price.append(0)
    elif 18 <= age < 26:
        price.append(990)
    elif 26 <= age < 100:
        price.append(1390)
    else:
        print("Внимание! Некорретно указан возраст участника.")
if ticket > 3:
    print("Ура!!!Вам предоставлена скидка 10 % \nИТОГО стоимость заказа со скидкой составила:", sum(price) - (sum(price)/100) * 10)
else:
    print("Общая стоимость заказа:", sum(price))