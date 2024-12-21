def id_generator(starting_id: int = 0):
    id = starting_id
    def generate_next_id():
        nonlocal id
        id += 1
        return id
    return generate_next_id
