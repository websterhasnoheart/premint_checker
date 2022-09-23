from Premint.premint import Premint
import os, sys

with Premint(teardown=True) as bot:    
    bot.verify_wallets()
    bot.display_results()
    
    print("Raffle checking completed, congrats if you won! ")
    user_input = input("Continue to checking ? (Y/N): ")
    if (user_input == 'Y'):
        os.execl(sys.executable, sys.executable, *sys.argv)
    elif (user_input == 'N'):
        sys.exit('Exiting...')
    else:
        print("Invalid input, exiting..")
