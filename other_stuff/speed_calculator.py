

def calc_sequence(speeds, abilities, turn_meter_per_speed=0.066 / 100, debug=False):
    current_turn_meter = [0 for _ in speeds]
    speed_boosted = [0 for _ in speeds]

    for ability_key in abilities:
        for ability in abilities[ability_key]:
            ability['current_cooldown'] = ability.get('offset', 0)

    # Boss is last in priority
    priority_list = [i for i in range(1, len(speeds))] + [0]
    # print(priority_list)
    protected = False
    while True:
        next_actor = -1
        most_filled = 0.9

        for i in priority_list:
            speed = speeds[i]
            if speed_boosted[i] > 0:
                current_turn_meter[i] += speed * turn_meter_per_speed * 1.3
            else:
                current_turn_meter[i] += speed * turn_meter_per_speed

            if current_turn_meter[i] > most_filled:
                most_filled = current_turn_meter[i]
                next_actor = i

        if next_actor == -1:
            continue
        current_turn_meter[next_actor] = 0

        # Do judgments and actions based on next_actor.
        if debug:
            print([next_actor, protected, current_turn_meter, speed_boosted])

        yield next_actor, protected
        if next_actor != 0:
            protected = False

        if speed_boosted[next_actor] > 0:
            speed_boosted[next_actor] -= 1

        for ability in abilities.get(next_actor, []):
            ability['current_cooldown'] -= 1
            if ability['current_cooldown'] <= 0:
                ability['current_cooldown'] = ability['cooldown']
            else:
                continue
            for effect in ability['effects']:
                if debug:
                    print(effect)
                if effect == 'turn_meter_boost':
                    for i in range(1, len(speeds)):
                        current_turn_meter[i] += ability['value']
                if effect == 'speed_boost':
                    for i in range(1, len(speeds)):
                        speed_boosted[i] = max(speed_boosted[i], 2)
                if effect == 'prolong_buffs':
                    for i in range(1, len(speeds)):
                        if speed_boosted[i] > 0:
                            speed_boosted[i] += 1
                if effect == 'protect':
                    protected = True

            break

# Desired speeds are that speed 1 and 2 take turns being the last one from the boss.
def check_for_desired_sequence(speeds, abilities):
    boss_turn_count = 0



    current_turn_meter = [0 for _ in speeds]

    last_character = None

    previous_last_character = None

    turns_from_last = [0 for _ in speeds]

    for next_actor, protected in calc_sequence(speeds, abilities):
        if boss_turn_count >= 50:
            break

        if next_actor == 0:
            boss_turn_count += 1

            # print([boss_turn_count, last_character, previous_last_character])
            # Check that we are going smoothly between the characters.
            if not protected:
                if boss_turn_count > 1:
                    # All still good if it is first rounds
                    # print([boss_turn_count, speeds, last_character, previous_last_character] )
                    return boss_turn_count
            turns_from_last[last_character] = 0

            previous_last_character = last_character
            # apply maulie boost since boss attacks.

        else:
            last_character = next_actor
            turns_from_last[next_actor] += 1

    return 50


def get_sequence_for_speeds(speeds, abilities, turn_meter_per_speed, boss_turns=50):
    sequence = []
    current_boss_turn = 0
    for target in calc_sequence(speeds, abilities, turn_meter_per_speed):
        sequence.append(target)
        if target == 0:
            current_boss_turn += 1
        if current_boss_turn >= boss_turns:
            return sequence
    return sequence


def test_turn_meter_per_second(speeds, abilities, turn_meter_per_speed_samples):
    last_sequence = None
    last_turn_meter_per_second = None
    for turn_meter_per_speed in turn_meter_per_speed_samples:
        sequence = get_sequence_for_speeds(speeds, abilities, turn_meter_per_speed)
        if last_sequence is not None and last_sequence != sequence:
            print(last_turn_meter_per_second, turn_meter_per_speed, sequence, last_sequence)
            break
        last_sequence = sequence
        last_turn_meter_per_second = turn_meter_per_speed





