import time
def fast(text):
    while  True:
        print('\r'+text,end='')
        time.sleep(0.3)
        text=text[1:]+text[0]
fast('Fast text today ')

