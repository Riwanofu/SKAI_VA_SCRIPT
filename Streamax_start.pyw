##################### IVANOV STREAMAX SCRIPT ######################################################

#################### ИМПОРТ БИБЛИОТЕК ДЛЯ РАБОТЫ СКРИПТА ####################

import keyboard
from playwright.sync_api import Playwright, expect, sync_playwright

#################### ПЕРЕМЕННАЯ ДЛЯ ИНИЦИАЛИЗАЦИИ ####################

def run(playwright: Playwright):

        ##################################################################################
    ###################### ВЫБОР ПУТЕЙ ФАЙЛОВ ###############################################
###############################################################################################                   #
                                                                                        #########              ####
    c29n = 'C:\\скрипт\\ST_C29N V3.3.28_RC24031970'                                     ##########         ########
    m1n = 'C:\\скрипт\\HY_X1N_AI_M0010_V3.5.8.16_RC24082970'                            ###########      ###############################
    adplus = 'C:\\скрипт\\ADPLUS2.0_V3.5.8.9_T240426.71_M0010'                          ###########   #### СЮДА ВПИСАТЬ ПУТИ ФАЙЛОВ ####
    config_3_ch = 'C:\\скрипт\\config'                                                  ###########      ###############################
    config_5_ch = 'C:\\скрипт\\config'                                                  ##########         ########
                                                                                        #########              ####
###############################################################################################                   #
    #########################################################################################
        ##################################################################################

    browser = playwright.chromium.launch(
        args=['--start-maximized'], headless=False)
    context = browser.new_context(no_viewport=True)
    page = context.new_page()

############################ НАЧАЛЬНЫЙ ЭКРАН ######################################################

    page.goto("http://192.168.240.1/login",
            wait_until='networkidle')

    page.locator("span").filter(
        has_text="中文（简体）EnglishPortuguêsEspañol").click()
    page.get_by_role("link", name="Русский").click()

    page.locator("#username").fill("admin")
    page.locator("#password").fill("admin")

    page.locator("#password").press("Enter")
    page.wait_for_timeout(110)

    page.goto('http://192.168.240.1/pages/preview',
            wait_until='domcontentloaded')

############################ ОБНОВЛЕНИЕ КАМЕРЫ C29N ###############################################

    #################### ВЫБОР ПРОШИВКИ C29N ####################

    def c29n_upgrade():

        page.goto('http://192.168.240.1/pages/maintenance',
            wait_until='domcontentloaded')

        page.get_by_role("link", name=" Обновить").click()
        page.wait_for_timeout(500)

        #################### ПОДГРУЗКА ФАЙЛА ИЗ СКРЫТОГО ПРОВОДНИКА ####################

        page.locator("#file_path_IPC_UPGRADE").click()
        with page.expect_file_chooser() as fc_info_c29n:
            page.locator("#upgrade div").filter(
                has_text="Обновление IPCПросматриватьОбновить").locator("span").click()

        file_с29n = fc_info_c29n.value
        file_с29n.set_files(c29n)

        page.locator("#upgrade div").filter(
            has_text="Обновление IPCПросматриватьОбновить").get_by_role("button").click()
        page.get_by_role(
            "cell", name="Все").locator("label").click()
        page.locator(
            "#edit_ipc_dialog_modal").get_by_role("button", name="Обновить").click()
        page.get_by_role("button", name=" Ok").click()

    def c29n_pass():
        pass

    #################### ЛОГИКА РАБОТЫ БЛОКА ####################

    while True:

        if keyboard.is_pressed('alt+1'):

            c29n_upgrade()
            
            while True:
                
                if keyboard.is_pressed('alt+1'):
                    continue
                break

        elif keyboard.is_pressed('alt+q' or 'alt+й'):

            c29n_pass()
            break

        elif keyboard.is_pressed('alt+r' or 'alt+к'):

            context.close()
            browser.close()
            exit()
            break

