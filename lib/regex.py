import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

name = r"John\sCena|Anya\sTaylor\-Joy|D\'Angelo"
name_regex = re.compile(name)

phone_number = r"5{10}|5{3}\-5{3}\-5{4}|\(5{3}\)\s5{3}\-5{4}"
phone_regex = re.compile(phone_number)

email_address = r"johncena\@wwe\.com|[A-z]*\@[A-z]{3}\.[A-z]{3}|[A-z]*\.[A-z]*\@[A-z]{3}\.[A-z]{3}|[A-z]*\.[A-z]*[0-9]*\@[A-z]{3}\.[A-z]{3}"
email_regex = re.compile(email_address)
