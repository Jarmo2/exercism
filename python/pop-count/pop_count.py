def egg_count(display_value: int) -> int:
    number_of_eggs = 0
    in_binary = bin(display_value)
    for pos in in_binary:
        if pos == '1':
            number_of_eggs += 1
    return number_of_eggs

