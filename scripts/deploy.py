from brownie import FundMe,MockV3Aggregator,config,network
from scripts.helpful_scripts import get_account,deploy_mocks,LOCAL_BLOCKCHAIN_ENVIRONMENTS





def deploy_fund_me():
 
  # firstly we deploy our contract and then we need to verfiy and publish our smartcontract in etherscan 
  #fund_me= FundMe.deploy({"from": account}, publish_source=True)

  #if we want use the presistant network like goreli, use the associated address
  # otherwise ,deploy mocks
  ##livechain 
   account = get_account()
   if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
   else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

   fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
   print(f"Contract deployed to {fund_me.address}")
   return  fund_me


    


def main():
    deploy_fund_me()
