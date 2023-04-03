from brownie import FundMe,network
from scripts.helpful_scripts import get_account
from scripts.deploy import deploy_fund_me
import pytest

def test_can_fund_and_withdraw():
    account=get_account()
    fund_me= deploy_fund_me
    entrance_fee = fund_me.getEntranceFee()+100
    tx= fund_me.fund({"from":account,"value":entrance_fee})
    tx.wait(1)
    assert fund_me.addressToAmountFunded(account.address) ==entrance_fee
    tx2=fund_me.withdraw({"from":account})
    tx2.wait(1)
    assert fund_me.addressToAmountFunded(account.address) ==0

def test only_owner_can_withdraw():
  if network.show_active not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
   pytest.skip("only for local  test")
