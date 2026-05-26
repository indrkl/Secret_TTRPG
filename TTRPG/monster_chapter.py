from rulebook_chapters.character_creation import get_playcard_flowable
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

    elements.append({'type': 'minortitle', 'content': 'Playcards'})
    for playcard in ['acquainted', 'adept', 'talented', 'legendary']:
        if hasattr(monsters, '%s_card'%(playcard)):
            elements.append({'type': 'flowables', 'content': get_playcard_flowable(
                getattr(monsters, '%s_card'%(playcard)))
                             })
    elements.append({'type': 'minortitle', 'content': 'Feats'})

    for feat in monsters.feats:
        elements.append({'type': 'flowables', 'content': prep_feat_flowable(feat)})

    return elements



def get_monsters_chapters():

    elements = [
        {'type': 'title', 'content': 'None humanoid creatures'},
        {'type': 'paragraph', 'content': '''
None humanoid creatures (beasts, monsters, undead) can be created similarly like player characters. Only difference is 
that they have their own base archetypes, with custom features, kinda like having innate feats and then they have a 
path, with it's own feats and advancement options. This is more to create epic monsters, but ideas can also be gotten
for mob monsters.      
        '''},
    ]
    elements.extend(get_monster_chapter(beasts, 'Beasts'))
    # elements.extend(get_monster_chapter(undead, 'Undead'))

    return elements