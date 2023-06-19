import argparse
import gnupg

def verify_signature(signature_file, public_key_file, passphrase):
    gpg = gnupg.GPG()
    with open(public_key_file, "r") as f:
        public_key = f.read()

    with open(signature_file, "rb") as f:
        signature_data = f.read()

    verified_data = gpg.verify_data(signature_data, data=None, key_data=public_key, passphrase=passphrase)
    return verified_data

def main():
    parser = argparse.ArgumentParser(description="PGP signature verifier")
    parser.add_argument("-s", "--signature-file", type=str, required=True, help="File containing the signature")
    parser.add_argument("-b", "--public-key-file", type=str, required=True, help="Public key file")
    parser.add_argument("-p", "--passphrase", type=str, required=True, help="Passphrase for the private key")
    args = parser.parse_args()

    signature_file = args.signature_file
    public_key_file = args.public_key_file
    passphrase = args.passphrase

    verified_data = verify_signature(signature_file, public_key_file, passphrase)

    if verified_data.valid:
        print("Signature verified successfully!")
        print("Verified data:")
        print(verified_data.data.decode('utf-8'))
    else:
        print("Signature verification failed. Error message:")
        print(verified_data.status)

if __name__ == "__main__":
    main()