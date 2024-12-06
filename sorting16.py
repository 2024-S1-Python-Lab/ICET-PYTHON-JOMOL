my_dict={'banana':3,'apple':1,'cherry':2,'dates':4}
print("Orginal list:",my_dict)
asorted_dict=dict(sorted(my_dict.items()))
print("Ascending order:",asorted_dict)
dsorted_dict=dict(sorted(my_dict.items(),reverse=True))
print("DEscending order:",dsorted_dict)
