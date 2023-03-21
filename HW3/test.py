from slide_window import slide_window_fn

ip = range(10)
output = slide_window_fn(input = list(ip),width = 3,increment = 4)
print(output)
