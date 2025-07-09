def calculate_total(products, discount=0):
    total = 0
    for product in products:
        total += product['price']
    return total - (total * discount / 100)

def test_calculate_total_with_empty_list():
    print("Testing with an empty list")
    assert calculate_total([]) == 0
    print("Empty list test passed")

def test_calculate_total_with_single_product():
    print("Testing with a single product")
    products = [
        {'name': 'apple', 'price': 5}
    ]
    assert calculate_total(products, discount=5) == 4.75
    print("Single product test passed")

def test_calculate_total_with_multiple_products():
    print("Testing with multiple products")
    products = [
        {'name': 'apple', 'price': 5},
        {'name': 'banana', 'price': 3},
        {'name': 'cherry', 'price': 2}
    ]
    assert calculate_total(products, discount=10) == 9
    print("Multiple products test passed")

if __name__ == "__main__":
    test_calculate_total_with_empty_list()
    test_calculate_total_with_single_product()
    test_calculate_total_with_multiple_products()
    print("All tests passed!")