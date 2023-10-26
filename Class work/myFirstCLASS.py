

# class MSCDSB:

#     def __init__(self): #Member function
          
#     #data members / properties/ attributes
#          self.name = "MSC DS B"
         
#          self.students = ["A","B","C"]

#     def printStudents(self):  #Member function
#         for student in self.students:

#           print(student)

# obj = MSCDSB()
# print(obj.name)
# print(obj.students)




# class car:
#     def __init__(self,mfg,mdl,yer):
#         self.Manufacture = mfg
#         self.Model = mdl
#         self.Year = yer


# bmw = car("BMW","F Series",2020)
# print(bmw.Manufacture)

# ferari = car ("ferrari","A Series","2023")
# print(ferari.Model)



#craete a class restaurant, that accepts
#iteam and quantity as a input
#inside your class you are having the item
#and its cost (unit price) as a dictionary
# create a function calculate total cost
#that prints the itemname,qty & total cost.


# class resturant:

#     def __init__(self,itemname,qty):
#         self.itemname = itemname
#         self.qty = qty
#         self.menuitems ={
#             "RICE":30,
#             "CHICKEN":100,
#             "DAL":40,
#             "CHAPATI":15,
#         }

#     def totalcost(self):
#         print("total cost of the order")
#         print("item\t:",self.itemname)
#         print("quantity\t:",self.qty)
#         total = self.qty * self.menuitems[self.itemname]
#         print("total\t:",total)


# order = resturant("RICE",4)
# order.totalcost()




#define a class expenses tracker that stores the
#expenses and income in a dictionary
#implement the method to
# - store the transaction;
# - view transaction
# - calculate the total expense/income..

class expensetracker:
    def __init__(self):
        self.expenceDict = {
            "income": [],
            "expense": [],

        }
    def store_transactions(self,type,amt,category,date,details):

        trans = {
            "Amount":amt,
            "Category":category,
            "date":date,
            "details":details,
        }
        if type =="income":
            self.expenseDict["income"].append(trans)
        else:
            self.expenceDict["expense"].append(trans)
    def view_transaction(self):
        print("your incomr")
        for item in self.expenceDict["income"]:
            print(item)
        for item in self.expenceDict["expense"]:
            print(item)
    def calculate_transaction(self):
        total_income = 0
        for item in self.expenceDict["income"]:
            total_income += item["Amount"]
            print("total income\t:\t",total_income)
        total_expense = 0
        for item in self.expenceDict["expense"]:
            total_expense += item["Amount"]
            print("total expense\t:\t",total_expense)


