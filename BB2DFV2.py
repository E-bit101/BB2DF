import json
import time
def importmodules():
    try:
        import pygame as pg
        import keyboard as kb
    except:
        input("Modules failed to import. Please run the following commands in your console: [pip install pygame] and [pip install keyboard]. Press enter to continue.")
        importmodules()
importmodules()
import keyboard as kb
import random
print("Better UI coming soon!")

def macro(Json):
    kb.press_and_release("enter")
    kb.press_and_release("t")
    time.sleep(0.1)
    kb.write("/rc")
    kb.press_and_release("enter")
    kb.press_and_release("1")
    kb.press_and_release("t")
    time.sleep(0.3)
    kb.write("/i get armor_stand")
    kb.press_and_release("enter")
    offsetnum = [0.3,0.5,0.9,0.4,0.1,0.6,1]
    for i in range(len(Json)):
        kb.press_and_release("t")
        time.sleep(2 + (offsetnum[i % len(offsetnum)]))
        kb.write("/i lore add " + str(Json[i]))
        kb.press_and_release("enter")

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
inp = input("Automatically input values? Y/N")
if (inp == "Y" or inp == "y"):
    input("After pressing enter, this program will wait 10 seconds which you should use to switch to minecraft and go to your codespace. After those 10 seconds it will do /rc and setup the model. Press enter to continue.")
    time.sleep(10)
    macro(parse_json(jsoninput,scale))
else:
    input("(newline)".join(parse_json(jsoninput,scale)))
