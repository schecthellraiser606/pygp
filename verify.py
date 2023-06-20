import argparse
import gnupg

def verify_signature(pubkey_file, signature_file):
    gpg = gnupg.GPG()

    with open(pubkey_file, 'r') as f:
        key_data = f.read()
        import_result = gpg.import_keys(key_data)
        if import_result.count == 0:
            raise ValueError('Failed to import public key')

    public_key = import_result.fingerprints[0]

    with open(signature_file, 'r') as f:
        signature_data = f.read()

    verified = gpg.verify(signature_data)

    if verified.fingerprint == public_key and verified.valid:
        print("\n[+] Signature is valid\n")
    else:
        print("\n[!] Signature is not valid\n")

def main():
    parser = argparse.ArgumentParser(description="PGP signature verifier")
    parser.add_argument("-p", "--pubkey-file", type=str, required=True, help="Public key file")
    parser.add_argument("-s", "--signature-file", type=str, required=True, help="File containing the signature")
    args = parser.parse_args()

    pubkey_file = args.pubkey_file
    signature_file = args.signature_file

    verify_signature(pubkey_file, signature_file)

if __name__ == "__main__":
    main()