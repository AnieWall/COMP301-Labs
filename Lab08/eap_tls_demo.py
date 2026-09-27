import subprocess

def verify(cert_file):
    """The real certificate check: does this chain to our CA?"""
    r = subprocess.run(["openssl", "verify", "-CAfile", "ca.pem", cert_file],
                       capture_output=True, text=True)
    return r.stdout.strip().endswith("OK")

def subject(cert_file):
    r = subprocess.run(["openssl", "x509", "-in", cert_file, "-noout", "-subject"],
                       capture_output=True, text=True)
    return r.stdout.strip()

def eap_tls(server_cert, client_cert):
    """EAP-TLS: BOTH sides present and verify a certificate. No password exists."""
    print("  1. server sends its certificate ->", subject(server_cert))
    if not verify(server_cert):
        return "FAIL: client could not verify the server certificate"
    print("  2. client VERIFIED the server certificate")
    if client_cert is None:
        return "FAIL: EAP-TLS requires a client certificate, client has none"
    print("  3. client sends its certificate ->", subject(client_cert))
    if not verify(client_cert):
        return "FAIL: server could not verify the client certificate"
    print("  4. server VERIFIED the client certificate;",
          "server learns identity:", subject(client_cert))
    return "EAP-Success (mutual certificate authentication, no password used)"

print("[EAP-TLS, client has certificate]")
print(" ", eap_tls("server.pem", "client.pem"))

print("\n[EAP-TLS, client has NO certificate]")
print(" ", eap_tls("server.pem", None))
