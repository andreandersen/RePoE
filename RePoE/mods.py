from PyPoE.poe.constants import MOD_DOMAIN
from RePoE.util import write_json, call_with_default_args


def _convert_stats(stats):
    # 'Stats' is a virtual field that is an array of ['Stat1', ..., 'Stat5'].
    # 'Stat{i}' is a virtual field that is an array of ['StatsKey{i}', 'Stat{i}Min', 'Stat{i}Max']
    r = []
    for stat in stats:
        if stat[0] is not None:
            r.append({
                'id': stat[0]['Id'],
                'min': stat[1],
                'max': stat[2]
            })
    return r


def _convert_spawn_weights(spawn_weights):
    # 'SpawnWeight' is a virtual field that is a tuple of ('SpawnWeight_TagsKeys', 'SpawnWeight_Values')
    r = []
    for tag, value in spawn_weights:
        r.append({
            'id': tag['Id'],
            'value': value
        })
    return r


def _convert_generation_weights(generation_weights):
        # 'GenerationWeight' is an array of arrays with two elements where the first contains
        # the id, and the second the value
    r = []
    ids = generation_weights[0]
    vals = generation_weights[1]
    for idx, id in enumerate(ids):
        r.append({
            'id': id['Id'],
            'value': vals[idx]
        })
    return r


def _convert_buff(buff_definition, buff_value):
    if buff_definition is None:
        return {}
    return {
        'id': buff_definition['Id'],
        'range': buff_value
    }


def _convert_granted_effects(granted_effects_per_level):
    if granted_effects_per_level is None:
        return {}
    # These two identify a row in GrantedEffectsPerLevel.dat
    return {
        'granted_effect_id': granted_effects_per_level['GrantedEffectsKey']['Id'],
        'level': granted_effects_per_level['Level']
    }


def _convert_tags_keys(tags_keys):
    r = []
    for tag in tags_keys:
        r.append(tag['Id'])
    return r


def ignore_mod_domain(domain):
    return domain is not MOD_DOMAIN.ITEM and domain is not MOD_DOMAIN.FLASK and domain is not MOD_DOMAIN.MASTER\
        and domain is not MOD_DOMAIN.JEWEL and domain is not MOD_DOMAIN.ATLAS


# todo enable when useful
# ignored information about mods:
# - GenerationWeight_{TagsKeys, Values} (changes mod spawning weight when the item has specific tags, e.g. those above)
# ignored mods:
# - domain of 'monster', 'chest', 'area', 'stance', 'atlas', 'leaguestone'
def write_mods(data_path, relational_reader, **kwargs):
    root = {}
    for mod in relational_reader['Mods.dat']:
        domain = MOD_DOMAIN_FIX.get(mod['Id'], mod['Domain'])
        if ignore_mod_domain(domain):
            continue
        obj = {
            'required_level': mod['Level'],
            'stats': _convert_stats(mod['Stats']),
            'domain': domain.name.lower(),
            'name': mod['Name'],
            'generation_type': mod['GenerationType'].name.lower(),
            'group': mod['CorrectGroup'],
            'spawn_tags': _convert_spawn_weights(mod['SpawnWeight']),
            'grants_buff': _convert_buff(mod['BuffDefinitionsKey'], mod['BuffValue']),
            'grants_effect': _convert_granted_effects(mod['GrantedEffectsPerLevelKey']),
            'is_essence_only': mod['IsEssenceOnlyModifier'] > 0,
            'adds_tags': _convert_tags_keys(mod['TagsKeys']),
            'generation_weights': _convert_generation_weights(mod['GenerationWeight'])
        }
        if mod['Id'] in root:
            print("Duplicate mod id:", mod['Id'])
        else:
            root[mod['Id']] = obj

    write_json(root, data_path, 'mods')


# a few unique item mods have the wrong mod domain so they wouldn't be added to the file without this
MOD_DOMAIN_FIX = {
    "AreaDamageUniqueBodyDexInt1": MOD_DOMAIN.ITEM,
    "ElementalResistancePerEnduranceChargeDescentShield1": MOD_DOMAIN.ITEM,
    "LifeGainOnEndurangeChargeConsumptionUniqueBodyStrInt6": MOD_DOMAIN.ITEM,
    "ReturningProjectilesUniqueDescentBow1": MOD_DOMAIN.ITEM,
}


if __name__ == '__main__':
    call_with_default_args(write_mods)
