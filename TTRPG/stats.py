import random


def check_match(dice_rolls, target_dice, target_count, proficiency):
    proficiency_remaining = proficiency
    proficiency_threshold = 0
    used_dice = []
    remaining_dice = dice_rolls

    while proficiency_remaining >= proficiency_threshold:
        rm_indx = []
        for i in range(len(remaining_dice)):
            if abs(remaining_dice[i]-target_dice) == proficiency_threshold:
                proficiency_remaining -= proficiency_threshold
                used_dice.append(remaining_dice[i])
                rm_indx.append(i)
            if proficiency_remaining < proficiency_threshold:
                break
        proficiency_threshold += 1

        for i in range(len(rm_indx)-1, -1, -1):
            del(remaining_dice[rm_indx[i]])

    return len(used_dice) >= target_count


def gen_dice_roll(number_of_dice):
    dice = []
    for i in range(number_of_dice):
        dice.append(random.randint(1, 6))
    return dice


def get_stats(target_dice, target_count, sample_size):
    print("Roll target is %d X R%d, sample size: %d"%(target_count, target_dice, sample_size))
    for proficieny in range(0, 6):
        successes = 0
        for i in range(sample_size):
            dice = gen_dice_roll(6)
            if check_match(dice, target_dice, target_count, proficieny):
                successes += 1

        odds = successes * 100.0 / sample_size
        print("With proficiency %d your odds would be %.1f %%"%(proficieny, odds))


sample_size = 10000
for target_count in range(2, 7):
    for target_dice in [4, 5, 6]:
        get_stats(target_dice, target_count, sample_size)
