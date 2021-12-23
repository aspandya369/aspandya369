mini_dict = {}
for char in range(97,123):
    mini_dict.setdefault(chr(char),char)
print(mini_dict)
