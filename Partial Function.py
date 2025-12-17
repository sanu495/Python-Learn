# Partial Function

# In Partial Function if function need two arguments (we can give one argument)

from functools import partial

def calculate_prices(base_price,tax_price):
    return base_price *(1 + tax_price)

price_with_gst=partial(calculate_prices,tax_price=0.18)  # Partial function helps for a fixed arguments value (tax)

print(price_with_gst(7886))        # passing a one argument


def create_mail(username,domain_name):
    return f"{username}@{domain_name}"

gmail=partial(create_mail,domain_name="gmail.com")
ymail=partial(create_mail,domain_name="ymail.com")

print(gmail("sanoop"))
print(ymail("sanu464"))