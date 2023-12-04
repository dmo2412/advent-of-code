def fuel_requirement(s):
  # Initialize the fuel requirement to 0
  fuel = 0
  
  # Split the SNAFU number into its digits
  digits = [d for d in s]
  
  # Initialize the place value to 1 (for the ones place)
  place_value = 1
  
  # Iterate through the digits in reverse order
  for d in reversed(digits):
    if d == '2':
      fuel += 2 * place_value
    elif d == '1':
      fuel += 1 * place_value
    elif d == '0':
      fuel += 0 * place_value
    elif d == '-':
      fuel += -1 * place_value
    elif d == '=':
      fuel += -2 * place_value
    else:
      # If the digit is not recognized, return -1
      return -1
    
    # Update the place value to the next place
    place_value *= 5
  
  # Return the fuel requirement
  return fuel

# Read the input
# fuel_requirements = input().strip().split('\n')
with open('25inp.txt') as f:
    lines = f.readlines()

fuel_requirements = []
for line in lines:
    line = line.strip("\n")
    fuel_requirements.append(line)

# Initialize the total fuel requirement to 0
total_fuel = 0

# Iterate through the fuel requirements
for fr in fuel_requirements:
  # Convert the SNAFU number to a decimal number and add it to the total
  total_fuel += fuel_requirement(fr)

# Print the total fuel requirement
print(total_fuel)
