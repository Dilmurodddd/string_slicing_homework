def main(s,n,k):
    """
    The s string variable is given. return from index n to index k.
    Args:s string o'zgaruvchisi berilgan. n indeksidan k indeksiga qaytish.
        s(str): parameter
        n(int): parameter
        k(int): parameter
    Returns:
        str: answer
    """
    return str(s)[n:k]
print(main('axasasasxs',0,6))