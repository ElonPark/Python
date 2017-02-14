# 파이썬 유니코드
def unicode_test(value):
    import unicodedata
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print('value = "%s", name = "%s", lookup = "%s"' %(value, name, value2))


unicode_test('A')
unicode_test('$')
unicode_test('\u00a2')
unicode_test('\u20ac')
unicode_test('\u2603')
unicode_test('\u00e9')
print('caf\u00e9')
