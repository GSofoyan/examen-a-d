class Batch:
    def __init__(self, quantity: int, cost_per_unit: float):
        self.quantity = quantity
        self.cost_per_unit = cost_per_unit

    def __str__(self):
        return f'Batch(quantity={self.quantity}, cost_per_unit={self.cost_per_unit})'

class Product:

    def __init__(self, product_name : str, holding_cost : float, stockout_penalty: float):
        self.product_name = product_name
        self.holding_cost = holding_cost
        self.stockout_penalty = stockout_penalty
        self.batches = []

    def add_batch(self, quantity, cost_per_unit):
        self.batches.append(Batch(quantity, cost_per_unit))

    def fulfill_demand(self, demand):

        while len(self.batches) > 0:

            if self.batches[-1].quantity <= demand:
                demand -= self.batches[-1].quantity
                self.batches.pop()
                if demand == 0:
                    return 0
            else:
                self.batches[-1].quantity -= demand
                return 0
        return demand * self.stockout_penalty

    def calculate_holding_cost(self):
        aantal_prod = 0
        for batch in self.batches:
            aantal_prod += batch.quantity

        return aantal_prod * self.holding_cost
    def __str__(self):
        string = ""
        for batch in self.batches:
            string += f"Batch(quantity={batch.quantity}, cost_per_unit={batch.cost_per_unit})\n"

        return string


