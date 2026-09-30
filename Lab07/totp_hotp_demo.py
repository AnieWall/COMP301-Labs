import base64, hmac, hashlib, struct, time

secret_b32 = 'JBSWY3DPEHPK3PXP'
key = base64.b32decode(secret_b32, casefold=True)

def hotp(key, counter, digits=6):
    counter_bytes = struct.pack('>Q', counter)
    h = hmac.new(key, counter_bytes, hashlib.sha1).digest()
    o = h[19] & 15
    code = (struct.unpack('>I', h[o:o+4])[0] & 0x7fffffff) % (10 ** digits)
    return str(code).zfill(digits)

def totp(key, for_time=None, step=30, digits=6):
    if for_time is None:
        for_time = int(time.time())
    counter = int(for_time / step)
    return hotp(key, counter, digits)

print('TOTP now:', totp(key))
print('TOTP after 31s:', totp(key, for_time=int(time.time())+31))
print('HOTP counter=1:', hotp(key, 1))
print('HOTP counter=2:', hotp(key, 2))
