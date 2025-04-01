import re


def ignore_word(word, ignore_list):
    if word in ignore_list:
        return True
    if any(char.isdigit() for char in word):
        return True
    if re.match(
        r"((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*",
        word,
    ):
        return True
    if re.search(r"[^\w\s.,!?-]", word) or len(word) == 1 or word == "":
        return True
    return False


def check_word(word, acceptable_list, ignore_list):
    word = word.lower()
    word = word.rstrip("!?,.:")
    if ignore_word(word, ignore_list):
        return True
    if word in acceptable_list:
        return True
    return False
