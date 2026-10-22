def count_prefix_matches(search_term, prefix):
    counts = 0

    for term in search_term :
        if term.startswith(prefix):
            counts += 1
    return counts
if __name__ == "__main__":
    terms = 'apple', 'application', 'applet', 'banana', 'appstore'
    pre = 'app'

print(count_prefix_matches(terms, pre))                     