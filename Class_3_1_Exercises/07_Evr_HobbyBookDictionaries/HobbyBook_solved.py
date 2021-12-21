# @TODO: Your code here
pet_dict = {"name": "Zeus", 
    "age": 12,
    "hobbies": ["playing ball", "running", "mooching food"],
    "wake_up": {"Sunday":"9am", "Monday":"6am", "Tuesday":"6am", "Wednesday":"6am", "Thursday":"6am", "Friday":"6am", "Saturday":"7am"}}


message = (
    f"My pet's name is {pet_dict['name']} and he is {pet_dict['age']} years old.\n"
    f"He has {len(pet_dict['hobbies'])} hobbies and his favourite is {pet_dict['hobbies'][0]}.\n"
    f"On Sundays he wakes up at {pet_dict['wake_up']['Sunday']}")

print(message)