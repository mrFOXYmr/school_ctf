enc = [103, 101, 100, 123, 49, 93, 53, 120, 113, 115, 114, 126, 104, 97, 87, 113, 40, 83, 93, 97, 99, 114]
def step1(data):
    return "".join(chr(ord(c) ^ ((i + 3) % 7)) for i, c in enumerate(data))

def step2(data):
    return data[-2:] + data[:-2]

def step3(data):
    even = data[::2]
    odd = data[1::2]
    return even + odd

cipher_text = [ord(c) for c in step3(step2(step1(input())))]
if cipher_text == enc:
    print("valid password")
else:
    print("error.")