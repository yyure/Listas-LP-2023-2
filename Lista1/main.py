import data
import utils

people_data = data.people_data

print(people_data)

utils.add_person(people_data , 'Nome', 100, [])
print(people_data)

print(utils.remove_person(people_data, 'Alice'))

print(utils.get_ages(people_data))

print(utils.get_hobbies(people_data))

print(utils.get_people_by_hobbies(people_data, ['hiking']))

print(utils.match_people(people_data))