def find_good_speeds(abilities, boss_speed):
    min_speed = int(boss_speed * 1.05)
    max_speed = int(boss_speed * 1.4)
    min_attack_speed = int(boss_speed * 0.95)

    max_support_speed = int(boss_speed * 1.4)

    best_turn_count = 0
    best_speeds = []

    all_good_speeds = []

    print([min_speed, max_speed])
    for speed_1 in range(min_attack_speed, max_speed + 1, 3):
        for speed_2 in range(min_attack_speed, max_speed + 1, 3):
            for speed_3 in range(min_speed, max_speed + 15, 3):
                for speed_4 in range(min_speed, max_speed + 15, 5):
                    for speed_5 in range(min_attack_speed, max_speed + 1, 5):
                        speeds = [speed_1, speed_2, speed_3, speed_4, speed_5]
                        turn_count = check_for_desired_sequence([boss_speed] + speeds, abilities)
                        if turn_count > best_turn_count or (turn_count == best_turn_count and speed_2 > best_speeds[1]) or turn_count == 50:
                            print([turn_count, speeds])
                            best_speeds = speeds
                            best_turn_count = turn_count
                            if turn_count == 50:
                                all_good_speeds.append(speeds)

    return best_turn_count, best_speeds


def test_speeds(speeds, abilities):
    indx = 0
    for _, _ in calc_sequence(speeds, abilities, debug=True):
        indx += 1
        if indx >= 100:
            break

# print(find_good_speeds(0, 170))
# print(find_good_speeds({
#     5: [{'effects': ['turn_meter_boost', 'speed_boost'], 'value': 0.15, 'cooldown': 3, 'offset': 0}
#         ],
#     3: [{'effects': ['protect'], 'cooldown': 3, 'offset': 0}, {'effects': ['prolong_buffs'], 'value': 1, 'cooldown': 4, 'offset': 0}],
#     4: [{'effects': ['protect'], 'cooldown': 3, 'offset': 2}, {'effects': ['prolong_buffs'], 'value': 1, 'cooldown': 4, 'offset': 0}]
# }, 190))
#
# print(find_good_speeds({
#     5: [{'effects': ['turn_meter_boost', 'speed_boost'], 'value': 0.15, 'cooldown': 3, 'offset': 0}
#         ],
#     3: [{'effects': ['protect'], 'cooldown': 3, 'offset': 0}, {'effects': ['prolong_buffs'], 'value': 1, 'cooldown': 4, 'offset': 2}],
#     4: [{'effects': ['protect'], 'cooldown': 3, 'offset': 2}, {'effects': ['prolong_buffs'], 'value': 1, 'cooldown': 4, 'offset': 0}]
# }, 190))

# print(find_good_speeds({
#     5: [{'effects': ['turn_meter_boost', 'speed_boost'], 'value': 0.15, 'cooldown': 3, 'offset': 0}
#         ],
#     3: [{'effects': ['protect'], 'cooldown': 3, 'offset': 0}],
#     4: [{'effects': ['protect'], 'cooldown': 3, 'offset': 2}]
# }, 190))

# test_speeds( [190, 180, 204, 199, 219, 255], {
#     5: [{'effects': ['turn_meter_boost', 'speed_boost'], 'value': 0.15, 'cooldown': 3, 'offset': 0}
#         ],
#     3: [{'effects': ['protect'], 'cooldown': 3, 'offset': 0}, {'effects': ['prolong_buffs'], 'value': 1, 'cooldown': 4, 'offset': 2}],
#     4: [{'effects': ['protect'], 'cooldown': 3, 'offset': 2}, {'effects': ['prolong_buffs'], 'value': 1, 'cooldown': 4, 'offset': 0}]
# })
test_speeds( [190, 180, 261, 280, 264, 265], {
    5: [{'effects': ['turn_meter_boost', 'speed_boost'], 'value': 0.15, 'cooldown': 3, 'offset': 0}
        ],
    3: [{'effects': ['protect'], 'cooldown': 3, 'offset': 0}, {'effects': ['prolong_buffs'], 'value': 1, 'cooldown': 4, 'offset': 2}],
    4: [{'effects': ['protect'], 'cooldown': 3, 'offset': 2}, {'effects': ['prolong_buffs'], 'value': 1, 'cooldown': 4, 'offset': 0}]
})

