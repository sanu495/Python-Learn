# Higher Order Function 1

# Giving a input of function to another function

def google_mail(username,domain="gmail.com"):
    return f"{username}@{domain}"

def yahoo_mail(username,domain="yahoo.com"):
    return f"{username}@{domain}"

def outlook_mail(username,domain="outlook.com"):
    return f"{username}@{domain}"

def micro_soft_mail(username,domain="microsoft.com"):
    return f"{username}@{domain}"

def build_mail(username,email_func):         # This function contain another function method (Its call the method instead of us)
    return email_func(username)

print(build_mail("sanoop sanu",google_mail))  # Here Im passing parameter is function 


# Higher Order Function 2
# Return a function from its output

def email_builder(domain):
    def builder_mail(username):
        return f"{username}@{domain}"
    return builder_mail                 # This Function returning a function

gmail=email_builder("gmail.com")       #Pre Bounded Function
yahoo=email_builder("yahoo.com")
micro_soft=email_builder("microsoft.com")

print(gmail("sanoop"))
print(yahoo("sanu"))
print(micro_soft("sebina"))



