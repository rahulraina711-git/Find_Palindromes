this1 = "borroworrob"


def Palindrome_Finder(str):
    strings = []                # this list will contain all the possible combinations of the given word (the substrings).
    The_Palindrome_List = []    # this list will contain the final palindromes
    n = len(str)
    # For holding all the formed substrings
    subst = []

    # This loop maintains the starting character
    for i in range(0, n):
        # This loop will add a character to start character one by one till the end is reached
        for j in range(i, n):
            subst.append(str[i:(j + 1)])

    for i in subst:
        strings.append(i)

    for k in strings:
        if k == ''.join(reversed(k)):
            The_Palindrome_List.append(k)
    print(The_Palindrome_List)


Palindrome_Finder(this1)
