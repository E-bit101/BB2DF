import json

def parse_json(json_str, scale):
    data = json.loads(json_str)
    elements = data['elements']
    result = []

    for e in elements:
        name = e['name']
        x_from, y_from, z_from = e['from']
        x_to, y_to, z_to = e['to']
        x_to -= x_from
        y_to -= y_from
        z_to -= z_from
        xrotation, yrotation, zrotation = e.get('rotation', [0, 0, 0])
        xorigin, yorigin, zorigin = e['origin']
        xrotation = round(xrotation * scale,3) 
        yrotation = round(yrotation * scale,3) 
        zrotation = round(zrotation * scale,3) 
        x_from = round(x_from * scale,3) 
        y_from = round(y_from * scale,3) 
        z_from = round(z_from * scale,3) 
        x_to = round(x_to * scale,3) 
        y_to = round(y_to * scale,3) 
        z_to= round(z_to * scale,3) 
        object = str(x_from) + "/" + str(y_from) + "/" + str(z_from) + "/" + str(xrotation) + "/" + str(yrotation) + "/" + str(zrotation) + "/" + str(x_to) + "/" + str(y_to) + "/" + str(z_to) + "/" + name
        result.append(object)
    return result

jsoninput = input("Code here")
scale = float(input("Scale factor"))
input("~".join(parse_json(jsoninput,scale)))
