def main(s,n):
    """
    The s string variable is given. return all characters except n characters at the end.
    Args:s string o'zgaruvchisi berilgan. oxirida n ta belgidan tashqari barcha belgilarni qaytaring.
        s(str): parameter
        n(int): parameter
    Returns:
        str: answer
    """
    return str(s).strip(str(s)[-n:])
print(main('1234567890hjbcbsjhv',5))