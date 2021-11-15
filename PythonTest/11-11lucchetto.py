def gen_pwds(symbols: str, n: int) -> [str]:
    if n == 0:
        return [""]
    result = []
    for v1 in symbols:
        for v2 in symbols:
            for v3 in symbols:
                combo = v1 + v2 + v3
                result.append(combo)
    return result