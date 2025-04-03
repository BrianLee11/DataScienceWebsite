# services/logic.py
def add_integer(location):
    mapping = {
        'home': 0,
        'info': 1,
        'about': 2,
        'linearRegression': 3
    }
    return mapping[location] + 0
