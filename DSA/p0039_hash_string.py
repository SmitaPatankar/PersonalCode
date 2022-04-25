def hash_str(a_string, table_size):
    return sum([ord(c) for c in a_string]) % table_size


print(hash_str("cat", 11))
print(hash_str("tac", 11))


def hash_str(a_string, table_size):
    return sum([i * ord(c) for i, c in enumerate(a_string, 1)]) % table_size


print(hash_str("cat", 11))
print(hash_str("tac", 11))
