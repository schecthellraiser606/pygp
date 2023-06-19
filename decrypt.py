import argparse
import gnupg

def decode_data(encrypted_data_file, private_key_file, passphrase):
    gpg = gnupg.GPG()
    with open(private_key_file, "r") as f:
        private_key = f.read()

    with open(encrypted_data_file, "rb") as f:
        encrypted_data = f.read()

    decrypted_data = gpg.decrypt(encrypted_data, passphrase=passphrase, key_data=private_key)
    return decrypted_data


def main():
    parser = argparse.ArgumentParser(description="PGP data decoder")
    parser.add_argument("-e", "--encrypted-data-file", type=str, required=True, help="File containing the encrypted data")
    parser.add_argument("-r", "--private-key-file", type=str, required=True, help="Private key file")
    parser.add_argument("-p", "--passphrase", type=str, required=True, help="Passphrase for the private key")
    args = parser.parse_args()

    encrypted_data_file = args.encrypted_data_file
    private_key_file = args.private_key_file
    passphrase = args.passphrase

    decrypted_data = decode_data(encrypted_data_file, private_key_file, passphrase)

    if decrypted_data.ok:
        print("Data decoded successfully!")
        print("Decoded data:")
        print(decrypted_data.data.decode('utf-8'))
    else:
        print("Failed to decode the data. Error message:")
        print(decrypted_data.status)

if __name__ == "__main__":
    main()