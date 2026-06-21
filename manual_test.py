from discount import calculate_discount

def run_test_case(name, previous_total, new_order):
    total_after_order = previous_total + new_order
    discount_rate = calculate_discount(total_after_order)
    discount_amount = new_order * discount_rate
    final_price = new_order - discount_amount

    print(f"--- {name} ---")
    print(f"Tổng mua trước: {previous_total:,} VNĐ")
    print(f"Đơn hàng mới: {new_order:,} VNĐ")
    print(f"Tổng sau đơn hàng: {total_after_order:,} VNĐ")
    print(f"Tỷ lệ giảm giá: {discount_rate * 100}%")
    print(f"Số tiền được giảm: {discount_amount:,} VNĐ")
    print(f"Giá trị thanh toán cuối: {final_price:,} VNĐ")
    print()

# TC01: Tổng trước 60M, đơn mới 2M
run_test_case("TC01", 60_000_000, 2_000_000)

# TC02: Tổng trước 30M, đơn mới 2M
run_test_case("TC02", 30_000_000, 2_000_000)

# TC03: Tổng trước 49M, đơn mới 2M
run_test_case("TC03", 49_000_000, 2_000_000)