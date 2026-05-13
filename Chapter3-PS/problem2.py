letter = ''' Dear <|Name|>,
    You are selected!
    <|Date|>'''

print(letter.replace("<|Name|>","Abhishek").replace("<|Date|>","24 April 2026"))