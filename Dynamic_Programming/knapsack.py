import collections

Item = collections.namedtuple('Item', ['weight', 'value'])


def max_value(knapsack_max_weight, items):
    """
    Get the maximum value of the knapsack.
    """
    sorted_items = sorted(items)
    weight_dict = dict()
    for weight, _ in sorted_items:
        weight_dict[weight] = 0
    for weight, value in sorted_items:
        if knapsack_max_weight - weight >= 0:
            knapsack_max_weight -= weight
            for w in weight_dict:
                weight_dict[w] += value
    return max(weight_dict.items(), key=lambda x: x[1])[1]


tests = [
    {
        'correct_output': 14,
        'input':
            {
                'knapsack_max_weight': 15,
                'items': [Item(10, 7), Item(9, 8), Item(5, 6)]}},
    {
        'correct_output': 13,
        'input':
            {
                'knapsack_max_weight': 25,
                'items': [Item(10, 2), Item(29, 10), Item(5, 7), Item(5, 3), Item(5, 1), Item(24, 12)]}}]
for test in tests:
    assert test['correct_output'] == max_value(**test['input'])
