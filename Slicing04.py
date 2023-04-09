def main(s,n):
    """
    The s string variable is given. return n characters from the beginning.
    Args:s string o'zgaruvchisi berilgan. boshidan n ta belgini qaytaring.
        s(str): parameter
        n(int): parameter
    Returns:
        str: answer
    """
    return str(s)[:n]
print(main('abcde',2))