import random

from vbexadc1 import Batch
from vbexadc1 import Product

class Inventory_Manager:
    def __init__(self):
        self.elem = dict()

    def add_product(self, product_name, holding_cost, stockout_penalty):
        if product_name in self.elem:
            print(f"Product {product_name} already exists.")
            return None

        self.elem[product_name] = Product(product_name, holding_cost, stockout_penalty)

    def restock_product(self, product_name, quantity, cost_per_unit):
        if product_name not in self.elem:
            print(f"Product {product_name} not found.")
            return None

        self.elem[product_name].add_batch(quantity, cost_per_unit)

    def simulate_demand(self,min_demand = 0, max_demand = 20):
        dic = dict()
        for product_name in self.elem:
            demand = random.randint(min_demand, max_demand)
            dic[product_name] = demand

        return dic

    def simulate_day(self,demand):
        stockout = 0
        holding = 0
        for product_name in self.elem:
            if product_name in demand:
                stockout+=self.elem[product_name].fulfill_demand(demand[product_name])
            holding+=self.elem[product_name].calculate_holding_cost()
        return stockout,holding

    def save_to_csv(self,filename:str):
        file = open(filename, "w")
        inv=""
        for product_name in self.elem:
            for batch in self.elem[product_name].batches:
                inv += f"{product_name},{str(batch.quantity)},{str(batch.cost_per_unit)}\n"

        file.write(inv)
        file.close()

    def load_from_csv(self,filename:str):
        try:
            file = open(filename, 'r')
        except:
            print("File doesnt exist")
            return None

        line = file.readline()
        while line != "":
            lijst = line.split(',')
            if lijst[0] not in self.elem:
                self.add_product(lijst[0], 0, 0)

            self.restock_product(lijst[0], int(lijst[1]), float(lijst[2]))
            line = file.readline()

        file.close()

    def print_inventory(self):
        print("Current Inventory:")
        body = ""
        for product_name in self.elem:
            print(f"Product {product_name}")
            print(self.elem[product_name])


    #def main(self):
         #self.add_product("PC",10,200)
         #self.add_product("GSM",5,100)
         #self.restock_product("GSM",1000,2)
         #self.restock_product("GSM",2000,3)
         #self.restock_product("PC",100,50)
         #self.restock_product("PC",10,40)
         #self.print_inventory()

        #x= self.simulate_demand(1,20)
        #print(x)
        #self.simulate_day(x)
        #self.save_to_csv("inventory.csv")

#crm = Inventory_Manager()
#crm.main()



