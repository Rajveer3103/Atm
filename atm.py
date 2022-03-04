class Atm: 
    def __init__(self, colour, width, height, bankname):
        self.colour= colour
        self.width= width
        self.height= height
        self.bankname= bankname

    def Withdraw(self):
        print("Withdrawing Money")
    def Balance(self):
        print("Checking Balance")
    def Pin(self):
        print("Enter Pin")

atm1= Atm("Silver",50,20,"SBI")
atm1.Pin()
atm1.Balance()
atm1.Withdraw()
        

 