list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
full_player = len(list_players)
half_player = full_player // 2

teamFirst = list_players[:half_player]
teamSecond = list_players[half_player:]

print("Команда 1:", teamFirst)
print("Команда 2:", teamSecond)