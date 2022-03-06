def same_frequency(num1, num2):
    if len(str(num1)) == len(str(num2)):
        for num in str(num1):
            if(str(num1).count(num) != str(num2).count(num)):
                return False
        return True
    return False
    
           
    
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """