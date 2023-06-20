import argparse
import gnupg

def verify_signature(signature_file, public_key_file):
    gpg = gnupg.GPG()
    with open(public_key_file, "r") as f:
        public_key_data = f.read()

    with open(signature_file, "rb") as f:
        signature_data = f.read()

    verified_data = gpg.verify(signature_data, key_data=public_key_data)

    if verified_data.valid:
        return True
    else:
        return False

def main():
    parser = argparse.ArgumentParser(description="PGP signature verifier")
    parser.add_argument("-s", "--signature-file", type=str, required=True, help="File containing the signature")
    parser.add_argument("-b", "--public-key-file", type=str, required=True, help="Public key file")
    args = parser.parse_args()

    signature_file = args.signature_file
    public_key_file = args.public_key_file

    if verify_signature(signature_file, public_key_file):
        print("Signature verified successfully!")
    else:
        print("Signature verification failed.")

if __name__ == "__main__":
    main()