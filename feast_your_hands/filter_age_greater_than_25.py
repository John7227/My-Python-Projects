def select_age_greater_than_25(ages_greater_than_25):

    return ages_greater_than_25["age"] > 25

def get_result(age):

    return list(filter(select_age_greater_than_25, age))



age = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 20}]

print(get_result(age))
