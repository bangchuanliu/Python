from hashlib import md5
from struct import unpack_from


def hash(item):
    k = md5(str(item).encode("utf-8")).digest()
    h = unpack_from(">I",k)[0]
    return h