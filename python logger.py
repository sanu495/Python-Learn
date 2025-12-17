# Python Logger
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    #filename="app.log", # you can remove this line to log to console
    filemode="w"
)

def divide(a,b):
    logging.info(f"Dividing {a} by {b}")
    try:
        result=a/b
        logging.debug(f"Result : {result}")
        return result
    except ZeroDivisionError:
        logging.error("Tried to divide by zero")
        return None
    
divide(30,5)
divide(48,0)