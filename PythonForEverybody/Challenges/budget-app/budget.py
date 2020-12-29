class Category:
    def __init__(self, name):
        # initialise ledger and name
        self.name = name
        self.ledger = list()

    def deposit(self, amount, description=""):
        # using dictionary to append in ledger
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        # check if there are enough funds
        total = self.check_funds(amount)

        if total:
            # apply the same rule from deposit
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        fund = 0
        n = len(self.ledger)
        for i in range(n):
            # sum all the funds in the ledger
            fund = fund + self.ledger[i]["amount"]
        return fund

    def transfer(self, amount, object_name):
        # withdraw the money
        success = self.withdraw(amount, f"Transfer to {object_name.name}")
        # deposit the money
        object_name.deposit(amount, f"Transfer from {self.name}")
        # check if the withdraw method returned True -> the transfer was successful
        if success:
            return True
        return False

    def check_funds(self, amount):
        # get the funds
        fund = self.get_balance()
        # verify if there are more funds than the requested amount
        if fund < amount:
            return False
        return True

    def __str__(self):
        # title with 30 chars, centered category name between *
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for i in range(len(self.ledger)):
            # get the description with max 23 chars and amount with max 7 chars, double precision float
            items += f"{self.ledger[i]['description'][0:23]:23}{self.ledger[i]['amount']:>7.2f}\n"
            # calculate the total
            total += self.ledger[i]['amount']

        # the output final form
        output = title + items + "Total: " + str(total)
        return output

    def get_withdrawals(self):
        total = 0
        # calculate the total as above
        for i in range(len(self.ledger)):
            if self.ledger[i]['amount'] < 0:
                total += self.ledger[i]['amount']
        return total

def create_spend_chart(categories):
    # set the title
    chart = "Percentage spent by category\n"

    # using map to create percentages
    total = 0
    breakdown = []
    for category in categories:
        total += category.get_withdrawals()
        breakdown.append(category.get_withdrawals())

    totals = list(map(lambda x: int(x / total * 10) / 10, breakdown))

    for i in range(100, -1, -10):
        cat_spaces = " "
        for total in totals:
            # for each category, insert the percentage into chart or blank
            if total * 100 >= i:
                cat_spaces += "o  "
            else:
                cat_spaces += "   "
        # insert the percentage numbers
        chart += str(i).rjust(3) + "|" + cat_spaces + "\n"

    # insert the dashes
    dashes = "-" + "---" * len(categories)
    names = []
    x_axis = ""
    for category in categories:
        # append the categories to a list
        names.append(category.name)

    # get the maximum category name length
    maxi = max(names, key=len)

    # loop throw the maximum length
    for x in range(len(maxi)):
        nameStr = '     '
        # get each letter and insert it correctly
        for name in names:
            if x >= len(name):
                nameStr += "   "
            else:
                nameStr += name[x] + "  "
        # avoid newline at the end
        if x != len(maxi) - 1:
            nameStr += '\n'
        x_axis += nameStr

    # the output final form
    chart += dashes.rjust(len(dashes) + 4) + "\n" + x_axis
    return chart
