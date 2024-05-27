def calculate_structure_sum(value_):
    res= 0
    if value_:
        if isinstance(value_, str):
            res+= len(value_)
        elif isinstance(value_, int) or isinstance(value_, float) or isinstance(value_, bool):
            res+= value_
        elif isinstance(value_, list) or isinstance(value_, tuple) or isinstance(value_, set):
            for i in value_:
                res+= calculate_structure_sum(i)
        elif isinstance(value_, dict) :
            for key, i in value_.items():
                res+= calculate_structure_sum(i)
                res+= calculate_structure_sum(key)
    else:
        res= 0
    return res

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