# print(find_good_speeds({}, 190))
# print(find_good_speeds({5: [{'key': 'turn_meter_boost', 'value': 0.2, 'cooldown': 3, 'offset': 0}]}, 170))
# print(find_good_speeds({}, 170))

# test_turn_meter_per_second([190, 257, 275, 275, 236, 176], {3: [{'key': 'turn_meter_boost', 'value': 0.2, 'cooldown': 3, 'offset': 0}]},
#                            [0.065 / 100, 0.066 / 100, 0.067 / 100, 0.068 / 100, 0.069 / 100, 0.07 / 100])

# print(check_for_desired_sequence([170, 257, 276, 166, 167, 168], 0))
# print(check_for_desired_sequence([190, 254, 270, 169, 168, 167], 0))
# print(check_for_desired_sequence([190, 254, 270, 169, 168, 167], 0.25))
# print(check_for_desired_sequence([170, 212, 297, 216], 0.25))
# print(check_for_desired_sequence([190, 212, 297, 216], 0.25))

# [50, [227, 257, 200, 226, 226]]
# [50, [227, 257, 203, 226, 226]]
# [50, [227, 257, 206, 226, 226]]
# [50, [227, 257, 209, 226, 226]]
# [50, [227, 257, 212, 226, 226]]
# [50, [227, 257, 215, 226, 226]]
# [50, [227, 257, 218, 226, 226]]
# [50, [227, 257, 227, 201, 226]]
# [50, [230, 257, 230, 201, 226]]
# [50, [242, 257, 233, 161, 161]]
# [50, [242, 257, 236, 161, 161]]
# [50, [242, 257, 239, 161, 161]]
# [50, [242, 257, 242, 166, 161]]
# [50, [245, 257, 245, 166, 161]]
# [50, [248, 257, 248, 166, 161]]
# [50, [257, 260, 260, 231, 176]]
# [50, [257, 263, 263, 231, 176]]
# [50, [257, 266, 266, 231, 176]]

