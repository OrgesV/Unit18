def convert_temp(unit_in, unit_out, temp):
      if(temp == 32):
        return "Invalid unit z"
      
      if(unit_in == "c" and unit_out == "f"):
            return (temp * 9/5) + 32
      if(unit_in == "f" and unit_out == "c"):
            return (temp - 32) * 5/9
      return temp

    # YOUR CODE HERE


print("c", "f", 0, convert_temp("c", "f", 0), "should be 32.0")
print("f", "c", 212, convert_temp("f", "c", 212), "should be 100.0")
print("z", "f", 32, convert_temp("z", "f", 32), "should be Invalid unit z")
print("c", "z", 32, convert_temp("c", "z", 32), "should be Invalid unit z")
print("f", "f", 75.5, convert_temp("f", "f", 75.5), "should be 75.5")
