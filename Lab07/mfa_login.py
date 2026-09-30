import base64, hashlib, hmac, secrets, struct, time

# --- account registration ---
def register(user, password):
    salt = secrets.token_bytes(16)
    dk = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 600_000)
    seed = base64.b32encode(secrets.token_bytes(20)).decode()
    with open("mfa_db.txt", "a") as db:
        db.write(f"{user}:$pbkdf2-sha256$600000${salt.hex()}${dk.hex()}:{seed}\n")
    return seed

# --- factors ---
def check_password(record, candidate):
    _, alg, iters, salt_hex, expected = record.split("$")
    dk = hashlib.pbkdf2_hmac(
        alg.replace("pbkdf2-", ""),
        candidate.encode(),
        bytes.fromhex(salt_hex),
        int(iters)
    )
    return hmac.compare_digest(dk.hex(), expected)

def totp(seed, for_time=None, step=30, digits=6):
    key = base64.b32decode(seed, casefold=True)
    if for_time is None:
        for_time = int(time.time())

    h = hmac.new(
        key,
        struct.pack(">Q", int(for_time / step)),
        hashlib.sha1
    ).digest()

    o = h[19] & 15

    return str(
        (struct.unpack(">I", h[o:o+4])[0] & 0x7fffffff)
        % (10 ** digits)
    ).zfill(digits)

def login(user, password, code):
    for line in open("mfa_db.txt"):
        u, record, seed = line.strip().split(":")
        if u == user:
            f1 = check_password(record, password)
            f2 = hmac.compare_digest(totp(seed), code)
            print(f"factor1(knowledge)={f1} factor2(possession)={f2}")
            return f1 and f2

    return False

# --- demo ---
seed = register("alice", "Tr0pical!9")
print(f"alice's TOTP seed: {seed}  (this line is what a QR code would carry)")

good = totp(seed)

print("correct password + current code ->",
      "ACCEPT" if login("alice", "Tr0pical!9", good) else "REJECT")

print("wrong password + current code   ->",
      "ACCEPT" if login("alice", "wrong", good) else "REJECT")

print("correct password + stale code   ->",
      "ACCEPT" if login(
          "alice",
          "Tr0pical!9",
          totp(seed, int(time.time()) - 60)
      ) else "REJECT")

print("correct password + random code  ->",
      "ACCEPT" if login(
          "alice",
          "Tr0pical!9",
          "000000"
      ) else "REJECT")
