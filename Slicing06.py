def main(s,n):
    """
    The s string variable is given. return all characters except n characters from the beginning.
    Args:s string o'zgaruvchisi berilgan. boshidan n ta belgidan tashqari barcha belgilarni qaytaring.
        s(str): parameter
        n(int): parameter
    Returns:
        str: answer
    """
    return str(s).strip(str(s)[:n])
print(main('123456789abcdeghijklmn',5))