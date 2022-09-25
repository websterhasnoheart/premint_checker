import csv
from multiprocessing.sharedctypes import Value
import os, sys


def get_wallet_info():
    wallets = []
    with open('testing_wallets.csv') as file:
        reader = csv.DictReader(file, skipinitialspace=True)
        for line in reader:
            wallets.append(line)
    return wallets
        
        
def get_base_url():
    try:
        premint_url = input("Please enter your Premint raffle url: ").split('/')
        https, _, domain, raffle, *end = premint_url
        return f"{https}//{domain}/{raffle}"
    except ValueError:
        print("Invalid premint raffle link, please try again!")
        os.execl(sys.executable, sys.executable, *sys.argv)

    # if using regex, replace line 17 18 with the following code
    # url = re.search("^http.*[p|P]remint.xyz/.*?(?=/)", premint_url)
    # print(premint_url,url)
    # return url.group()
