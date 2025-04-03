from stats import gen_dice_roll

def match(presented_dice: list, challenge_dice: list, proficiency: int):
    prof_part_success = proficiency
    prof_success = proficiency
    boon_success = proficiency

    presented_dice.sort()
    challenge_dice.sort()

    for i in range(len(presented_dice)):
        prof_part_success -= max(0, challenge_dice[i] - 1 - presented_dice[i])
        prof_success -= max(0, challenge_dice[i] - presented_dice[i])
        boon_success -= max(0, challenge_dice[i] + 1 - presented_dice[i])

    if boon_success >= 0:
        return 3
    if prof_success >= 0:
        return 2
    if prof_part_success >= 0:
        return 1
    return 0



def get_statistics(presented_dice: list, proficiency: int, difficulty: int, hard: bool, number_of_runs: int):
    effort = len(presented_dice)

    result_d = {0: 0, 1: 0, 2: 0, 3: 0}

    for i in range(number_of_runs):
        challenge_dice = gen_dice_roll(difficulty)
        challenge_dice.sort()

        if hard:
            challenge_dice = challenge_dice[-effort:]
        else:
            challenge_dice = challenge_dice[:effort]

        result_d[match(presented_dice, challenge_dice, proficiency)] += 1

    print(f"""with presented dice {presented_dice} and {proficiency} proficiency. We ran {number_of_runs} tryes on {effort} / {difficulty} {'hard' if hard else 'easy'}.
{result_d[0]} times it failed.
{result_d[1]} times it partially succeeded.
{result_d[2]} times it succeeded.
{result_d[3]} times it succeeded with a boon.
""")

presented_dice = [6, 5, 4, 3, 3, 2]
proficiency = 5

get_statistics(presented_dice, proficiency, len(presented_dice), True, 1000)
get_statistics(presented_dice, proficiency, len(presented_dice) + 1, False, 1000)
get_statistics(presented_dice, proficiency, len(presented_dice) + 2, False, 1000)
get_statistics(presented_dice, proficiency, len(presented_dice) + 5, False, 1000)
get_statistics(presented_dice, proficiency, 20, False, 1000)