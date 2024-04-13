class Animal:
    this_is_a_property = {
        'key_1':'value 1'
    }
    this_list = ['kailash', 'karan', 'komal', 'arun']

    def this_is_a_method(self):
        print(self.this_list)

    @property
    def get_gully(self):
        return self.this_list[3]

    def add_name(self, name):
        self.this_list.append(name)
        return self.this_list

the_animal = Animal()
the_animal.this_is_a_method()

gully = the_animal.get_gully
print("this is index name is", gully)

the_animal.add_name("madhu")
print(the_animal.this_list)