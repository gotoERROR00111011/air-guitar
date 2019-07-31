def data_return(onORoff,turn):

    if onORoff == 1:
        print("음악 시작")
        onOff = 1
    else :
        print("음악 끄기")
        onOff = 0

    number = turn

    if number == 1:         # 낮은 도
        melody = 60
    elif number == 2:       # 낮은 레
        melody = 62
    elif number == 3:       # 낮은 미
        melody = 64
    elif number == 4:       # 낮은 파
        melody = 65
    elif number == 5:       # 낮은 솔
        melody = 67
    elif number == 6:       # 낮은 라
        melody = 69
    elif number == 7:       # 낮은 시
        melody = 71
    elif number == 8:       # 높은 도
        melody = 72
    elif number == 9:       # 높은 레
        melody = 74
    elif number == 10:      # 높은 미
        melody = 76
    elif number == 11:      # 높은 파
        melody = 77
    elif number == 12:      # 높은 솔
        melody = 79
    elif number == 13:      # 높은 라
        melody = 81
    elif number == 14:      # 높은 시
        melody = 83
        
##        
##    melody = [[60, 62, 64, 65, 67, 69, 71],
##              [72, 74, 76, 77, 79, 81, 83],
##              [84, 86, 88, 89, 91, 93, 95]]

    return onOff ,melody
