
class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = list()

    def __str__(self):
        title = f"{self.name:*^30}"
        items = ""
        total = 0
        for item in self.ledger:
            items += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + "\n"
            total += item['amount']
        output_1 = title + items + "Total: " + str(total)
        return output_1


    def get_balance (self):
        total = 0
        for x in self.ledger:
            total += x["amount"]
        return total
    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": amount, "description": description})
    def check_funds (self, amount):
        if self.get_balance() >= amount:
            return True
        return False

    def withdraw (self, amount, description = ""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False


    def transfer (self, amount, source_category):
        if self.check_funds (amount):
            self.withdraw(amount, "Transfer to " + source_category.name)
            source_category.deposit(amount, "Transfer from " + self.name)
            return True
        return False
    def totalamount(self):
      totalamount = 0
      for item in self.ledger:
        if item ["amount"] < 0:
          totalamount += item["amount"]
        return totalamount

def create_spend_chart(categories):
    #Not my code, taken from https://github.com/trsilva32
    spent_dict = {}
    for i in categories:
        s = 0
        for j in i.ledger:
            if j['amount'] < 0 :
                s+= abs(j['amount'])
        spent_dict[i.name] = round(s,2)
    total = sum(spent_dict.values())
    percent_dict = {}
    for k in spent_dict.keys():
        percent_dict[k] = int(round(spent_dict[k]/total,2)*100)
    output = 'Percentage spent by category\n'
    for i in range(100,-10,-10):
        output += f'{i}'.rjust(3) + '| '
        for percent in percent_dict.values():
            if percent >= i:
                output+= 'o  '
            else:
                output+= '   '
        output += '\n'
    output += ' '*4+'-'*(len(percent_dict.values())*3+1)
    output += '\n     '
    dict_key_list = list(percent_dict.keys())
    max_len_category = max([len(i) for i in dict_key_list])

    for i in range(max_len_category):
        for name in dict_key_list:
            if len(name)>i:
                output+= name[i] +'  '
            else:
                output+= '   '
        if i < max_len_category-1:
            output+='\n     '

    return output
