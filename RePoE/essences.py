from PyPoE.poe.constants import MOD_DOMAIN
from RePoE.util import write_json, call_with_default_args

def get_maybe_key(mod):
    return None if mod is None else mod['Id']

def write_essences(data_path, relational_reader, **kwags):
    root = []
    for e in relational_reader['Essences.dat']:
        obj = {
            'id': e['BaseItemTypesKey']['Id'],
            'name': e['BaseItemTypesKey']['Name'],
            'drop_level': e['BaseItemTypesKey']['DropLevel'],
            'item_classes': {
                'Amulet': get_maybe_key(e['Amulet2_ModsKey']),
                'Ring': get_maybe_key(e['Ring_ModsKey']),
                'Belt': get_maybe_key(e['Belt2_ModsKey']),
                'Quiver': get_maybe_key(e['Quiver_ModsKey']),
                'Helmet': get_maybe_key(e['Helmet2_ModsKey']),
                'Body Armour': get_maybe_key(e['BodyArmour2_ModsKey']),
                'Boots': get_maybe_key(e['Boots2_ModsKey']),
                'Gloves': get_maybe_key(e['Gloves2_ModsKey']),
                'Shield': get_maybe_key(e['Shield2_ModsKey']),
                'Bow': get_maybe_key(e['Bow_ModsKey']),
                'Claw': get_maybe_key(e['1Hand_ModsKey2']),
                'Dagger': get_maybe_key(e['1Hand_ModsKey2']),
                'Staff': get_maybe_key(e['2Hand_ModsKey2']),
                'Wand': get_maybe_key(e['Wand_ModsKey']),
                'One Hand Axe': get_maybe_key(e['1Hand_ModsKey2']),
                'One Hand Mace': get_maybe_key(e['1Hand_ModsKey2']),
                'One Hand Sword': get_maybe_key(e['1Hand_ModsKey2']),
                'Sceptre': get_maybe_key(e['1Hand_ModsKey2']),
                'Thrusting One Hand Sword': get_maybe_key(e['1Hand_ModsKey2']),
                'Two Hand Axe': get_maybe_key(e['2Hand_ModsKey2']),
                'Two Hand Mace': get_maybe_key(e['2Hand_ModsKey2']),
                'Two Hand Sword': get_maybe_key(e['2Hand_ModsKey2']),
            }
        }
        root.append(obj)
    write_json(root, data_path, 'essences')

if __name__ == '__main__':
    call_with_default_args(write_essences)