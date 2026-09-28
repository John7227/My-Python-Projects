def palindrome(each):
    result = []

    for words in each:

        store = words.lower()

        reverse = store[::-1]

        if(store == reverse):
            result.append(True)
        else:
            result.append(False)

    return result

