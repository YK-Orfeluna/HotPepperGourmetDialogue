from rule_based_extractor import RuleBasedAttributeExtractor
from rule_based_estimator import RuleBasedDialogueActTypeEstimator

extractor = RuleBasedAttributeExtractor()
estimator = RuleBasedDialogueActTypeEstimator()
attribute = extractor.extract(text='ラーメンを食べたい')
act_type = estimator.estimate(attribute)
print(act_type)
>>> 'INFORM_GENRE'