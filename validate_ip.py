def is_valid_octet(octet: str) -> bool:
    """
    Validates a given octet.

    Return: True if it's a valid number between 0 and 255,
    False otherwise.
    """
    try:
        int(octet)
        return 0 <= int(octet) <= 255

    except ValueError:
        return False  # The octet contained something other than a number


def is_valid_address(address: str) -> bool:
    """
    Validates a given address

    Return: True if the address has 4 valid octets, False otherwise.
    """
    octets = address.split('.')

    if not len(octets) == 4:
        return False

    for octet in octets:

        if not is_valid_octet(octet):
            return False

    return True


def main():
    """
    The main loop
    """
    while True:

        address = input("Enter an ip address (X to exit): ")

        if address.lower() == 'x':
            break
        elif is_valid_address(address):
            print("Valid")
        else:
            print("Not a valid address")


if __name__ == '__main__':
    main()
