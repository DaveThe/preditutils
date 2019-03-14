import logging
def print_hello(text="word"):
    logging.exception("AAAAAAAA")
    print(text)
    raise RuntimeError('disagio!')
