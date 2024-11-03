def find_common_participants(group_1, group_2, separator=','):
    group_a = group_1.split(separator)
    group_b = group_2.split(separator)

    common_participants = set(group_a) & set(group_b)

    return sorted(common_participants)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common = find_common_participants(participants_first_group, participants_second_group, '|')
print(common)
