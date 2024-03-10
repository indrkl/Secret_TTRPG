from stats import gen_dice_roll


def get_result(target, roll):
    diff = abs(target - roll)
    if diff <= 1:
        return 1
    elif diff > 2:
        return -1
    else:
        return 0


sample_size = 100000

def get_stats(target_number, dice_used, sample_size):
    total = 0.0
    for i in range(sample_size):
        dice = gen_dice_roll(dice_used)
        result = 0
        for d in dice:
            result += get_result(target_number, d)
        if result > 1:
            total += min(result, 1)

    boost = total / sample_size

    print ("""Using %d dice for target number %d we boost on average by %.2f"""%(dice_used, target_number, boost))


get_stats(1, 1, sample_size)
get_stats(1, 2, sample_size)
get_stats(1, 3, sample_size)
get_stats(2, 1, sample_size)
get_stats(2, 2, sample_size)
get_stats(2, 3, sample_size)
get_stats(3, 1, sample_size)
get_stats(3, 2, sample_size)
get_stats(3, 3, sample_size)
