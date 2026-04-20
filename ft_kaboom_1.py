
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

    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    from alchemy.grimoire.dark_spellbook import dark_spell_record
    for spell in book:
        print(f"  Testing record {spell} spell: ", end="")
        response = dark_spell_record(spell, book[spell])
        if response.find("INVALID") != -1:
            print(f"Spell failed to record: {response}")
        else:
            print(f"Spell recorded: {response}")
