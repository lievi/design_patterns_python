from shipping_cost import ShippingCost
from postal_strategy import PostalStrategy
from fedex_strategy import FedExStrategy

# Test Fedex shipping
strategy = FedExStrategy()
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost('order 1')
assert cost == 3.00

strategy = PostalStrategy()
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost('order 2')
assert cost == 5.00

print('All tests passed !!!')