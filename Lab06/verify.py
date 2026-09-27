import hashlib, hmac, sys

def verify(user, candidate):
    for line in open("shadow_db.txt"):
        u, record = line.strip().split(":", 1)
        if u != user:
            continue

        _, alg, iters, salt_hex, expected = record.split("$")

        dk = hashlib.pbkdf2_hmac(
            alg.replace("pbkdf2-", ""),
            candidate.encode(),
            bytes.fromhex(salt_hex),
            int(iters)
        )

        return hmac.compare_digest(dk.hex(), expected)

    return False

print("ACCEPT" if verify(sys.argv[1], sys.argv[2]) else "REJECT")
