def greatest(data: list) -> str:
    max_ = ""
    for v in data:
        if isinstance(v, list):
            name = greatest(v)
        else:
            name = v
        if name >= max_:
            max_ = name
    return max_

values = ["Ann", ["Bart", ["Carol", "Cindy"], "Bob", "Art"], ["Bea"], "Bill"]
g = greatest(values)
print(g)