import re


def contain_blank(choice):
    blank = re.sub("\s", "", choice)
    if blank == "":
        return True
    else:
        return False


def is_not_number(choice):
    number = re.sub("\d\s", "", choice)
    if number == "":
        return True
    else:
        return False
