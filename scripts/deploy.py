from brownie import accounts, config

def deploy_simpleStorage():
    #local rpc account
    #account = accounts[0]
    
    #live account
    account = accounts.add(config['wallets']['dev_account_1']['private_key'])
    print(account)

def main():
    deploy_simpleStorage()