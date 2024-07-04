from nada_dsl import *
import random

def nada_main():
    party1 = Party(name="Party1")

    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # function for encryption
    @nada_fn
    def encrypt_message(plain: SecretInteger, k: SecretInteger) -> SecretInteger:
        encrypted = (plain + k) * Integer(3)  
        return encrypted

    # decryption function
    @nada_fn
    def decrypt_message(encrypted: SecretInteger, k: SecretInteger) -> SecretInteger:
        decrypted = (encrypted / Integer(3)) - k 
        return decrypted

    #function invocation , then storing returned values
    encrypted_message = encrypt_message(my_int1, my_int2)
    decrypted_message = decrypt_message(encrypted_message, my_int2)

    #output formattting
    output_original = Output(my_int1, "original_message", party1)
    output_encrypted = Output(encrypted_message, "encrypted_message", party1)
    output_decrypted = Output(decrypted_message, "decrypted_message", party1)

    return [output_original, output_encrypted, output_decrypted]
