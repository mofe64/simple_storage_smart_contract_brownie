from brownie import accounts, SimpleStorage, network, config


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_simple_storage():
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})
    print(simple_storage)
    stored_value = (
        simple_storage.retrieve()
    )  # call the retrieve function in our smart contract
    print(stored_value)
    transaction = simple_storage.store(
        100, {"from": account}
    )  # when performing a transaction we need to add who
    # we are transacting from, ie. who is initiating the transaction
    transaction.wait(1)
    updated_value = simple_storage.retrieve()
    print(updated_value)


def main():
    deploy_simple_storage()
