class ChaiUtils:
    @staticmethod
    def clan_Ingredients(text):
       return [i.strip() for i in text.split(',')]
       
raw = "water, milk,      honey     , ginger "
cleaned = ChaiUtils.clan_Ingredients(raw)
print(cleaned)