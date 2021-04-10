# blockchain 

'''
List of things needed for cryptocurrency:

Blockchain

Blocks

Transactions
'''
'''
  Block class
  
    instance variables:
      prevHash
      Transaction
      time stamp
      
    methods:
'''
'''
  Transaction class
    instance variables:
      sender
      receiver
      amount
      time stamp
      hash of block

    methods:
      user input
      calculate the hash
      checks if the transaction is between two valid users with valid blocks
      
'''
import hashlib
import json

class Blockchain():
    def __init__(self):
        self.chain = []
        self.pendingTransactions = []
        self.blockCount = 0
        self.transactionCount = 0
    
    def addTransaction(self, sender, receiver, amount):
        self.pendingTransactions.append(Transaction(sender, receiver, amount))
        self.transactionCount += 1

        if self.transactionCount % 3 == 0:
            self.addBlock()
            #self.pendingTransactions.clear()
            #self.transactionCount = 0
        
    def addBlock(self):
        if self.blockCount == 0:
            genesisBlock = Block("0", self.pendingTransactions[0:self.transactionCount], self.blockCount)
            self.chain.append(genesisBlock)
            print(self.displayOneBlock())
            self.blockCount += 1
        else:
            newBlock = Block(self.getPrevBlockHash(), self.pendingTransactions[self.transactionCount-3:], self.blockCount)
            self.chain.append(newBlock)
            print(self.displayOneBlock())
            self.blockCount += 1

    def getPrevBlockHash(self):
        return self.chain[-1].hash

    def displayOneBlock(self):
        block = self.chain[-1]
        string = f"Block #{block.index}\n"
        string += f"\tPrevious Block Hash: {block.prevHash}\n"
        string += f"\tCurrent Block Hash: {block.hash}\n" 

        #transactionJSON = []
        for transaction in block.transactions:
            # temp = {
            #     "sender": transaction.sender
            # }
            # transactionJSON.append(temp)
            string += f"\t\tTransaction ID: {transaction.hash}\n"
            string += f"\t\t\tSender: {transaction.sender}\n"
            string += f"\t\t\tReceiver: {transaction.receiver}\n"
            string += f"\t\t\tAmount: {transaction.amount}\n"

        #string += transactionJSON
        return string

    def display(self):
        if self.blockCount >= 1:
            blockArr = []

            for block in self.chain:
                blockJSON = {
                    "prevHash": block.prevHash,
                    "hash": block.hash,

                }
                
                transactionJSON = []
                for transaction in block.transactions:
                    temp = {
                        "sender": transaction.sender
                    }
                    transactionJSON.append(temp)
                    
                blockJSON["transactions"] = transactionJSON

                blockArr.append(blockJSON)
            return blockArr
        else:
            for transaction in self.pendingTransactions:
                print(transaction)



class Block():
    def __init__(self, prevHash, transactions, index):
        self.prevHash = prevHash
        self.transactions = transactions
        self.time = 100
        self.index = index
        self.hash = self.calculateHash()

    def calculateHash(self):
        transactionString = list(map(str, self.transactions))
        hashString = self.prevHash + ("").join(transactionString) + str(self.index) + str(self.time)
        #return hashlib.sha256(hashString.encode().hexdigest())
        return hashlib.sha256(json.dumps(hashString).encode('utf-8')).hexdigest()

class Transaction():
    def __init__(self, sender, receiver, amount):
        self.sender = sender 
        self.receiver= receiver
        self.amount = amount
        self.time = 100
        self.hash = self.calculateHash()

    def calculateHash(self):
        hashString = self.sender + self.receiver + str(self.amount) + str(self.time)
        #return hashlib.sha256(hashString.encode('utf-8').hexdigest())
        return hashlib.sha256(json.dumps(hashString).encode('utf-8')).hexdigest()
    
    def __str__(self):
       return f"Transaction ID: {self.hash}\nSender: {self.sender}\nReciever: {self.receiver}\nAmount: {self.amount}"

    

if __name__ == "__main__":
    reefies = Blockchain()
    reefies.addTransaction("areef", "bae", 20)
    reefies.addTransaction("areef", "vorfous", 30)
    reefies.addTransaction("asd", "bafe", 20)
    reefies.addTransaction("areef", "voroasus", 30)
    reefies.addTransaction("areef", "bae", 20)
    reefies.addTransaction("dfg", "vodfrous", 30)
    reefies.addTransaction("arefef", "bae", 20)
    reefies.addTransaction("ardeef", "vorous", 30)
    reefies.addTransaction("ardfeef", "bdfsae", 20)
    reefies.addTransaction("areef", "vorous", 30)
    reefies.addTransaction("argfdeef", "bae", 20)
    reefies.addTransaction("areef", "vorous", 30)
    reefies.addTransaction("aresdfef", "bae", 20)
    reefies.addTransaction("aresdfef", "vorous", 30)
    reefies.addTransaction("areef", "basdfe", 20)
    reefies.addTransaction("asdfreef", "vorous", 30)
    #print(reefies.display())