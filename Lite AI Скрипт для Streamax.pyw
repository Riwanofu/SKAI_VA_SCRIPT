########################### STREAMAX SCRIPT #######################################################

################ ИМПОРТ БИБЛИОТЕК ДЛЯ РАБОТЫ СКРИПТА ############

import keyboard
import re
from playwright.sync_api import Playwright, sync_playwright

################## ПЕРЕМЕННАЯ ДЛЯ ИНИЦИАЛИЗАЦИИ #################

def run(playwright: Playwright):

###################################################################################################
########################## ВЫБОР ПУТЕЙ ФАЙЛОВ #####################################################
###################################################################################################

    c29n = 'C:\\скрипт\\ST_C29N V3.3.28_RC24031970'
    m1n = 'C:\скрипт\HY_X1N_AI_M0010_V3.5.8 2-3819731810665889796.20_r25032404'
    adplus = 'C:\\скрипт\\ADPLUS2.0_V3.5.8.9_T240426.71_M0010'
    config_ch = 'C:\\скрипт\\config'

###################################################################################################
###################################################################################################
###################################################################################################

    browser = playwright.chromium.launch(
        args=['--start-maximized'], headless=False)
    context = browser.new_context(no_viewport=True)
    page = context.new_page()

    def main_menu():

        page.goto("http://192.168.240.1",
            wait_until='domcontentloaded')
        page.wait_for_timeout(100)
        
        page.locator("div").filter(
            has_text=re.compile(r"^Обслуживание$")).click()
        page.wait_for_timeout(100)
        page.locator("iframe").content_frame.get_by_role(
            "link", name=" Конфигурация").click()
        pass
        
    def pass_anything():
        pass

############################ НАЧАЛЬНЫЙ ЭКРАН ######################################################

    page.goto("http://192.168.240.1/login",
            wait_until='domcontentloaded')
    page.wait_for_timeout(150)

    page.locator("span").filter(
        has_text="中文（简体）EnglishPortuguêsEspañol").click()
    page.get_by_role("link", name="Русский").click()
    page.wait_for_timeout(10)

    page.locator("#username").fill("admin")
    page.locator("#password").fill("admin")
    page.wait_for_timeout(10)

    page.locator("#password").press("Enter")
    page.wait_for_timeout(150)

    page.goto("http://192.168.240.1/pages/preview",
            wait_until='domcontentloaded')

############################ ОБНОВЛЕНИЕ КАМЕРЫ C29N ###############################################

    #################### ВЫБОР ПРОШИВКИ C29N ####################

    def c29n_upgrade():

        page.goto('http://192.168.240.1/pages/maintenance',
            wait_until='domcontentloaded')
        page.wait_for_timeout(100)

        page.get_by_role("link", name=" Обновить").click()
        page.wait_for_timeout(480)

        #################### ПОДГРУЗКА ФАЙЛА ИЗ СКРЫТОГО ПРОВОДНИКА ####################

        page.locator("#file_path_IPC_UPGRADE").click()
        with page.expect_file_chooser() as fc_info_c29n:
            page.locator("#upgrade div").filter(
                has_text="Обновление IPCПросматриватьОбновить").locator("span").click()

        file_с29n = fc_info_c29n.value
        file_с29n.set_files(c29n)
        page.wait_for_timeout(25)

        page.locator("#upgrade div").filter(
            has_text="Обновление IPCПросматриватьОбновить").get_by_role("button").click()
        page.get_by_role(
            "cell", name="Все").locator("label").click()
        page.locator(
            "#edit_ipc_dialog_modal").get_by_role("button", name="Обновить").click()
        page.get_by_role("button", name=" Ok").click()

    #################### ЛОГИКА РАБОТЫ БЛОКА ####################

    while True:

        if keyboard.is_pressed('alt+1'):

            c29n_upgrade()
            
            while True:
                
                if keyboard.is_pressed('alt+1'):
                    continue
                break

        elif keyboard.is_pressed('alt+q' or 'alt+й'):

            pass_anything()
            break

        elif keyboard.is_pressed('alt+a' or 'alt+ф'):

            main_menu()

            while True:
                
                if keyboard.is_pressed('alt+a' or 'alt+ф'):
                    continue
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
        page.wait_for_timeout(100)

        page.get_by_role("link", name=" Обновить").click()
        page.wait_for_timeout(480)

        #################### ПОДГРУЗКА ФАЙЛА ИЗ СКРЫТОГО ПРОВОДНИКА ####################

        with page.expect_file_chooser() as fc_info_terminal:
            page.locator("#upgrade div").filter(
                has_text="Обновление устройстваПросматриватьОбновить").locator("span").click()

        file_terminal = fc_info_terminal.value
        file_terminal.set_files(m1n)
        page.wait_for_timeout(25)

        page.locator("#upgrade div").filter(
            has_text="Обновление устройстваПросматриватьОбновить").get_by_role("button").click()
        page.get_by_role("button", name=" Ok").click()

    #################### ВЫБОР ПРОШИВКИ ADPLUS ##################

    def adplus_upgrade():

        page.goto('http://192.168.240.1/pages/maintenance',
            wait_until='domcontentloaded')
        page.wait_for_timeout(100)

        page.get_by_role("link", name=" Обновить").click()
        page.wait_for_timeout(480)

        #################### ПОДГРУЗКА ФАЙЛА ИЗ СКРЫТОГО ПРОВОДНИКА ####################

        with page.expect_file_chooser() as fc_info_terminal:
            page.locator("#upgrade div").filter(
                has_text="Обновление устройстваПросматриватьОбновить").locator("span").click()

        file_terminal = fc_info_terminal.value
        file_terminal.set_files(adplus)
        page.wait_for_timeout(25)

        page.locator("#upgrade div").filter(
            has_text="Обновление устройстваПросматриватьОбновить").get_by_role("button").click()
        page.get_by_role("button", name=" Ok").click()

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

            pass_anything()
            break

        elif keyboard.is_pressed('alt+a' or 'alt+ф'):

            main_menu()

            while True:
                
                if keyboard.is_pressed('alt+a' or 'alt+ф'):
                    continue
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
        page.wait_for_timeout(100)

        page.get_by_role(
            "link", name=" Конфигурация").click()
        page.wait_for_timeout(480)

        #################### ПОДГРУЗКА ФАЙЛА ИЗ СКРЫТОГО ПРОВОДНИКА ####################

        with page.expect_file_chooser() as fc_info_3:
            page.locator("#parameter div").filter(
                has_text="Импорт параметров DMSПросматриватьИмпорт").locator("span").click()

        file_config_3 = fc_info_3.value
        file_config_3.set_files(config_ch)
        page.wait_for_timeout(25)

        page.locator("#parameter div").filter(
            has_text="Импорт параметров DMSПросматриватьИмпорт").get_by_role("button").click()
        page.get_by_role("button", name="OK").click()

        with page.expect_file_chooser() as fc_info_3:
            page.locator("#parameter div").filter(
                has_text="Импортировать параметрыПросматриватьИмпорт").locator("span").click()

        file_config_3 = fc_info_3.value
        file_config_3.set_files(config_ch)
        page.wait_for_timeout(25)

        page.locator("#parameter div").filter(
            has_text="Импортировать параметрыПросматриватьИмпорт").get_by_role("button").click()
        page.get_by_role("button", name="OK").click()

        page.goto('http://192.168.240.1/pages/preview',
                wait_until='domcontentloaded')
        page.wait_for_timeout(100)

        page.locator("#volume").click()

