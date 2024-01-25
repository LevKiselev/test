def nop(*rest, **kwargs):
    print(rest)
    print(kwargs)

# nop()
nop("Любое", "сказанное", "вами слово", "будет проигнорировано", w='test')
# nop(100500, None, [1, 2, 3, 4, 5])
