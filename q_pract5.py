def reverse_log_words(s):
    words = s.split()
    words.reverse()

    return " ".join(words)
if __name__ == "__main__":
    log_words = " a good   exmaple  "
    print(reverse_log_words(log_words))    