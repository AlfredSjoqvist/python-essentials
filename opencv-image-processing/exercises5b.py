


# 506 #
def create_lock(set_passcode, message):
    def unpack_message(compare_passcode):
        if set_passcode == compare_passcode:
            return message
        else:
            return "Fel kod!"
    
    return unpack_message


# 506 #
lock = create_lock(123, "hej")
print(lock(2))
print(lock(123))


# 507 #
double_int = lambda x: 2*x
print(double_int(4))


# 508 #
sum_of_squares = lambda x, y: x**2 + y**2
print(sum_of_squares(2, 3))


# 509 #
double_lamb_add = lambda x: lambda y: x+y
print(double_lamb_add(2)(5))
print(double_lamb_add(2))



