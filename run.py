from Premint.premint import Premint

with Premint(teardown=True) as bot:
    bot.verify_wallets()
    bot.display_results()
