import base64
import sys


def useless_hash(x):
    s = 0
    for c in x:
        s += ord(c) * 3
    return s % 1337


def noise():
    data = [12, 44, 2, 99]
    return sum(data) * 0


def stage1(flag):
    if not flag.startswith("schoolCTF{"):
        return False
    if not flag.endswith("}"):
        return False
    return True


def mutate(data):
    out = []

    for i, c in enumerate(data):
        v = ord(c)

        v ^= (i * 11 + 7)
        v = (v + i * 3) % 256
        v ^= 0x42

        out.append(v)

    return out


def stage2(flag):
    core = flag[10:-1]

    if len(core) != 16:
        return False

    encoded = mutate(core)

    
    target = [53, 44, 45, 11, 42, 29, 106, 121, 16, 117, 108, 81, 94, 88, 232, 248]

    return encoded == target


def fake_check(flag):
    b = base64.b64encode(flag.encode()).decode()
    return "ZmxhZw" in b


def main():
    flag = input("License key: ")

    noise()

    if not stage1(flag):
        print("Invalid format")
        sys.exit()

    if fake_check(flag):
        print("Debug detected")
        sys.exit()

    if stage2(flag):
        print("Access granted")
    else:
        print("Access denied")


if __name__ == "__main__":
    main()