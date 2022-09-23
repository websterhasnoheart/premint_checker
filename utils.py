import csv

def get_wallet_info():
    wallets = []
    with open('mywallets.csv') as file:
        reader = csv.DictReader(file, skipinitialspace=True)
        for line in reader:
            wallets.append(line)
    return wallets
        


def get_base_url():
    premint_url = input("Please enter your Premint raffle url: ").split('/')

    # using destructured assignment
    https, _, domain, raffle, *end = premint_url
    return f"{https}//{domain}/{raffle}"

    # if using regex, replace line 17 18 with the following code
    # url = re.search("^http.*[p|P]remint.xyz/.*?(?=/)", premint_url)
    # print(premint_url,url)
    # return url.group()
