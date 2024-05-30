# funtion to call my program
def main():
    # greet user
    print(" Hey, welcome to email slicer ")
    print("")

    # collect user email
    email_address = input("Enter your email address: ")

    # slice or split it in between @ and . e.g: hello@ebubemoses.com
    """ username=hello, domain=ebubemoses.com, split_domain, domain=ebubemoses, extension=com """
    (user_name, domain) = email_address.split("@")
    (domain, extension) = domain.split(".")

    # print slicing call
    print("Username:", user_name)
    print("Domain:", domain)
    print("Extension:", extension)

# run function over again until false....
while True:
    try:
        # call out all function
        main()
    except:
        print("Wrong E-mail.")
