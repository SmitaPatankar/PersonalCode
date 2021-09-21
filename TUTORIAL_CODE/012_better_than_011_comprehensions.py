a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = [x**2 for x in a if x % 2 == 0]
print(even_squares)  # [4, 16, 36, 64, 100]

chile_ranks = {'ghost': 1, 'habanero': 2, 'cayenne': 3}
rank_dict = {rank: name for name, rank in chile_ranks.items()}
chile_len_set = {len(name) for name in rank_dict.values()}
print(rank_dict)  # {1: 'ghost', 2: 'habanero', 3: 'cayenne'}
print(chile_len_set)  # {8, 5, 7}
