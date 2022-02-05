from brownie import accounts, config, SimpleStorage

def deploy_simple_storage():
    #local network account
    account = accounts[0]
    
    #live network account
    # account = accounts.add(config['wallets']['dev_account_1']['private_key'])

    simple_storage = SimpleStorage.deploy({'from': account})
    stored_value = simple_storage.retrieve()
    print(stored_value)
    simple_storage.store(452, {'from': account}).wait(1)
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)

def main():
    deploy_simple_storage()