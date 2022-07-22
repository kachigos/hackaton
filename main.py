from hack import delete_car, list_of_cars, retrieve_data, create_car, update_car

def main():
    print('privet tebe doctepny next funtion: \n\tLIST-1:\n\tRETRIEVE-2\n\tCREATE-3\n\tUPDATE-4\n\tDELETE-5')
    choice = input('vvedite deicstie(1,2,3,4,5):  ')
    if choice == '1':
        print(list_of_cars())
    elif choice == '2':
        print(retrieve_data())
    elif choice == '3':
        print(create_car())
    elif choice == '4':
        print(update_car())
    elif choice == '5':
        print(delete_car())
    else:
        print('invalid choice!!')
        main()
    ask = input('hotite prodolzhit\?YES/NO')
    if ask.lower() == 'yes':
        main()
    else:
        print('poka! poka')
main()