import inspect

def introspection_info(obj):
    type_ = type(obj)
    attributes = []
    methods = []
    for i in dir(obj):
        if '__' not in i:
            attributes.append(i)
        else:
            methods.append(i)
    module = __name__
    info = {f"type: {type_}, attributes: {attributes}, methods: {methods}, modele: {module}"}
    return info



number_info = introspection_info(42)
print(number_info)
