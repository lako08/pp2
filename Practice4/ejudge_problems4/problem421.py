import importlib

q = int(input().strip())

for _ in range(q):
    module_path, attr = input().strip().split()
    
    try:
        module = importlib.import_module(module_path)
    except ImportError:
        print("MODULE_NOT_FOUND")
        continue
    
    if not hasattr(module, attr):
        print("ATTRIBUTE_NOT_FOUND")
        continue
    
    attr_value = getattr(module, attr)
    if callable(attr_value):
        print("CALLABLE")
    else:
        print("VALUE")