# COMP301 Lab 04: Asymmetric Encryption and Key Exchange

> **Repository note:** Private keys and secret key material generated during this lab were retained locally and are intentionally not included in this public repository. Public keys, ciphertexts, plaintext/recovered test files, and the README are included.

## Part 1: OpenSSH Algorithms and Key Generation

OpenSSH public-key algorithms and key-exchange methods were examined using `ssh -Q key` and `ssh -Q kex`.

RSA, ECDSA, and Ed25519 SSH key pairs were generated and their fingerprints were inspected.

Generated during the exercise:
- `rsa_id` / `rsa_id.pub`
- `ecdsa_id` / `ecdsa_id.pub`
- `ed25519_id` / `ed25519_id.pub`

These SSH key pairs were generated for Part 1 testing and are not included as submission artifacts.

## Part 2: RSA Hybrid Encryption

A 2048-bit RSA key pair was generated. A random 32-byte AES key was then generated and protected using RSA-OAEP with SHA-256.

The AES key was recovered with the RSA private key and verified against the original. AES-256-CTR was then used to encrypt and decrypt the test message. The recovered plaintext matched the original.

Associated files:
- `rsa_private.pem`
- `rsa_public.pem`
- `aes_key.bin`
- `aes_key_raw.bin`
- `aes_key.enc`
- `aes_key_recovered.bin`
- `aes_iv.bin`
- `plaintext.txt`
- `ciphertext.enc`
- `recovered.txt`

The generated AES key and IV were stored in their corresponding lab files rather than displayed in this README.

## Part 3: ECC Key Exchange (ECDH)

Independent ECC key pairs for Alice and Bob were generated using the `prime256v1` curve.

Alice derived a shared secret using Alice's private key and Bob's public key. Bob independently derived a shared secret using Bob's private key and Alice's public key. The two resulting shared-secret files were compared with `diff` and were identical.

The ECDH shared secret was hashed with SHA-256 to derive an AES-256 key. AES-256-CTR was then used to encrypt and decrypt the ECC-track message. The recovered plaintext matched the original.

Associated files:
- `alice_private.pem`
- `alice_public.pem`
- `alice_shared.bin`
- `bob_private.pem`
- `bob_public.pem`
- `bob_shared.bin`
- `aes_key_ecc.bin`
- `aes_iv_ecc.bin`
- `plaintext_ecc.txt`
- `ciphertext_ecc.enc`
- `recovered_ecc.txt`

The derived AES key and generated IV were stored in their corresponding lab files rather than displayed in this README.

## Completion

Parts 1, 2, and 3 of COMP301 Lab 04 were completed successfully.
