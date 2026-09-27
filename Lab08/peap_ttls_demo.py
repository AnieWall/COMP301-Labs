import subprocess, hashlib, hmac, secrets

def verify(cert_file):
    r = subprocess.run(["openssl", "verify", "-CAfile", "ca.pem", cert_file],
                       capture_output=True, text=True)
    return r.stdout.strip().endswith("OK")

def peap_ttls(server_cert, client_cert, password):
    """PEAP / EAP-TTLS: only the SERVER presents a certificate."""
    print("  1. server sends its certificate; client presents:",
          client_cert or "no certificate")

    if not verify(server_cert):
        return "FAIL: client could not verify the server certificate"

    print("  2. client VERIFIED the server certificate -> TLS tunnel is up")
    print("     (client needed no certificate -> no per-device PKI required)")

    challenge = secrets.token_bytes(16)
    proof = hmac.new(password.encode(), challenge, hashlib.sha256).hexdigest()
    expected = hmac.new(b"Tr0pical!9", challenge, hashlib.sha256).hexdigest()

    ok = hmac.compare_digest(proof, expected)

    print("  3. inner challenge-response inside tunnel:",
          "ACCEPT" if ok else "REJECT")

    return "EAP-Success (password protected by tunnel)" if ok else "FAIL: bad password"

print("[PEAP / EAP-TTLS, client has NO certificate, uses a password]")
print(" ", peap_ttls("server.pem", None, "Tr0pical!9"))