############################### ОБНОВЛЕНИЕ ТЕРМИНАЛА ##############################################

    #################### ВЫБОР ПРОШИВКИ M1N ####################

    def m1n_upgrade():

        page.goto('http://192.168.240.1/pages/maintenance',
            wait_until='domcontentloaded')

        expect(page.locator(
            "#maintenance_left_menu")).to_contain_text("Обновить")
        page.get_by_role("link", name=" Обновить").click()
        page.wait_for_timeout(500)

        page.locator("#file_path_remote_upgrade_device").click()

        #################### ПОДГРУЗКА ФАЙЛА ИЗ СКРЫТОГО ПРОВОДНИКА ####################

        with page.expect_file_chooser() as fc_info_terminal:
            page.locator("#upgrade div").filter(
                has_text="Обновление устройстваПросматриватьОбновить").locator("span").click()

        file_terminal = fc_info_terminal.value
        file_terminal.set_files(m1n)

        page.locator("#upgrade div").filter(
            has_text="Обновление устройстваПросматриватьОбновить").get_by_role("button").click()
        page.get_by_role("button", name=" Ok").click()

    #################### ВЫБОР ПРОШИВКИ ADPLUS ####################

    def adplus_upgrade():

        page.goto('http://192.168.240.1/pages/maintenance',
            wait_until='domcontentloaded')

        expect(page.locator(
            "#maintenance_left_menu")).to_contain_text("Обновить")
        page.get_by_role("link", name=" Обновить").click()
        page.wait_for_timeout(500)

        page.locator("#file_path_remote_upgrade_device").click()

        #################### ПОДГРУЗКА ФАЙЛА ИЗ СКРЫТОГО ПРОВОДНИКА ####################

        with page.expect_file_chooser() as fc_info_terminal:
            page.locator("#upgrade div").filter(
                has_text="Обновление устройстваПросматриватьОбновить").locator("span").click()

        file_terminal = fc_info_terminal.value
        file_terminal.set_files(adplus)

        page.locator("#upgrade div").filter(
            has_text="Обновление устройстваПросматриватьОбновить").get_by_role("button").click()
        page.get_by_role("button", name=" Ok").click()

    def terminal_pass():
        pass

    #################### ЛОГИКА РАБОТЫ БЛОКА ####################

    while True:

        if keyboard.is_pressed('alt+2'):

            m1n_upgrade()
            
            while True:
                
                if keyboard.is_pressed('alt+2'):
                    continue
                break

        elif keyboard.is_pressed('alt+3'):

            adplus_upgrade()

            while True:
                
                if keyboard.is_pressed('alt+3'):
                    continue
                break

        elif keyboard.is_pressed('alt+w' or 'alt+ц'):

            terminal_pass()
            break

        elif keyboard.is_pressed('alt+r' or 'alt+к'):

            context.close()
            browser.close()
            exit()
            break

