from RePoE.util import write_json, call_with_default_args

def write_items(data_path, relational_reader, **kwargs):
    """Writes items to json file"""
    base_items = relational_reader['BaseItemTypes.dat']
    attr_req = dict((x['BaseItemTypesKey']['Id'], x) for x in (y for y in relational_reader['ComponentAttributeRequirements.dat'] if y['BaseItemTypesKey'] != None))    
    armour_stats = dict((x['BaseItemTypesKey']['Id'], x) for x in relational_reader['ComponentArmour.dat'])
    shield_stats = dict((x['BaseItemTypesKey']['Id'], x) for x in relational_reader['ShieldTypes.dat'])
    weapon_stats = dict((x['BaseItemTypesKey']['Id'], x) for x in relational_reader['WeaponTypes.dat'])

    root = {}
    for it in base_items:
        attr = attr_req.get(it['Id'])
        armour = armour_stats.get(it['Id'])
        shield = shield_stats.get(it['Id'])
        weapon = weapon_stats.get(it['Id'])
        obj = {
            'id': it['Id'],
            'name': it['Name'],
            'class' : {
                'id': it['ItemClassesKey']['Id'],
                'name': it['ItemClassesKey']['Name'],
                'category': it['ItemClassesKey']['Category']
            },
            'width': it['Width'],
            'height': it['Height'],
            'inherits_from': it['InheritsFrom'],
            'drop_level': it['DropLevel'],
            'implicits': list(map(lambda x: x['Id'], it['Implicit_ModsKeys'])),
            'tags': list(map(lambda x: x['Id'], it['TagsKeys'])),
            'visual_identity': {
                'id': it['ItemVisualIdentityKey']['Id'],
                'dds': it['ItemVisualIdentityKey']['DDSFile'],
                'is_alternate_art': it['ItemVisualIdentityKey']['IsAlternateArt']
            },
            'is_picked_up_by_monsters': it['IsPickedUpByMonsters'],
            'armour_stats': None if armour is None else {
                'armour': armour['Armour'],
                'evasion': armour['Evasion'],
                'energy_shield': armour['EnergyShield']
            },
            'attribute_requirements': None if attr is None else {
                'str': attr['ReqStr'],
                'dex': attr['ReqDex'],
                'int': attr['ReqInt']
            },
            'shield_stats': None if shield is None else {
                'block': shield['Block']
            },
            'weapon_stats': None if weapon is None else {
                'crit': weapon['Critical'],
                'aps': 0 if weapon['Speed'] is 0 else 1000 / weapon['Speed'],
                'dmg_min': weapon['DamageMin'],
                'dmg_max': weapon['DamageMax'],
                'range': weapon['RangeMax'],
                'null6': weapon['Null6']
            }
        }
        root[obj['id']] = obj

    write_json(root, data_path, 'items')

if __name__ == '__main__':
    call_with_default_args(write_items)