########################### ПРОФИЛЬ 5 КАНАЛ #######################################################

    def config_5_channel():

        page.goto('http://192.168.240.1/pages/maintenance',
                wait_until='domcontentloaded')
        page.wait_for_timeout(100)

        page.get_by_role(
            "link", name=" Конфигурация").click()
        page.wait_for_timeout(480)

        #################### ПОДГРУЗКА ФАЙЛА ИЗ СКРЫТОГО ПРОВОДНИКА ####################

        with page.expect_file_chooser() as fc_info_5:
            page.locator("#parameter div").filter(
                has_text="Импорт параметров DMSПросматриватьИмпорт").locator("span").click()

        file_config_5 = fc_info_5.value
        file_config_5.set_files(config_ch)
        page.wait_for_timeout(25)

        page.locator("#parameter div").filter(
            has_text="Импорт параметров DMSПросматриватьИмпорт").get_by_role("button").click()
        page.get_by_role("button", name="OK").click()

        with page.expect_file_chooser() as fc_info_5:
            page.locator("#parameter div").filter(
                has_text="Импортировать параметрыПросматриватьИмпорт").locator("span").click()

        file_config_5 = fc_info_5.value
        file_config_5.set_files(config_ch)
        page.wait_for_timeout(25)

        page.locator("#parameter div").filter(
            has_text="Импортировать параметрыПросматриватьИмпорт").get_by_role("button").click()
        page.get_by_role("button", name="OK").click()

        page.goto('http://192.168.240.1/pages/preview',
                wait_until='domcontentloaded')
        page.wait_for_timeout(100)

        page.locator("#volume").click()

########################### ПРОФИЛЬ 6 КАНАЛ #######################################################

    def config_6_channel():

        page.goto('http://192.168.240.1/pages/maintenance',
                wait_until='domcontentloaded')
        page.wait_for_timeout(100)

        page.get_by_role(
            "link", name=" Конфигурация").click()
        page.wait_for_timeout(480)

        #################### ПОДГРУЗКА ФАЙЛА ИЗ СКРЫТОГО ПРОВОДНИКА ####################

        with page.expect_file_chooser() as fc_info_6:
            page.locator("#parameter div").filter(
                has_text="Импорт параметров DMSПросматриватьИмпорт").locator("span").click()

        file_config_6 = fc_info_6.value
        file_config_6.set_files(config_ch)
        page.wait_for_timeout(25)

        page.locator("#parameter div").filter(
            has_text="Импорт параметров DMSПросматриватьИмпорт").get_by_role("button").click()
        page.get_by_role("button", name="OK").click()

        with page.expect_file_chooser() as fc_info_6:
            page.locator("#parameter div").filter(
                has_text="Импортировать параметрыПросматриватьИмпорт").locator("span").click()

        file_config_6 = fc_info_6.value
        file_config_6.set_files(config_ch)
        page.wait_for_timeout(25)

        page.locator("#parameter div").filter(
            has_text="Импортировать параметрыПросматриватьИмпорт").get_by_role("button").click()
        page.get_by_role("button", name="OK").click()

        page.goto('http://192.168.240.1/pages/preview',
                wait_until='domcontentloaded')
        page.wait_for_timeout(100)

        page.locator("#volume").click()
    
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

        elif keyboard.is_pressed('alt+6'):

            config_6_channel()
            
            while True:
                
                if keyboard.is_pressed('alt+6'):
                    continue
                break

        elif keyboard.is_pressed('alt+a' or 'alt+ф'):

            main_menu()

            while True:
                
                if keyboard.is_pressed('alt+a' or 'alt+ф'):
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