from menu import Menu

# Пример использования
def action1():
    print("Выполняется действие 1")

def test_menu():
    # Создаем главное меню
    main_menu = Menu("Главное меню")

    # Создаем подменю
    settings_menu = Menu("Настройки", main_menu)
    info_menu = Menu("Информация", main_menu)

    # Добавляем пункты в главное меню
    main_menu.add_action_item("Пункт 1", action1)

    main_menu.add_action_item("Пункт 2", lambda: print("Выполняется действие 2"))

    main_menu.add_submenu_item("Настройки", settings_menu)
    main_menu.add_submenu_item("Информация", info_menu)

    # Добавляем пункты в меню настроек
    settings_menu.add_action_item("Изменить параметр 1", lambda: print("Изменяем параметр 1..."))
    settings_menu.add_action_item("Изменить параметр 2", lambda: print("Изменяем параметр 2..."))
    settings_menu.add_action_item("Сбросить настройки", lambda: print("Сброс настроек..."))
    settings_menu.add_action_item("Закрыть настроек", lambda: settings_menu.stop())

    # Добавляем пункты в меню информации
    info_menu.add_action_item("О программе", lambda: print("Консольное меню v1.0\nРазработано на Python"))
    info_menu.add_action_item("Помощь", lambda: print("Управление:\n"
        "Стрелки Вверх/Вниз или W/S - навигация\n"
        "Enter или Space - выбор пункта\n"
        "Esc - выход/возврат"))

    # Демонстрация удаления пункта меню (раскомментировать для тестирования)
    # main_menu.remove_item("Пункт 1")

    # Запускаем главное меню
    main_menu.run()


if __name__ == "__main__":
    test_menu()
