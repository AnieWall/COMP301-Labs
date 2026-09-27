import hashlib, hmac, secrets

# --- provisioning (done once, in-band, by the server) ---
pac_key = secrets.token_bytes(32)
pac_id  = "alice-pac-001"
print(f"provisioned PAC id={pac_id}")

# --- tunnel setup ---
client_hello = secrets.token_bytes(16)
server_hello = secrets.token_bytes(16)

def derive_tunnel_key(pac, label, c, s):
    return hmac.new(pac, label + c + s, hashlib.sha256).digest()

client_tk = derive_tunnel_key(
    pac_key, b"EAP-FAST tunnel", client_hello, server_hello
)

server_tk = derive_tunnel_key(
    pac_key, b"EAP-FAST tunnel", client_hello, server_hello
)

print("tunnel key established from PAC:",
      "MATCH" if hmac.compare_digest(client_tk, server_tk) else "MISMATCH")

# Client with the wrong PAC
wrong_pac = secrets.token_bytes(32)

attacker_tk = derive_tunnel_key(
    wrong_pac, b"EAP-FAST tunnel", client_hello, server_hello
)

print("attacker with wrong PAC derives same tunnel key:",
      "yes" if hmac.compare_digest(attacker_tk, server_tk)
      else "no (rejected)")
