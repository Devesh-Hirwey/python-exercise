"""

    You are given a string str, you need to return True if  the words "cat" and "hat"
    appear same number of times in str, otherwise return False.


    Note: str contains only lowercase English alphabets.

"""


def cat_hat(str):
    return str.count('cat') == str.count('hat')

    """
    
    
    This function, cat_hat, checks if the number of times the substring "cat" appears in
    a string is equal to the number of times the substring "hat" appears.

        Here's how it works:

    str.count('cat'): This part of the code counts the number of times the substring "cat"
    appears within the input string str.
    
    str.count('hat'): This counts the number of times the substring "hat"
    appears within the input string str.
    
    ==: This is a comparison operator that checks if the values on either side are equal.
    So, the function essentially returns True if the count of "cat" is equal to the count of "hat"
    in the given string, and False otherwise.
    
    
    """
