from db_manager import *

def menu():
    # 1. Проверяем таблицу при запуске
    create_table()
    
    while True:
        print("\n--- PhoneBook Menu (Practice 8) ---")
        print("1. Загрузить из CSV")
        print("2. Добавить/Обновить контакт (Upsert)") # Новое!
        print("3. Показать контакты (с пагинацией)")   # Новое!
        print("4. Поиск (через SQL-функцию)")          # Новое!
        print("5. Удалить контакт (через процедуру)") # Новое!
        print("0. Выход")
        
        choice = input("Выберите действие: ")
        
        if choice == '1':
            upload_from_csv('contacts.csv')
            
        elif choice == '2':
            name = input("Имя: ")
            phone = input("Телефон: ")
            # ВЫЗОВ НОВОЙ ПРОЦЕДУРЫ (она сама решит: обновить или создать)
            upsert_contact(name, phone) 
            
        elif choice == '3':
            limit = int(input("Сколько контактов показать? "))
            offset = int(input("Сколько пропустить (с какого начать)? "))
            rows = get_paged_contacts(limit, offset)
            for row in rows:
                print(f"ID: {row[0]} | Имя: {row[1]} | Тел: {row[2]}")
                
        elif choice == '4':
            pattern = input("Введите часть имени или телефона: ")
            # ВЫЗОВ НОВОЙ SQL-ФУНКЦИИ
            results = search_with_function(pattern)
            for row in results:
                print(row)
                
        elif choice == '5':
            val = input("Введите имя или телефон для удаления: ")
            # ВЫЗОВ ПРОЦЕДУРЫ УДАЛЕНИЯ
            delete_via_procedure(val)
            
        elif choice == '0':
            print("Пока!")
            break

if __name__ == "__main__":
    menu()