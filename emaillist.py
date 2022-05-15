import re
def is_email(address):
    if re.search("[\w._%+-]{1,20}@[\w.-]{2,20}.[a-zA-z]{2,3}", address):
        print("{} is valid".format(address))
    else:
        print("{} isn't valid".format(address))


def main():
    is_email("db@aol.com")
    is_email("m@.com")
    is_email("@apple.com")
    is_email("db@.com")

main()
