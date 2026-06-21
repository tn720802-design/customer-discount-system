def calculate_discount(total_purchase_this_year):
    """
    Tính tỷ lệ giảm giá dựa trên tổng giá trị mua hàng trong năm.
    Khách hàng thân thiết (tổng >= 50 triệu) được giảm 10%.
    """
    LOYALTY_THRESHOLD = 50_000_000
    DISCOUNT_RATE = 0.1

    if total_purchase_this_year >= LOYALTY_THRESHOLD:
        return DISCOUNT_RATE
    return 0