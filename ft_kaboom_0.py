from alchemy.grimoire import light_spell_record
from alchemy.grimoire import light_spell_allowed_ingredients

if __name__ == "__main__":
    book = {
        "Flame Burst": "fire, sulfur, charcoal",
        "Tidal Wave": "water, salt, moonstone",
        "Stone Skin": "earth, clay, iron",
        "Wind Whisper": "air, feather, dust",
        "Shadow Bind": "ink, obsidian, nightshade",
        "Healing Light": "herbs, honey, sunlight",
        "Arcane Blast": "crystal, mana, ash",
        "Forest Call": "earth, leaves, sap",
        "Storm Eye": "air, water, lightning_essence",
        "Ember Touch": "fire, oil, spice"
    }

    print("=== Kaboom 0 ===")
    print("Using grimoire module directly\n")
    print(f"Valid ingredients: {light_spell_allowed_ingredients()}")
    for spell in book:
        print(f"  Testing record {spell} spell: ", end="")
        response = light_spell_record(spell, book[spell])
        if response.find("INVALID") != -1:
            print(f"Spell failed to record: {response}")
        else:
            print(f"Spell recorded: {response}")
