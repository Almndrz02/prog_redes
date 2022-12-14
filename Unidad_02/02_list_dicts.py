# Create a list of the BRICS countries
country = [ 
            "Brazil", 
            "Russia", 
            "India", 
            "China", 
            "South Africa"
          ]

"""Create a dictionary of BRICS capitals.
Note that South Africa has 3 capitals. Therefore, we embed a list inside
the dictionary.
"""

capitals = {
    "Brazil": "Brasilia",
    "Russia": "Moscow",
    "India": "New Delhi",
    "China": "Beijing",
    "South Africa": [
                        "Pretoria",
                        "Cape Town",
                        "Bloemfontein"
                    ]
           }

# Print the list and dictionary
print("Countrys: ")
print('\n'.join(country))

print("Capitals: ")
print('\n'.join(capitals) )
"""
What response did you get?
Why did the list and dictionary contents not print?
Fix the code and run the script again.
"""

print( "South Africa: ",'\n'.join(capitals["South Africa"]) )
"""
Why did you get an error for the 2nd capital of South Africa?
Hint: Check the syntax for the index value.
"""