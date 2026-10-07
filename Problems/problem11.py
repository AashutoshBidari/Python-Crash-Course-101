# write code to fill in the letter templete given

letter = ''' Dear <|Name|>, 
 You are selected!
    <|Date|>'''


print(letter.replace("<|Name|>", "Joseph").replace("<|Date|>", "9 Sep, 9999"))