########################### ПРОФИЛЬ 3 КАНАЛ #######################################################

    def config_3_channel():

        page.goto('http://192.168.240.1/pages/maintenance',
                wait_until='domcontentloaded')

        expect(page.locator(
            "#maintenance_left_menu")).to_contain_text("Конфигурация")
        page.get_by_role(
            "link", name=" Конфигурация").click()
        page.wait_for_timeout(500)

        page.locator("#file_path_pc_import_param").click()

        #################### ПОДГРУЗКА ФАЙЛА ИЗ СКРЫТОГО ПРОВОДНИКА ####################

        with page.expect_file_chooser() as fc_info_3:
            page.locator("#parameter div").filter(
                has_text="Импортировать параметрыПросматриватьИмпорт").locator("span").click()

        file_config_3 = fc_info_3.value
        file_config_3.set_files(config_3_ch)

        page.locator("#parameter div").filter(
            has_text="Импортировать параметрыПросматриватьИмпорт").get_by_role("button").click()
        page.get_by_role("button", name="OK").click()

        #################### ВХОД В НАСТРОЙКИ IPC ####################

        page.goto('http://192.168.240.1/pages/config',
                wait_until='domcontentloaded')

        page.get_by_role(
            "link", name="Наблюдение").click()
        page.get_by_role(
            "link", name=" Настройка IPC").click()

        page.get_by_role(
            "button", name="По умолчанию").click()

        #################### НАСТРОЙКА И ВЫКЛ 3 CH ДЛЯ КАЛИБРОВКИ ####################

        page.get_by_role(
            "row", name="3  ").locator("label").first.click()

        page.get_by_role(
            "button", name="").nth(2).click()
        page.locator("span").filter(
            has_text="По умолчаниюDSMMDVR").locator("span").click()

        page.get_by_role(
            "link", name="DSM").click()
        page.wait_for_timeout(100)
        page.locator(
            "#edit_ip_address").fill("10.100.100.100")
        page.get_by_role(
            "button", name="OK").click()
        page.wait_for_timeout(100)

        page.get_by_role(
            "row", name="10.100.100.100:9006:1  ").locator("span").first.click()

        page.locator(
            "#ipc_start_address").fill("1")

        page.get_by_role(
            "button", name="Сохранить").click()

        page.goto('http://192.168.240.1/pages/config',
                wait_until='domcontentloaded')
        page.wait_for_timeout(100)

        #################### КАЛИБРОВКА 3 КАНАЛА ####################

        page.get_by_role(
            "link", name="Тревога").click()
        page.get_by_role(
            "link", name=" AI приложение").click()
        expect(page.get_by_role(
            "listitem").filter(has_text="Алгоритм калибр")).to_be_visible()
        page.get_by_role(
            "listitem").filter(has_text="Алгоритм калибр").click()
        page.wait_for_timeout(120)

        page.get_by_role(
            "row", name="3").locator("input[name=\"use\"]").click()
        page.locator(
            "#calibration_list").get_by_role("link", name="DMS").click()
        page.get_by_role(
            "row", name="DMS").locator("input[name=\"mode\"]").click()
        page.get_by_role(
            "link", name="Калибровка").click()
        page.get_by_role(
            "cell", name="Калибровка").locator("span").nth(3).click()
        page.get_by_role(
            "link", name="Side").click()
        page.get_by_role(
            "button", name="Сохранить").click()
        page.get_by_role("button", name="OK").click()

        #################### ВКЛЮЧЕНИЕ 3 КАНАЛА ДЛЯ КАЛИБРОВКИ ####################

        page.get_by_role(
            "link", name="Наблюдение").click()
        page.get_by_role(
            "link", name=" Настройка IPC").click()

        page.get_by_role(
            "row", name="10.100.100.100:9006:1  ").locator("label").first.click()
        page.get_by_role(
            "button", name="Сохранить").click()

        page.goto('http://192.168.240.1/pages/preview',
                wait_until='domcontentloaded')

        page.locator(
            "#player").get_by_text("3").dblclick()
        page.locator("#volume").click()

        #################### ВЫКЛЮЧЕНИЕ КАЛИБРОВКИ 3 КАНАЛА ####################

        keyboard.wait('alt+4')

        page.goto('http://192.168.240.1/pages/config',
                wait_until='domcontentloaded')

        page.get_by_role(
            "link", name="Тревога").click()
        page.get_by_role(
            "link", name=" AI приложение").click()
        expect(page.get_by_role(
            "listitem").filter(has_text="Алгоритм калибр")).to_be_visible()
        page.get_by_role(
            "listitem").filter(has_text="Алгоритм калибр").click()
        page.wait_for_timeout(120)

        page.get_by_role(
            "cell", name="Калибровка Side").locator("input[name=\"mode\"]").click()
        page.get_by_role(
            "link", name="Нормально").click()
        page.get_by_role(
            "button", name="Сохранить").click()

        #################### ПРОСМОТР 3 КАНАЛА + ОСТ. КАМЕРЫ ####################

        page.goto('http://192.168.240.1/pages/preview',
                wait_until='domcontentloaded')

        page.locator("#play9").click()

