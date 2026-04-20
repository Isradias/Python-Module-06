from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed: list[str] = dark_spell_allowed_ingredients()
    ingredients = ingredients.replace("and", ",")
    ingredients_list: list[str] = ingredients.split(",")
    ingredients_list = [x.lower().strip() for x in ingredients_list]
    sentence: str = " - INVALID"
    for x in ingredients_list:
        if x in allowed:
            sentence = " - VALID"
    ingredients_list[0] = ingredients_list[0].capitalize()
    to_return: str = "and ".join(ingredients_list)
    to_return = to_return.replace("and ", ", ", len(ingredients_list) - 1)
    to_return += sentence
    return to_return
