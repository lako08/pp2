import json

def apply_patch(source, patch):
    result = source.copy() if isinstance(source, dict) else source
    
    for key, value in patch.items():
        if value is None:
            if key in result:
                del result[key]
        elif key not in result:
            result[key] = value
        elif isinstance(result.get(key), dict) and isinstance(value, dict):
            result[key] = apply_patch(result[key], value)
        else:
            result[key] = value
    
    return result

source = json.loads(input().strip())
patch = json.loads(input().strip())

patched = apply_patch(source, patch)

print(json.dumps(patched, sort_keys=True, separators=(',', ':')))