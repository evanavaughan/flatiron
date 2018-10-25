import re

def say_hello(name):
    # takes in a name and returns the string "Hi my name is " plus the name
    # use whichever form of interpolation is most appropriate
    return "Hi my name is {}".format(name)
#print(say_hello("Bob"))

def replace_given_substring(str_to_replace, str_to_insert, string):
    return string.replace(str_to_replace, str_to_insert)
#print(replace_given_substring("name", "Bob", "People call me name"))

def remove_duplicate_period(string):
    return re.sub(r'\.+', r".", string)

def remove_duplicate_question(string):
    return re.sub(r'\?+', r"?", string)

def remove_duplicate_excl(string):
    return re.sub(r'\!+', r"!", string)

def remove_duplicate_comma(string):
    return re.sub(r'\,+', r",", string)

def remove_duplicate_punctuation(string):
        # should remove all duplicate punctuation marks in a given string
        # i.e. "Hi!!!!!!" should be reformatted to "Hi!"
        # i.e. "Hello..... My name is Terrance!! How are you???" -> "Hello. My name is Terrance! How are you?"
    x = remove_duplicate_period(string)
    y = remove_duplicate_comma(x)
    z = remove_duplicate_excl(y)
    return remove_duplicate_question(z)


def validate_email_format(email):
    regex = re.compile('[_!#$%^&*()<>?/\|}{~:]')
    if(regex.search(email) == None):
        if email.endswith('.com') and email.find(r'[\@]'):
            return True
    else:
        return False


def anonymize_credit_card_number(credit_card_number):
        # should replace all characters except the last 4 with 'X'
        # return the anonymized credit card number as a string
        # the credit card may have characters that are not numbers (i.e. spaces and dashes, which we would want to keep)
        # i.e. 1234-5678-90-1234 -> XXXX-XXXX-XX-1234
    #    credit_card_number = str(credit_card_number)
    #    return credit_card_number[-4:-1] = "XXXX"
    last_four = credit_card_number[-4:]
    numbers_to_x = re.sub(r'\d', 'X', credit_card_number)
    beginning_card_portion = numbers_to_x[0:-4]
    return beginning_card_portion + last_four
