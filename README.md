# Premint Raffle Checker

The original repo : `https://github.com/gurdeep999/premintChecker`

## Introduction

- The script is created to check the premint raffle results.
- A template for filling in wallet addresses is provided as `mywallets.csv` (please do not change the name of the csv file)
- Improvements were made to adapt the authors’ situation
- Wallet balance will also be checked
-  **As premint is busting their ass to eliminate premint bots, this repo will stop updating itself while remaining functional, but a more advanced version of premint checker with proxy support is [here](https://github.com/websterhasnoheart/Premint_Checker_with_Proxy_Support)**
## 1. Requirement

- `Python 3.8`
- `web3.py`
- `selenium`
- `prettytable`
- `webdriver_manager`

## 2. Installation

1. Git clone `git@github.com:websterhasnoheart/premint_checker.git`
2. cd `premint_checker`
3. `py run.py`
4. input `premint link` eg : [`https://www.premint.xyz/Luskorpnft/`](https://www.premint.xyz/Luskorpnft/)

## 3. Manual

1. Fill in your wallet names and addresses in `mywallets.csv`
2. Run the script by `py run.py`
3. Fill in the premint raffle address
4. Check your raffle result

![image](https://user-images.githubusercontent.com/66870019/191744116-89fc79b2-b0d2-472b-b9a4-219de9f0a92f.png)
![image](https://user-images.githubusercontent.com/66870019/191744273-e1f4b7d8-2e95-4c5d-8bbe-c5d5ece342f5.png)

## 4. Warning

- Please do not run the program too frequent(example : 100 wallets for 3 times in 3 mins), as you might get detected and warning from premint.xyz

![image](https://user-images.githubusercontent.com/66870019/192098318-27901f57-dfaa-491e-912a-3486120de3e5.png)

