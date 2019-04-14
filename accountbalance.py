class AccountBalance :
    def processTransactions(self,startingBalance, transactions):
        c = []
        credit = 0
        debit = 0
        alist = list(transactions)
        for element in alist:
            c.append(element.split(' '))
        for part in c:
            if part[0] == 'C':
                credit = credit + int(part[1])
            elif part[0] == 'D':
                debit = debit + int(part[1])
            FinalBalance = startingBalance + credit - debit
        return FinalBalance
