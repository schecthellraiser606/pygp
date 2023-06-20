import argparse
import gnupg

def sign_message(message, private_key_file, passphrase):
    gpg = gnupg.GPG()
    with open(private_key_file, "r") as f:
        private_key = f.read()

    signed_data = gpg.sign(message, keyid=private_key, passphrase=passphrase)
    return signed_data

def main():
    parser = argparse.ArgumentParser(description="PGP message signer")
    parser.add_argument("-m", "--message", type=str, required=True, help="Message to sign")
    parser.add_argument("-r", "--private-key-file", type=str, required=True, help="Private key file")
    parser.add_argument("-p", "--passphrase", type=str, required=True, help="Passphrase for the private key")
    args = parser.parse_args()

    message = args.message
    private_key_file = args.private_key_file
    passphrase = args.passphrase

    signed_data = sign_message(message, private_key_file, passphrase)

    if signed_data.status == "signature created":
        print("Message signed successfully!")
        print("Signed message:")
        print(signed_data.data.decode('utf-8'))
    else:
        print("Failed to sign the message. Error message:")
        print(signed_data.status)

if __name__ == "__main__":
    main()