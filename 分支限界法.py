class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

def knapsack_branch_and_bound(items, capacity):
    def bound(node, n, current_weight, current_value):
        if current_weight >= capacity:
            return 0
        bound_value = current_value
        j = node + 1
        total_weight = current_weight
        while j < n and total_weight + items[j].weight <= capacity:
            total_weight += items[j].weight
            bound_value += items[j].value
            j += 1
        if j < n:
            bound_value += (capacity - total_weight) * (items[j].value / items[j].weight)
        return bound_value

    def branch_and_bound(node, n, current_weight, current_value):
        nonlocal max_value
        if current_weight <= capacity and current_value > max_value:
            max_value = current_value

        if node >= n or current_weight >= capacity or bound(node, n, current_weight, current_value) <= max_value:
            return
        branch_and_bound(node + 1, n, current_weight, current_value)
        branch_and_bound(node + 1, n, current_weight + items[node].weight, current_value + items[node].value)

    n = len(items)
    max_value = 0
    branch_and_bound(-1, n, 0, 0)
    return max_value

items = [Item(3, 66), Item(2, 40), Item(5, 95), Item(4, 40)]
capacity = 9
max_value = knapsack_branch_and_bound(items, capacity)
print("Maximum value (Branch and Bound):", max_value)
