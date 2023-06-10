from monsters import beasts, undead
from Normal_feats import prep_feat_flowable

def get_monster_chapter(monsters, monster_name):
    elements = [
        {'type': 'subtitle', 'content': monster_name},
    ]

    if hasattr(monsters, 'info'):
        for info in monsters.info:
            elements.append({'type': 'paragraph', 'content': info})

    elements.append({'type': 'minortitle', 'content': 'Archetypes'})
    for archetype in monsters.archetypes:
        elements.append({'type': 'minortitle', 'content': archetype['name']})
        elements.append({'type': 'paragraph', 'content': archetype['description']})

    elements.append({'type': 'minortitle', 'content': 'Advancement options'})
    elements.append({'type': 'list', 'content': monsters.advancement_options})

    for feat in monsters.feats:
        elements.append({'type': 'flowables', 'content': prep_feat_flowable(feat)})

    return elements



def get_monsters_chapters():

    elements = [
        {'type': 'title', 'content': 'None humanoid creaters'},
        {'type': 'paragraph', 'content': '''
None humanoid creatures (beasts, monsters, undead) are created similarly like player characters. Only difference is that
they have their own base archetypes, with custom features, kinda like having innate feats and then they have a path,
with it's own feats and advancement options. Note that when looking at the HP per level, then first level still has the
3 times multiplier similarly to player characters.        
        '''},
    ]
    elements.extend(get_monster_chapter(beasts, 'Beasts'))
    # elements.extend(get_monster_chapter(undead, 'Undead'))

    return elements