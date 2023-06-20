import argparse
import gnupg

def generate_keypair(gpg, name, email, passphrase):
    input_data = gpg.gen_key_input(
        key_type="RSA",
        key_length=2048,
        name_real=name,
        name_email=email,
        passphrase=passphrase
    )
    key = gpg.gen_key(input_data)
    return key

def save_keys(gpg, public_key_file, private_key_file, key):
    public_key = gpg.export_keys(key.fingerprint)
    private_key = gpg.export_keys(key.fingerprint, secret=True)

    with open(public_key_file, "w") as f:
        f.write(public_key)

    with open(private_key_file, "w") as f:
        f.write(private_key)

def main():
    parser = argparse.ArgumentParser(description="PGP key pair generator")
    parser.add_argument("-n", "--name", dest="name", type=str, required=True, help="Name for the key owner")
    parser.add_argument("-e", "--email", dest="email", type=str, required=True, help="Email address for the key owner")
    parser.add_argument("-p", "--passphrase", dest="passphrase", type=str, required=True, help="Passphrase to protect the private key")
    parser.add_argument("--public-key-file", default="public_key.asc", help="Output file for the public key")
    parser.add_argument("--private-key-file", default="private_key.asc", help="Output file for the private key")
    args = parser.parse_args()

    gpg = gnupg.GPG()
    key = generate_keypair(gpg, args.name, args.email, args.passphrase)
    save_keys(gpg, args.public_key_file, args.private_key_file, key)

    print("Key pair generated successfully!")
    print(f"Public key saved to: {args.public_key_file}")
    print(f"Private key saved to: {args.private_key_file}")

if __name__ == "__main__":
    main()