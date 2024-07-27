string : str = "   Python is fun!   "
trimmed_string = string.strip()
print("Trimmed string:", '"' + trimmed_string + '"')
left_side_justified = trimmed_string.ljust(20, '*')
print("Left justified:", '"' + left_side_justified + '"')
right_side_justified = trimmed_string.rjust(20, '*')
print("Right justified:", '"' + right_side_justified + '"')