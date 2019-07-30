"""
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""

def count_decode(message):
    nb_ways = 0
    
    def count_digits(message):
        return len(message)
        
    def decode(message, nb_ways):
        if count_digits(message) <= 2:
            if message[0]!='0' and message>='1' and message<='10':  # '0' and 'Ox' are not decodable
                nb_ways += 1
            elif message>='11' and message<='26':                   
                nb_ways += 2
            elif message>='27' and message<='99':
                nb_ways += 1
            return nb_ways

        elif count_digits(message) >= 3:
            first_digit = message[0]
            if first_digit!='0':
                nb_ways = decode(message[1:], nb_ways)
            
            first_two_digits = message[:2]            
            if first_two_digits>='1' and first_two_digits<='26':
                nb_ways = decode(message[2:], nb_ways)
        
        return nb_ways
        
    return decode(message, nb_ways)       
        
    
    
if __name__ == "__main__":
    print(count_decode('111'))
    print(count_decode('12010'))
    
    


    