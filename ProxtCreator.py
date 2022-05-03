# import requests
from proxy_manager_g4 import ProxyManager
# from proxy_manager_g4.consts import PROTOCOL_HTTPS, PROTOCOL_HTTP
from proxy_controller import ProxyChecker
from os import system

freeproxycreator = """               
Created by: ! Kontragerilla ღ ヅ#1019 Ver: 1.0
"""
CREATE_LIST = False


def file_writer(prxy: dict) -> None:
    from os import listdir
    global CREATE_LIST

    if "for_API.txt" not in listdir():
        f = open("for_API.txt", "w")
        f.write(f"{prxy}\n")
        f.close()
    else:
        with open("for_API.txt", "a+") as fileObj:
            proxtInFile = fileObj.readlines()
            if prxy not in proxtInFile:
                fileObj.write(f"{prxy}\n")
    if CREATE_LIST:
        if "proxy_list.txt" not in listdir():
            f = open("proxy_list.txt", "w")
            f.write(f"{prxy['proxy']}\n")
            f.close()
        else:
            with open("proxy_list.txt", "a+") as fileObj:
                proxtInFile = fileObj.readlines()
                if prxy not in proxtInFile:
                    fileObj.write(f"{prxy['proxy']}\n")


def create_proxys(amonunt: int, PROXY_MANAGER) -> None:
    """
    :param PROXY_MANAGER
    :param amonunt:  this number of ip addresses will be generated
    :return: None
    """

    while amonunt > 0:
        try:
            CHECKER = ProxyChecker()
            proxy = PROXY_MANAGER.get_random()
            # last_proxy = {http_s: f"{http_s}://username:password@{proxy}"}
            last_proxy = CHECKER.check_proxy(str(proxy))
            if last_proxy.get('status'):
                try:
                    system("color a")
                    print("--------------------------------------------")
                    print(f"[+] {proxy} created.")
                    print("    Country:" + last_proxy.get('country'))
                    print("    city:" + last_proxy.get('city'))
                    print("    Time response:" + last_proxy.get('time_response'))
                    print("    anonymity:" + last_proxy.get('anonymity'))
                    print("--------------------------------------------")

                    file_writer(last_proxy)
                    amonunt -= 1
                except:
                    ...

            else:
                system('color 4')
                print(f"[-] {proxy} Failed.")

        except Exception as err:
            system('color 4')
            print(f"[-] {str(proxy)} err: {err}")
            pass
    system('color a')
    print("[+] all proxies are sucsesfuly created")


def proxy_settings(amonunt: int, anonymity: bool = True) -> None:
    """
    :param anonymity: Your ip addresse will be anonymous or not to be
    :return: None
    """

    try:
        proxy_manager = ProxyManager(anonymity=anonymity)
        create_proxys(amonunt, proxy_manager)

    except BaseException as err:
        system('color 4')
        print(f"[-] err: {err} ")


def main():
    """
    Main menu
    :return:
    """
    system('color 6')
    print(freeproxycreator)
    while True:
        try:
            global CREATE_LIST
            system('color 6')
            amonut = int(input("[+] How much proxies do you want create?  : "))
            while True:
                create_list = input('[+] Do you want create proxy_list(y/n)(recommended): ').lower()
                if create_list == 'n':
                    CREATE_LIST = False
                    break
                if create_list == 'y':
                    CREATE_LIST = True
                    break
                else:
                    continue
            proxy_settings(amonut, anonymity=True)

        except TypeError:
            system('color 4')
            print("[-] Please enter a Number")
            continue


if __name__ == '__main__':
    main()
