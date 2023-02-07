import math

MAXIMAL_COLLISION_PROBABILITY = 2 ** -32


def collision_probability(number_of_draws: int, set_size: int) -> float:
    return 1 - math.exp(-number_of_draws ** 2 / (2 * set_size))


def collision_probability_log2(number_of_draws_log2: int, set_size_log2: int) -> float:
    """
    number_of_draws_log2 : we do 2 ** number_of_draws_log2 draws
    set_size_log2 : the draws are made on a set of set_size_log2 bits
    """
    return collision_probability(2 ** number_of_draws_log2, 2 ** set_size_log2)


def max_draws_for_set_size(set_size_log2: int) -> int:
    def has_low_enough_collision_probability(draw_count_log2):
        return collision_probability_log2(draw_count_log2, set_size_log2) < MAXIMAL_COLLISION_PROBABILITY

    return next(draw_count_log2 for draw_count_log2 in range(100, 0, -1) if has_low_enough_collision_probability(draw_count_log2))


def min_set_size_for_draw_count(draw_count_log2: int) -> int:
    def has_low_enough_collision_probability(set_size_log2):
        return collision_probability_log2(draw_count_log2, set_size_log2) < MAXIMAL_COLLISION_PROBABILITY

    return next(set_size_log2 for set_size_log2 in range(1024) if has_low_enough_collision_probability(set_size_log2))


print(collision_probability(10, 64000))

