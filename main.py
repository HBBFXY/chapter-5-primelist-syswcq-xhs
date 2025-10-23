def isOdd(n):
    # 先判断是否是整数（排除bool类型，因为bool是int的子类）
    if isinstance(n, int) and not isinstance(n, bool):
        # 是整数，再判断是否为奇数
        return n % 2 != 0
    # 非整数或其他情况，返回False
    return False    
