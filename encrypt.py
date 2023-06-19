import argparse
import gnupg

def encode_data(data, public_key_file):
    gpg = gnupg.GPG()
    with open(public_key_file, "r") as f:
        public_key = f.read()

    encrypted_data = gpg.encrypt(data, recipients=None, armor=True, always_trust=True, key_data=public_key)
    return encrypted_data

def main():
    parser = argparse.ArgumentParser(description="PGP data encoder")
    parser.add_argument("-d", "--data", type=str, required=True, help="Data to encode")
    parser.add_argument("-b", "--public-key-file", type=str, required=True, help="Public key file")
    args = parser.parse_args()

    encoded_data = encode_data(args.data, args.public_key_file)

    print("Data encoded successfully!")
    print("Encoded data:")
    print(encoded_data.data.decode('utf-8'))

if __name__ == "__main__":
    main()