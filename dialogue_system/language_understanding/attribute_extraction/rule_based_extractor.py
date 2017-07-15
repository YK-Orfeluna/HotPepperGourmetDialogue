from rule_based_extractor import RuleBasedAttributeExtractor

extractor = RuleBasedAttributeExtractor()
attribute = extractor.extract(text='ラーメンを食べたい')
print(attribute)
>>> {'LOCATION': '', 'GENRE': 'ラーメン', 'MAXIMUM_AMOUNT': ''}