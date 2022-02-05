from brownie import accounts, SimpleStorage

def test_deploy():
    #Arrange
    account = accounts[0]
    #Act
    simple_storage = SimpleStorage.deploy({'from': account})
    inital_stored_value = simple_storage.retrieve()
    expected = 0
    #Assert
    assert inital_stored_value == expected

def test_updating_storage():
    #Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({'from': account})
    #Act
    expected = 21
    simple_storage.store(expected, {'from': account}).wait(1)
    #Assert
    assert expected == simple_storage.retrieve()