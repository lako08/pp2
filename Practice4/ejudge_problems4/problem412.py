import json

def compare_objects(obj1, obj2, path=""):
    differences = []
    
    keys1 = set(obj1.keys()) if isinstance(obj1, dict) else set()
    keys2 = set(obj2.keys()) if isinstance(obj2, dict) else set()
    
    if isinstance(obj1, dict) and isinstance(obj2, dict):
        for key in keys1.union(keys2):
            new_path = f"{path}.{key}" if path else key
            
            if key not in obj1:
                val2 = json.dumps(obj2[key], separators=(',', ':'))
                differences.append(f"{new_path} : <missing> -> {val2}")
            elif key not in obj2:
                val1 = json.dumps(obj1[key], separators=(',', ':'))
                differences.append(f"{new_path} : {val1} -> <missing>")
            else:
                if isinstance(obj1[key], dict) and isinstance(obj2[key], dict):
                    differences.extend(compare_objects(obj1[key], obj2[key], new_path))
                elif obj1[key] != obj2[key]:
                    val1 = json.dumps(obj1[key], separators=(',', ':'))
                    val2 = json.dumps(obj2[key], separators=(',', ':'))
                    differences.append(f"{new_path} : {val1} -> {val2}")
    else:
        if obj1 != obj2:
            val1 = json.dumps(obj1, separators=(',', ':'))
            val2 = json.dumps(obj2, separators=(',', ':'))
            differences.append(f"{path} : {val1} -> {val2}")
    
    return differences

obj_a = json.loads(input().strip())
obj_b = json.loads(input().strip())

result = compare_objects(obj_a, obj_b)
result.sort()

if result:
    for line in result:
        print(line)
else:
    print("No differences")