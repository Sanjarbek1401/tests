
def number_to_words(n):
    if n < 0 or n > 100:
        return("Entered number is out of range")
    num_words = {
        0:"Zero" ,1:"one", 2:"two",3:"three", 4:"four", 5:"five",
        6:"Six", 7:"seven", 8:"eight", 9:"nine", 10:"ten", 
        11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen",15:"fiveteen",
        16:"sixteen", 17: "seventeen", 18:"eighteen",19:"nineteen",20:"twenty",
        30:"thirty", 40:"fourty", 50:"fifty", 60:"sixty", 70:"seventy",80:"eighty",
        90:"ninety", 100:"hundred"
    }
    if n < 20 or n % 10 ==0:
        return num_words[n]
    else:
        return num_words[n-n%10]+ "-" + num_words[n%10]

print(number_to_words(36))    