def main(s):
    """The s string variable is given. Return all characters except the one at the beginning and end.
    Args:s string o'zgaruvchisi berilgan. Boshidagi va oxiridagi belgidan tashqari barcha belgilarni qaytaring.
        s(str): parameter
    Returns:
        str: answer
    """
    return str(s).strip('*')
print(main('***a***a***'))