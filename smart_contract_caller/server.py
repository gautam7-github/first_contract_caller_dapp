import web3
from flask import Flask, render_template

from config import INFURA_ID

app = Flask(__name__)


# using testnet
w3 = web3.Web3(web3.HTTPProvider(
    f"https://ropsten.infura.io/v3/{INFURA_ID}"))
con = None


@app.before_first_request
def preProcess():
    global con
    # for writing to contract
    # dangerous code - can result in my bankruptcy
    # acct = w3.eth.account.privateKeyToAccount(PVT_KEY)
    # nonce = w3.eth.get_transaction_count(acct.address)

    # public info. - not dangerous
    add = "0x8cA4e451903E4DBb3df6EEeE34a02B0aca81edDC"
    abi = '[{"inputs":[],"name":"get","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"data","type":"uint256"}],"name":"set","outputs":[],"stateMutability":"nonpayable","type":"function"}]'
    con = w3.eth.contract(address=add, abi=abi)


@app.route("/")
def index():
    val = con.functions.get().call()
    print(val)
    return render_template("index.html", currVal=val)


if __name__ == "__main__":
    app.run(debug=True)
