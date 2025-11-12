def move(my_list, direction):
    # מוצא את המיקום של החזיר (ה-1)
    pig_index = my_list.index(1)

    # יוצר עותק מהרשימה כדי לעבוד עליו
    new_positions = my_list[:]

    # מאפס את המקום הנוכחי של החזיר
    new_positions[pig_index] = 0

    # מזיז ימינה
    if direction == 'right' and pig_index < len(my_list) - 1:
        new_positions[pig_index + 1] = 1

    # מזיז שמאלה
    elif direction == 'left' and pig_index > 0:
        new_positions[pig_index - 1] = 1

    # אם אי אפשר לזוז (החזיר בקצה)
    else:
        new_positions[pig_index] = 1  # נשאר במקום

    return new_positions

