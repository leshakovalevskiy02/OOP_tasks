class HistoryDict:
    def __init__(self, data=None):
        """
        self.data - хранит переданный словарь
        self.history_data - хранит словарь со всеми изменениями значений по ключу
        """
        self.data = {} if data is None else dict(data)
        self.history_data = {key: [self.data[key]] for key in self.data}
        
    def keys(self):
        return self.data.keys()
    
    def values(self):
        return self.data.values()
    
    def items(self):
        return self.data.items()
    
    def history(self, key):
        return self.history_data.get(key, [])
    
    def all_history(self):
        return self.history_data
    
    def __len__(self):
        return len(self.data)
      
    def __iter__(self):
        yield from self.data

    def __getitem__(self, key):
        return self.data[key]
    
    def __delitem__(self, key):
        self.data.pop(key)
        self.history_data.pop(key)
        
    def __setitem__(self, key, value):
        self.data[key] = value
        self.history_data[key] = self.history_data.get(key, []) + [value]

# TEST_1:
historydict = HistoryDict({'ducks': 99, 'cats': 1})

print(historydict['ducks'])
print(historydict['cats'])
print(len(historydict))

# TEST_2:
historydict = HistoryDict({'ducks': 99, 'cats': 1})

print(*historydict)
print(*historydict.keys())
print(*historydict.values())
print(*historydict.items())

# TEST_3:
historydict = HistoryDict({'ducks': 99, 'cats': 1})

historydict['ducks'] = 100
print(historydict.history('ducks'))
print(historydict.history('cats'))
print(historydict.history('dogs'))

# TEST_4:
historydict = HistoryDict({'ducks': 99, 'cats': 1})

print(historydict.all_history())
historydict['ducks'] = 100
historydict['ducks'] = 101
historydict['cats'] = 2
print(historydict.all_history())

# TEST_5:
historydict = HistoryDict({'ducks': 99, 'cats': 1})

historydict['dogs'] = 1
print(len(historydict))
del historydict['ducks']
del historydict['cats']
print(len(historydict))