# [190, 257, 275, 275, 236, 176]
# 0.00065 0.00066
# [2, 3, 1, 4, 5, 0, 2, 3, 1, 4, 2, 5, 3, 0, 1, 4, 2, 3, 5, 1, 0, 4, 2, 3, 1, 5, 4, 2, 3, 0, 1, 4, 2, 3, 5, 1, 0, 4, 2, 3, 1, 5, 4, 2, 0, 3, 1, 4, 2, 5, 3, 1, 0, 4, 2, 3, 5, 1, 4, 2, 0, 3, 1, 5, 4, 2, 3, 1, 0, 4, 2, 5, 3, 1, 4, 2, 0, 3, 1, 5, 4, 2, 3, 1, 0, 4, 2, 3, 5, 1, 4, 2, 3, 0, 1, 4, 2, 5, 3, 1, 0, 4, 2, 3, 5, 1, 4, 2, 0, 3, 1, 5, 4, 2, 3, 1, 0, 4, 2, 3, 5, 1, 4, 2, 0, 3, 1, 5, 4, 2, 3, 1, 0, 4, 2, 5, 3, 1, 4, 2, 0, 3, 1, 5, 4, 2, 3, 1, 0, 4, 2, 3, 5, 1, 4, 2, 3, 0, 1, 4, 2, 5, 3, 1, 0, 4, 2, 3, 5, 1, 4, 2, 0, 3, 1, 5, 4, 2, 3, 1, 0, 4, 2, 3, 5, 1, 4, 2, 0, 3, 1, 5, 4, 2, 3, 1, 0, 4, 2, 5, 3, 1, 4, 2, 0, 3, 1, 5, 4, 2, 3, 1, 0, 4, 2, 3, 5, 1, 4, 2, 3, 0, 1, 4, 2, 5, 3, 1, 0, 4, 2, 3, 5, 1, 4, 2, 0, 3, 1, 5, 4, 2, 3, 1, 0, 4, 2, 3, 5, 1, 4, 2, 0, 3, 1, 5, 4, 2, 3, 1, 0, 4, 2, 5, 3, 1, 4, 2, 0, 3, 1, 5, 4, 2, 3, 1, 0, 4, 2, 3, 5, 1, 4, 2, 3, 0, 1, 4, 2, 5, 3, 1, 0, 4, 2, 3, 5, 1, 4, 2, 0, 3, 1, 5, 4, 2, 3, 1, 0, 4, 2, 3, 5, 1, 4, 2, 0, 3, 1, 5, 4, 2, 3, 1, 0, 4, 2, 5, 3, 1, 4, 2, 0, 3, 1, 5, 4, 2, 3, 1, 0, 4, 2, 3, 5, 1, 4, 2, 3, 0, 1, 4, 2, 5, 3, 1, 0, 4, 2, 3, 5, 1, 4, 2, 0, 3, 1, 5, 4, 2, 3, 1, 0, 4, 2, 3, 5, 1, 4, 2, 0, 3, 1, 5, 4, 2, 3, 1, 0, 4, 2, 5, 3, 1, 4, 2, 0]
# [2, 3, 1, 4, 5, 0, 2, 3, 1, 4, 2, 3, 5, 0, 1, 4, 2, 3, 1, 5, 0, 2, 4, 3, 1, 2, 5, 4, 3, 0, 1, 2, 4, 3, 5, 1, 2, 0, 4, 3, 1, 2, 5, 4, 3, 0, 1, 2, 4, 3, 5, 1, 2, 0, 4, 3, 1, 2, 5, 4, 3, 0, 1, 2, 4, 3, 5, 1, 2, 0, 4, 3, 1, 2, 5, 4, 3, 0, 1, 2, 4, 3, 5, 1, 2, 0, 4, 3, 1, 2, 5, 4, 3, 0, 1, 2, 4, 3, 5, 1, 2, 0, 4, 3, 1, 2, 5, 4, 3, 0, 1, 2, 4, 3, 5, 1, 2, 0, 4, 3, 1, 2, 5, 4, 3, 0, 1, 2, 4, 3, 5, 1, 2, 0, 4, 3, 1, 2, 5, 4, 3, 0, 1, 2, 4, 3, 5, 1, 2, 0, 4, 3, 1, 2, 5, 4, 3, 0, 1, 2, 4, 3, 5, 1, 2, 0, 4, 3, 1, 2, 5, 4, 3, 0, 1, 2, 4, 3, 5, 1, 2, 0, 4, 3, 1, 2, 5, 4, 3, 0, 1, 2, 4, 3, 5, 1, 2, 0, 4, 3, 1, 2, 5, 4, 3, 0, 1, 2, 4, 3, 5, 1, 2, 0, 4, 3, 1, 2, 5, 4, 3, 0, 1, 2, 4, 3, 5, 1, 2, 0, 4, 3, 1, 2, 5, 4, 3, 0, 1, 2, 4, 3, 5, 1, 2, 0, 4, 3, 1, 2, 5, 4, 3, 0, 1, 2, 4, 3, 5, 1, 2, 0, 4, 3, 1, 2, 5, 4, 3, 0, 1, 2, 4, 3, 5, 1, 2, 0, 4, 3, 1, 2, 5, 4, 3, 0, 1, 2, 4, 3, 5, 1, 2, 0, 4, 3, 1, 2, 5, 4, 3, 0, 1, 2, 4, 3, 5, 1, 2, 0, 4, 3, 1, 2, 5, 4, 3, 0, 1, 2, 4, 3, 5, 1, 2, 0, 4, 3, 1, 2, 5, 4, 3, 0, 1, 2, 4, 3, 5, 1, 2, 0, 4, 3, 1, 2, 5, 4, 3, 0, 1, 2, 4, 3, 5, 1, 2, 0, 4, 3, 1, 2, 5, 4, 3, 0, 1, 2, 4, 3, 5, 1, 2, 0, 4, 3, 1, 2, 5, 4, 3, 0, 1, 2, 4, 3, 5, 1, 2, 0, 4, 3, 1, 2, 5, 4, 3, 0]
