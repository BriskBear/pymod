from time import localtime, strftime, time

# Supply epoch integer to see the conversion, or get the current epoch time (no input)
epoch = lambda stamp=None: int(time()) if stamp == None else strftime('%Y-%m-%d %H:%M:%S', localtime(int(stamp)))
