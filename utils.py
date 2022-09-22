import csv


def get_wallets():
    wallets = []
    with open('mywallets.csv') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            # as there is only 1 element every row we can just append the element directly as append row would just make a nested wallets list
            wallets.append(row[0])
    return wallets

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

    # using regex
    # url = re.search("^http.*[p|P]remint.xyz/.*?(?=/)", premint_url)
    # print(premint_url,url)
    # return url.group()
