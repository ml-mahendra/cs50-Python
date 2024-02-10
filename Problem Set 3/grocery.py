
g_list = {}
while True:
    try:
        item = input().lower()
        if item in g_list:
            g_list[item] += 1
        else:
            g_list[item] = 1

    except EOFError:
        
        for key in sorted(g_list.keys()):
            print(g_list[key], key.upper())
        break
