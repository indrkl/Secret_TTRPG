import random

available_dice = 8

def check_match(dice_rolls, target_dice, target_count, proficiency):
    proficiency_remaining = proficiency
    proficiency_threshold = 0
    used_dice = []
    remaining_dice = dice_rolls.copy()

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


def largest_streak(dice, target_dice, proficiency):
    largest = 0
    for i in range(1, len(dice)+1):
        if check_match(dice, target_dice, i, proficiency):
            largest = i
        else:
            break
    # print (str([dice, target_dice, proficiency]))
    return largest



def get_stats(target_dice, target_count, sample_size):
    print("Roll target is %d X R%d, sample size: %d"%(target_count, target_dice, sample_size))
    for proficieny in range(0, 1):
        successes = 0
        for i in range(sample_size):
            dice = gen_dice_roll(available_dice)
            if check_match(dice, target_dice, target_count, proficieny):
                successes += 1

        odds = successes * 100.0 / sample_size
        print("With proficiency %d your odds would be %.1f %%"%(proficieny, odds))


def largest_streak_stats(target_dice_set, sample_size, proficiency):
    total = 0.0
    for i in range(sample_size):
        dice = gen_dice_roll(available_dice)
        largest = 0
        for target_dice in target_dice_set:
            largest = max(largest, largest_streak(dice, target_dice, proficiency))
        total += largest
    print("""The average streak with following set: %s and %d proficiency is %.1f"""%(str(target_dice_set), proficiency, total / sample_size))




sample_size = 20000
# for target_count in range(2, 7):
#     for target_dice in [4, 5, 6]:
#         get_stats(target_dice, target_count, sample_size)
#
#     successes = 0
#     for i in range(sample_size):
#         dice = gen_dice_roll(6)
#         success = False
#         for result in range(1, 7):
#             if check_match(dice, result, target_count, 0):
#                 success = True
#         if success:
#             successes += 1
#     odds = successes * 100.0 / sample_size
#     print("""With target count %d, your odds would be %.1f to get any number"""%(target_count, odds))

first_number = 2
second_number = 5

if __name__ == '__main__':
    # largest_streak_stats([first_number], sample_size, 0)
    # # largest_streak_stats([first_number], sample_size, 1)
    # largest_streak_stats([first_number], sample_size, 2)
    # # largest_streak_stats([first_number], sample_size, 3)
    # largest_streak_stats([first_number], sample_size, 4)
    # largest_streak_stats([1, 2, 3, 4, 5, 6], sample_size, 0)
    # # largest_streak_stats([1, 2, 3, 4, 5, 6], sample_size, 1)
    # # largest_streak_stats([1, 2, 3, 4, 5, 6], sample_size, 2)
    # # largest_streak_stats([1, 2, 3, 4, 5, 6], sample_size, 3)
    # # largest_streak_stats([1, 2, 3, 4, 5, 6], sample_size, 4)
    # largest_streak_stats([first_number, second_number], sample_size, 0)
    # # largest_streak_stats([first_number, second_number], sample_size, 1)
    # largest_streak_stats([first_number, second_number], sample_size, 2)
    # # largest_streak_stats([first_number, second_number], sample_size, 3)
    # largest_streak_stats([first_number, second_number], sample_size, 4)
    largest_streak_stats([first_number, second_number], sample_size, 5)
