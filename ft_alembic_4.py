import alchemy

print("=== Alembic 4 ===")
print("Accessing the alchemy module using 'import alchemy'")
print("Testing create_air: " + alchemy.create_air())

try:
    print("Testing create_earth:" + alchemy.create_earth())
except Exception as e:
    print(f"Catch {e.__class__.__name__}: {e}")
