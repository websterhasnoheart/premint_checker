from Premint.premint import Premint
import os, sys

with Premint(teardown=True) as bot:    
    wallet_count = bot.verify_wallets()
    bot.display_results()
    print("********************************** " + 
        str(wallet_count) + " Wallets checked, congrats if you won!" 
            + " **********************************")
    
    user_input = input("Continue to checking ? (Y/N): ")
    if (user_input == 'Y'):
        os.execl(sys.executable, sys.executable, *sys.argv)
    elif (user_input == 'N'):
        sys.exit('Exiting...')
    else:
        print("Invalid input, exiting..")
