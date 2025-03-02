class MutableString:
    def __init__(self, string=""):
        self.string = string
        
    def lower(self):
        self.string = self.string.lower()
        
    def upper(self):
        self.string = self.string.upper()
        
    def __str__(self):
        return self.string
    
    def __repr__(self):
        return f"MutableString('{self.string}')"
    
    def __len__(self):
        return len(self.string)
    
    def __iter__(self):
        yield from self.string
        
    def __add__(self, other):
        """Операция + для экземпляров MutableString"""
        if isinstance(other, MutableString):
            return MutableString(self.string + other.string)
        return NotImplemented
        
    def __getitem__(self, key):
        return MutableString(self.string[key])
    
    def __setitem__(self, key, value):
        lst = list(self.string)
        lst[key] = value
        self.string = "".join(lst)
        
    def __delitem__(self, key):
        lst = list(self.string)
        del lst[key]
        self.string = "".join(lst)
            
# TEST_1:
mutablestring = MutableString('beegeek')

print(*mutablestring)
print(str(mutablestring))
print(repr(mutablestring))

# TEST_2:
mutablestring = MutableString('Beegeek')

mutablestring.lower()
print(mutablestring)
mutablestring.upper()
print(mutablestring)

# TEST_3:
mutablestring1 = MutableString('bee')
mutablestring2 = MutableString('geek')

print(mutablestring1 + mutablestring2)
print(mutablestring2 + mutablestring1)

# TEST_4:
mutablestring = MutableString('beegeek')

print(mutablestring)
mutablestring[0] = 'B'
mutablestring[-4] = 'G'
print(mutablestring)

# TEST_5:
mutablestring = MutableString('beegeek')

s1 = mutablestring[2:]
s2 = mutablestring[:5]
s3 = mutablestring[2:5:2]

print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))

# TEST_6:
mutablestring = MutableString('Ada Wong')
id1 = id(mutablestring)

mutablestring.upper()
id2 = id(mutablestring)

print(id1 == id2)

# TEST_7:
mutablestring = MutableString('beegeek')

del mutablestring[2:5]
del mutablestring[1:5:2]
print(mutablestring)

# TEST_8:
mutablestring = MutableString('beegeek')

mutablestring[-1] = 'ee'
print(mutablestring)

mutablestring[-2:] = 'geek'
print(mutablestring)

# TEST_9:
mutablestring = MutableString('beegeek')

del mutablestring[1:3]
print(mutablestring)

# TEST_10:
mutablestring1 = MutableString('bee')
mutablestring2 = MutableString('geek')

concat = mutablestring1 + mutablestring2
slicing = mutablestring1[1:2]
plus_indexing = mutablestring2[1]
minus_indexing = mutablestring2[-1]

print(type(concat))
print(type(slicing))
print(type(plus_indexing))
print(type(minus_indexing))