while True:
    print("Доступная пицца:")
    print("Доступные пиццы:\n 1.Маргарита\n 2.Пепперони\n 3.Грибная\n 4.Четыре сыра\n 5.Капричоза\n")
    choice=int(input("Какую пиццу вы хотите заказать? Введите номер: "))
    number=int(input("Сколько пицц вы хотите заказать? Введите количество: "))
    if choice==1:
        name="Маргарита"
    if choice==2:
        name="Пепперони"
    if choice==3:
        name="Грибная"
    if choice==4:
        name="Четыре сыра"
    if choice==5:
        name="Капричоза"
    print(
        f"Вы заказали {number} пиццы под номером {choice}"
    )
    ready_to_leave=input("Готовы ли вы оставить отзыв? (да/нет): ")
    if ready_to_leave == "да":
        review=input("Пожалуйста оставьте свой отзыв: ")
        if "вкусно" in review.lower():
            print("Спасибо за отзыв! Пицца в подарок")
    else:
        break
        print("Спасибо за отзыв!")
    print = ("Заказ от 20.09.2024 принят")









