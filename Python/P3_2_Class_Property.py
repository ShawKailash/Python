class Animal:
    this_is_a_property = {
        'key_1':'value 1'
    }
    this_list = ['kailash', 'karan', 'komal', 'arun']

    _like_this = "this is a private property"

the_animal = Animal()

print(the_animal.this_is_a_property)

print(the_animal.this_is_a_property['key_1'])

print(the_animal.this_list)

print(the_animal.this_list[2])

print(Animal.this_list)

print(Animal._like_this)

print(the_animal._like_this)

