import hashlib, hmac, secrets

# Server stores a SALTED HASH (Lab 06), never the password.
salt = secrets.token_bytes(16)
stored = hashlib.pbkdf2_hmac("sha256", b"Tr0pical!9", salt, 600_000)

# Server issues a fresh challenge for this session.
challenge = secrets.token_bytes(16)

# Client answers HMAC(password, challenge)
def respond(password, chal):
    return hmac.new(password.encode(), chal, hashlib.sha256).hexdigest()

client_proof = respond("Tr0pical!9", challenge)
server_expected = respond("Tr0pical!9", challenge)

print("challenge-response inner auth:",
      "ACCEPT" if hmac.compare_digest(client_proof, server_expected) else "REJECT")

# Replay test: attacker reuses old proof with a NEW challenge.
new_challenge = secrets.token_bytes(16)
replayed = client_proof
expected_new = respond("Tr0pical!9", new_challenge)

print("replayed response vs new challenge:",
      "ACCEPT" if hmac.compare_digest(replayed, expected_new) else "REJECT")
