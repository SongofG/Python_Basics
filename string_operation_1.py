>>> ## Q1)
>>> str = "The Espresso Spirit"
>>> str.upper() # 전부 다 대문자.
'THE ESPRESSO SPIRIT'
>>> str.lower() # 전부 다 소문자.
'the espresso spirit'
>>> 
>>> ## Q2)
>>> def birth_only(str):
	return str.split('-')[0]

>>> p1 = "070609-2011xxx"
>>> birth_only(p1)
'070609'
>>> 