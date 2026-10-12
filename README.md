# COMP 301 — Security Labs

This repository documents hands-on security labs completed as part of COMP 301 coursework at Loyola University Chicago.

The exercises move from foundational cryptography into practical authentication, password security, public-key infrastructure, multi-factor authentication, and enterprise authentication protocols. The repository emphasizes not only implementing security mechanisms, but also understanding their limitations, attack surfaces, and appropriate deployment scenarios.

## Areas Covered

The labs demonstrate practical experience with:

- Classical and modern cryptography
- AES symmetric encryption
- RSA and elliptic-curve cryptography
- Hybrid encryption
- Diffie-Hellman / ECDH key exchange
- X.509 certificates and certificate chains
- TLS and PKI validation
- Certificate revocation concepts
- Secure password hashing and salting
- PBKDF2 and scrypt
- Constant-time password verification
- Multi-factor authentication
- HOTP and TOTP
- Replay resistance
- FIDO2 / WebAuthn concepts
- EAP enterprise authentication methods
- Mutual certificate authentication
- Challenge-response authentication

## Lab Overview

| Lab | Topic | Key Concepts |
| --- | --- | --- |
| [Lab 02](./Lab02) | Classical Cryptography | Caesar cipher, Rail Fence cipher, encryption and decryption |
| [Lab 03](./Lab03) | Symmetric Encryption | AES-128-CTR, keys, initialization vectors, OpenSSL |
| [Lab 04](./Lab04) | Asymmetric Encryption & Key Exchange | RSA-OAEP, hybrid encryption, ECC, ECDH, AES-256-CTR |
| [Lab 05](./lab05) | TLS, Certificates & PKI | X.509 certificate inspection, certificate chains, trust anchors, CRL and OCSP |
| [Lab 06](./Lab06) | Password Storage | SHA-256 weaknesses, salts, PBKDF2, scrypt, constant-time verification |
| [Lab 07](./Lab07) | Multi-Factor Authentication | HOTP, TOTP, password + OTP authentication, replay attacks, FIDO2/WebAuthn |
| [Lab 08](./Lab08) | EAP Authentication Protocols | EAP-TLS, EAP-FAST, EAP-TTLS, PEAP, certificates, PACs, challenge-response |

## Selected Technical Work

### Classical Cryptography

Lab 02 implements Caesar and Rail Fence ciphers in Python, including both encryption and decryption. These exercises establish the distinction between substitution and transposition techniques before moving into modern cryptographic systems.

### AES Symmetric Encryption

Lab 03 uses OpenSSL to perform AES-128-CTR encryption. The exercise demonstrates the relationship between plaintext, ciphertext, cryptographic keys, and initialization vectors.

### RSA, ECC, and Hybrid Encryption

Lab 04 explores public-key cryptography through several mechanisms:

- RSA key generation
- RSA-OAEP protection of symmetric keys
- AES-based hybrid encryption
- ECC key generation
- ECDH shared-secret establishment
- Derivation of symmetric encryption keys from shared secrets
- Verification that independently derived ECDH secrets match

Private keys and sensitive key material generated during the exercise were intentionally excluded from the public repository.

### TLS and Public-Key Infrastructure

Lab 05 examines real X.509 certificates and trust relationships.

The work includes:

- Inspecting certificate subjects and issuers
- Following a certificate chain
- Identifying certificate authorities and trust anchors
- Examining certificate validity periods
- Comparing CRL and OCSP revocation approaches
- Understanding how a client establishes trust in a server certificate

### Secure Password Storage

Lab 06 demonstrates why password storage should not rely on plaintext, reversible encryption, or fast unsalted hashes.

The exercise progresses through:

1. Unsalted SHA-256 password hashes
2. Per-user random salts
3. Slow password-hashing functions
4. PBKDF2-HMAC-SHA256 with 600,000 iterations
5. Constant-time password verification

A test dictionary attack demonstrated the security impact of a slow KDF. In one VM run, the experimental rate dropped from approximately **60,241 SHA-256 hashes/second to 2.1 PBKDF2 guesses/second**, representing roughly a **28,686× slowdown**.

The exercise also demonstrates an important security principle: strong password hashing increases the cost of offline attacks, but weak passwords can still be guessed. Password policy and MFA remain necessary defense layers.

### Multi-Factor Authentication

Lab 07 explores authentication using multiple factor categories.

The work covers:

- Knowledge factors
- Possession factors
- Inherence factors
- HOTP counter-based authentication
- TOTP time-based authentication
- TOTP expiration and replay behavior
- A two-factor password + TOTP login implementation
- Phishing limitations of OTP systems
- FIDO2/WebAuthn as a phishing-resistant alternative

The two-factor implementation requires both a PBKDF2-verified password and a valid TOTP code before authentication succeeds.

### Enterprise Authentication with EAP

Lab 08 compares enterprise authentication methods:

- EAP-TLS
- EAP-FAST
- EAP-TTLS
- PEAP

The exercises demonstrate how these methods differ in certificate requirements and credential handling.

EAP-TLS uses mutual certificate authentication, while PEAP and EAP-TTLS establish a server-authenticated TLS tunnel before performing client authentication inside that tunnel. EAP-FAST demonstrates the use of a Protected Access Credential (PAC).

The lab also demonstrates replay resistance using fresh challenge-response values.

## Security Principles Reinforced

Across the labs, several recurring security principles are demonstrated:

**Defense in depth**  
No single control is sufficient. Secure systems combine encryption, authentication, credential protection, MFA, and access controls.

**Never store passwords directly**  
Passwords should be protected using a salted, deliberately slow password-hashing function.

**Private keys must remain private**  
Public certificates and public keys can be distributed; private keys should never be committed to a public repository.

**Authentication and encryption solve different problems**  
Encryption protects confidentiality, while certificates, signatures, MACs, and authentication protocols establish identity and integrity.

**Replay resistance matters**  
Fresh challenges, counters, timestamps, and per-session values prevent previously captured authentication material from being reused.

**Phishing resistance matters**  
OTP-based MFA improves security but can still be phished. FIDO2/WebAuthn provides stronger protection by using asymmetric credentials bound to the legitimate web origin.

## Technologies and Tools

- Python 3
- OpenSSL
- Linux / Ubuntu
- SSH
- Git
- GitHub
- SHA-256
- HMAC
- PBKDF2
- scrypt
- AES
- RSA
- ECC / ECDH
- X.509
- TLS
- HOTP / TOTP
- EAP

## Repository Structure

```text
COMP301-Labs/
```

Each directory contains the code, test artifacts, results, or submission evidence associated with that exercise.

## Security Notice
All credentials, certificates, passwords, seeds, and cryptographic values in this repository are educational test data created specifically for laboratory exercises.
They are not production credentials and should never be reused for real accounts or systems.
Private cryptographic keys are intentionally excluded where appropriate.

## Purpose
This repository serves both as a record of COMP 301 coursework and as a practical security portfolio demonstrating experience with cryptographic primitives, authentication systems, password security, PKI, MFA, and enterprise authentication protocols.
The work focuses on understanding not only how security mechanisms operate, but also why they fail when implemented incorrectly and how stronger designs mitigate those weaknesses.
