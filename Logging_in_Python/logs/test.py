from logger import logging
def add(a,b):
    logging.debug("The addition Function is Taking Place")
    return a+b

logging.debug("The addition Funciton is Called")
add(2,3)