-> It uses 2's Complement to store thr negative values 
    -> 1's Complement -> Inverse all the bits in the value
    -> 2's Complement -> Add 1 to 1's complement in the value


How to store number float: 
-> 32 bits -> 1 bit(sign bit) | 8 bit (Exponent) | 23 bits (Mantissa)

    -> How to convert bits for decimal points
        -> Multiply the bit with 2 and take the value at the left side of dot 
            ex. 0.125 = 001
                0.125 * 2 => 0.25 = 0
                0.25  * 2 => 0.5  = 0
                0.5   * 2 => 1.0  = 1
                0.0   * 2 => 0.0  = 0

-> Steps to store the number: (Example for value 8.125)
    -> Find the binary of the number => binary of 8 = 1000, 0.125 =>001=> Value = 1000.001 
    -> Make it in the form of (1.xx) * 2^exp => 1000.001 = 1.000001(000001 IS CALLED MENTISSA) * 2^3
    -> Add bias to the exponent => Bias for floating number is 127 => 3+127 = 130
    -> Take binary of the exponent => bnary of 130 => 10000010
    -> Place value in memory in above format
        SIGN BIT = 0 (+VE)
        EXPONENT = 10000010
        MANTISSA = 0000010000.....

-> Getting this stored decimal number 
    => Use this formula (-1)^sign Bit * (1+Mantissa)*2^(Exp - Bias)
    => (-1)^0+(1+Mantissa)*2^3
    => (1+2^-6 (Found one at the 6th place after decimal))*8
    => 1.015625 * 8
    => 8.125

Storing Double in memory
=> 64 bits -> 1 bit(sign bit) | 11 bit (Exponent) | 52 bits (Mantissa)

bias = 2^(expontnt bit length-1)-1 = 2^(11-1)-1 =>2^10 -1 = 1023
