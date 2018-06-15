import resource
import random
import time

names = ['rahul', 'John', 'Reshmi', 'Parvati', 'Kevin']
majors = ['Computer', 'Electrical', 'Electronics', 'TeleComm', 'Mathematics']

print("Before Execution Memory Usage: ", resource.getrusage(resource.RUSAGE_SELF))


def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
            }
        result.append(person)
    return result


def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
            }
    yield person


# Using List
# t1 = time.time()
# result = people_list(1000000)
# print("After Execution Memory Usage: ", resource.getrusage(resource.RUSAGE_SELF))
# t2 = time.time()
# print("Total Time Take: ", (t2-t1))

# Using Generators
t1 = time.time()
res = people_generator(1000000)
print("After Execution Memory Usage: ", resource.getrusage(resource.RUSAGE_SELF))
t2 = time.time()
print("Total Time Take: ", (t2-t1))