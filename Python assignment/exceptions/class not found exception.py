try:
    from non_existent_module import NonExistentClass
except ImportError as e:
    print(f"ClassNotFoundException: {e}")
