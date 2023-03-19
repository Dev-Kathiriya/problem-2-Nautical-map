with open('small_input.txt', 'r') as f:
    inp = f.read().splitlines()
    oba = int(inp[0])
    inp = inp[1:]
    startLat, startLong, endLat, endLong = inp[0].split(', ')
    startLat, startLong, endLat, endLong = float(
        startLat), float(startLong), float(endLat), float(endLong)
    array = []
    for data in inp[1:]:
        arrays = []
        for no in data.split(', '):
            arrays.append(float(no))
        array.append(arrays)
    lat = 0
    lon = 0
    for i in array:
        lat = max(i[0], lat)
        lon = max(i[1], lon)
    array2 = []
    for i in array:
        array2.append([int(i[0]*100/lat), int(i[1]*30/lon)])
    startLat, startLong, endLat, endLong = [int(
        startLat*100/lat), int(startLong*30/lon), int(endLat*100/lat), int(endLong*30/lon)]
    data = []
    for i in range(0, 30):
        row = []
        for j in range(0, 100):
            if ([j, i] in array2):
                row.append('*')
            elif ([startLat, startLong] == [j, i] or [endLat, endLong] == [j, i]):
                row.append('1')
            else:
                row.append('_')
        data.append(row)
    a, b = 1, 1
    while (not (b == 0)):
        b = startLat-endLat
        if (b < 0):
            if (not (data[startLong][startLat+1] == '*')):
                startLat = startLat+1
                data[startLong][startLat] = "0"
        elif b > 0:
            if (not (data[startLong][startLat-1] == '*')):
                startLat = startLat-1
                data[startLong][startLat] = "0"
    while (not (a == 0)):
        a = startLong-endLong
        if (a < 0):
            if (not (data[startLong+1][startLat] == '*')):
                startLong = startLong+1
                data[startLong][startLat] = "0"
        elif a > 0:
            if (not (data[startLong-1][startLat] == '*')):
                startLong = startLong+1
                data[startLong][startLat] = "0"
    with open('output.txt', 'w') as files:
        for i in range(0, 30):
            strs = ''
            for j in range(0, 100):
                if ([startLat, startLong] == [j, i] or [endLat, endLong] == [j, i]):
                    data[i][j] = '1'
                strs += str(data[i][j])
            files.write(strs+'\n')