########################### ПРОФИЛЬ 5 КАНАЛ #######################################################

    def config_5_channel():

        page.goto('http://192.168.240.1/pages/maintenance',
                wait_until='domcontentloaded')

        expect(page.locator(
            "#maintenance_left_menu")).to_contain_text("Конфигурация")
        page.get_by_role(
            "link", name=" Конфигурация").click()
        page.wait_for_timeout(500)

        page.locator("#file_path_pc_import_param").click()

        #################### ПОДГРУЗКА ФАЙЛА ИЗ СКРЫТОГО ПРОВОДНИКА ####################

        with page.expect_file_chooser() as fc_info_5:
            page.locator(
                "#parameter div").filter(
                    has_text="Импортировать параметрыПросматриватьИмпорт").locator("span").click()

        file_config_5 = fc_info_5.value
        file_config_5.set_files(config_5_ch)

        page.locator("#parameter div").filter(
            has_text="Импортировать параметрыПросматриватьИмпорт").get_by_role("button").click()
        page.get_by_role("button", name="OK").click()

        #################### ВХОД В НАСТРОЙКИ IPC ####################

        page.goto('http://192.168.240.1/pages/config',
                wait_until='domcontentloaded')

        page.get_by_role(
            "link", name="Наблюдение").click()
        page.get_by_role(
            "link", name=" Настройка IPC").click()

        page.get_by_role(
            "button", name="По умолчанию").click()

        #################### НАСТРОЙКА И ВЫКЛ 5 CH ДЛЯ КАЛИБРОВКИ ####################

        page.get_by_role(
            "row", name="5  ").locator("label").first.click()

        page.get_by_role(
            "button", name="").nth(4).click()
        page.locator("span").filter(
            has_text="По умолчаниюDSMMDVR").locator("span").click()

        page.get_by_role(
            "link", name="DSM").click()
        page.wait_for_timeout(100)
        page.locator(
            "#edit_ip_address").fill("10.100.100.100")
        page.get_by_role(
            "button", name="OK").click()
        page.wait_for_timeout(100)

        page.get_by_role(
            "row", name="10.100.100.100:9006:1  ").locator("span").first.click()

        page.locator(
            "#ipc_start_address").fill("1")

        page.get_by_role(
            "button", name="Сохранить").click()
        page.get_by_role(
            "button", name="OK").click()
        page.wait_for_timeout(100)

        page.get_by_role(
            "row", name="3  ").locator("label").first.click()

        page.get_by_role(
            "button", name="Сохранить").click()
        page.get_by_role(
            "button", name="OK").click()
        page.wait_for_timeout(100)

        page.get_by_role(
            "row", name="3  ").locator("label").first.click()

        page.get_by_role(
            "button", name="Сохранить").click()

        page.goto('http://192.168.240.1/pages/config',
                wait_until='domcontentloaded')
        page.wait_for_timeout(100)

        #################### КАЛИБРОВКА 5 КАНАЛА ####################

        page.get_by_role(
            "link", name="Тревога").click()
        page.get_by_role(
            "link", name=" AI приложение").click()
        expect(page.get_by_role(
            "listitem").filter(has_text="Алгоритм калибр")).to_be_visible()
        page.get_by_role(
            "listitem").filter(has_text="Алгоритм калибр").click()
        page.wait_for_timeout(120)

        page.get_by_role(
            "row", name="5").locator("input[name=\"use\"]").click()
        page.locator(
            "#calibration_list").get_by_role("link", name="DMS").click()
        page.get_by_role(
            "row", name="DMS").locator("input[name=\"mode\"]").click()
        page.get_by_role(
            "link", name="Калибровка").click()
        page.get_by_role(
            "cell", name="Калибровка").locator("span").nth(3).click()
        page.get_by_role(
            "link", name="Side").click()
        page.get_by_role(
            "button", name="Сохранить").click()
        page.get_by_role("button", name="OK").click()

        #################### ВКЛЮЧЕНИЕ 5 КАНАЛА ДЛЯ КАЛИБРОВКИ ####################

        page.get_by_role(
            "link", name="Наблюдение").click()
        page.get_by_role(
            "link", name=" Настройка IPC").click()

        page.get_by_role(
            "row", name="10.100.100.100:9006:1  ").locator("label").first.click()
        page.get_by_role(
            "button", name="Сохранить").click()

        page.goto('http://192.168.240.1/pages/preview',
                wait_until='domcontentloaded')

        page.locator(
            "#player").get_by_text("5").dblclick()
        page.locator("#volume").click()

        #################### ВЫКЛЮЧЕНИЕ КАЛИБРОВКИ 5 КАНАЛА ####################

        keyboard.wait('alt+5')

        page.goto('http://192.168.240.1/pages/config',
                wait_until='domcontentloaded')

        page.get_by_role(
            "link", name="Тревога").click()
        page.get_by_role(
            "link", name=" AI приложение").click()
        expect(page.get_by_role(
            "listitem").filter(has_text="Алгоритм калибр")).to_be_visible()
        page.get_by_role(
            "listitem").filter(has_text="Алгоритм калибр").click()
        page.wait_for_timeout(120)

        page.get_by_role(
            "cell", name="Калибровка Side").locator("input[name=\"mode\"]").click()
        page.get_by_role(
            "link", name="Нормально").click()
        page.get_by_role(
            "button", name="Сохранить").click()

        #################### ПРОСМОТР 5 КАНАЛА + ОСТ. КАМЕРЫ ####################

        page.goto('http://192.168.240.1/pages/preview',
                wait_until='domcontentloaded')

        page.locator("#play9").click()

    #################### ЛОГИКА РАБОТЫ БЛОКА ####################

    while True:

        if keyboard.is_pressed('alt+4'):

            config_3_channel()
            
            while True:
                
                if keyboard.is_pressed('alt+4'):
                    continue
                break

        elif keyboard.is_pressed('alt+5'):

            config_5_channel()
            
            while True:
                
                if keyboard.is_pressed('alt+5'):
                    continue
                break

        elif keyboard.is_pressed('alt+r' or 'alt+к'):

            context.close()
            browser.close()
            exit()
            break

##################### ИНИЦИАЦИЯ ВКЛЮЧЕНИЯ КОДА ####################################################

with sync_playwright() as playwright:
    run(playwright)
