from itertools import product

# I think i should implement this as a generator
def xor_decryptor(record, options):
    print("in decryptor")

    if options["attack_type"] == "Brute force":
        xor_key_length = options["key_length"]

        if int(xor_key_length) > len(record):
            print("Key length larger than record")
            return 

        # get all XOR keys
        possible_keys = product(range(256), repeat=int(xor_key_length))
        # for key in keys:
        for key in possible_keys:
            yield (bytes([b ^ key[i % len(key)] for i, b in enumerate(record)]), list(key))

    else:
        print("Not implemented attack_type in xor_decryptor function")
        return 