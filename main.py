import os
from colorama import Fore
import random
import string
import json
import requests


os.system("cls")

print(f"{Fore.WHITE}[ {Fore.CYAN}§ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Discord Invite Generator + Checker made by {Fore.WHITE}LnX{Fore.LIGHTBLACK_EX} | Licensed under {Fore.WHITE}MIT {Fore.LIGHTBLACK_EX}License")
print(f"{Fore.WHITE}[ {Fore.CYAN}§ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}You can follow me on Github: {Fore.WHITE}https://github.com/lnxcz")
auto = input(f"\n{Fore.WHITE}[ {Fore.YELLOW}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Auto scrape proxies {Fore.WHITE}(yes/no){Fore.LIGHTBLACK_EX}: {Fore.WHITE}")
amount = int(input(f"\n{Fore.WHITE}[ {Fore.YELLOW}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX}How much invites will be generated: {Fore.WHITE}"))

def scrape():
    f = open("proxies.txt", "a+")
    f.truncate(0)
    r = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1800&ssl=yes')
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        f.write((p)+"\n")
    f.close()


if auto == "yes":
    scrape()



print(f"\n{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Generating {Fore.WHITE}{amount}{Fore.LIGHTBLACK_EX} invites!")

fulla = amount


p = open(f"proxies.txt", encoding="UTF-8")


rproxy = p.read().split('\n')

while amount > 0:
    f = open(f"invites.txt","a", encoding="UTF-8")
    if not rproxy[0]:
        print(f"{Fore.WHITE}[ {Fore.RED}! {Fore.WHITE}] {Fore.LIGHTBLACK_EX}All proxies are invalid!{Fore.WHITE}")
        exit()
    proxi = random.choice(rproxy)
    proxies = {
        "https": proxi
    }
    amount = amount - 1
    code = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(6)])
    try:
        url = requests.get(f"https://canary.discord.com/api/v6/invite/{code}?with_counts=true", proxies=proxies, timeout=3)
        if url.status_code == 200:
            jurl = url.json()
            ginfo = jurl["guild"]
            gname = ginfo["name"]
            members = jurl["approximate_member_count"]
            print(f"{Fore.WHITE}[ {Fore.GREEN}+ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Working Invite {Fore.WHITE}{code}{Fore.LIGHTBLACK_EX} | Name {Fore.WHITE}{gname}{Fore.LIGHTBLACK_EX} | {Fore.WHITE}{members}{Fore.LIGHTBLACK_EX} members")
            f.write(f"\ndiscord.gg/{code}     |     {members}     |     {gname}")
            f.close()
        elif url.status_code == 404:
            fulla = fulla - 1
            print(f"{Fore.WHITE}[ {Fore.RED}- {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Invalid Invite {Fore.WHITE}{code}")
        elif url.status_code == 429:
            fulla = fulla - 1
            print(f"{Fore.WHITE}[ {Fore.RED}- {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Proxy {Fore.WHITE}{proxi} is ratelimited")
            index = rproxy.index(proxi)
            del rproxy[index]
        else:
            fulla = fulla - 1
            print(f"{Fore.WHITE}[ {Fore.RED}! {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Invalid Error! | Status code {Fore.WHITE}{url.status_code}")
    except:
        index = rproxy.index(proxi)
        del rproxy[index]
        pw = open(f"proxies.txt","w", encoding="UTF-8")
        for i in rproxy:
            pw.write(i + "\n")
        pw.close()
        fulla = fulla - 1
        print(f"{Fore.WHITE}[ {Fore.RED}- {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Failed connecting to proxy {Fore.WHITE}{proxi}{Fore.LIGHTBLACK_EX} | Removing from list!")
        pass

print(f"{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Succefully generated {Fore.WHITE}{fulla} {Fore.LIGHTBLACK_EX}working invites!{Fore.WHITE}")
