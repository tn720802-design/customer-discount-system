def calculate_discount(previous_total_purchase):
    """
    PHIÊN BẢN CÓ BUG: chỉ kiểm tra tổng mua trước đó,
    KHÔNG cộng dồn đơn hàng hiện tại vào tổng.
    """
    LOYALTY_THRESHOLD = 50_000_000
    DISCOUNT_RATE = 0.1

    if previous_total_purchase >= LOYALTY_THRESHOLD:
        return DISCOUNT_RATE
    return 0