from Writer import Writer
if __name__ == '__main__':
    adresa = ('127.0.0.1',20000)
    writer = Writer(adresa)
    writer.start()