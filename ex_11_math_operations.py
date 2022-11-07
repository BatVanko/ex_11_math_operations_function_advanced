def math_operations(*args, **kwargs):

    for i in range( len(args)):
        current_num = float(args[i])
        index = i % 4
        if index == 0:
            kwargs['a'] += current_num
        elif index == 1:
            kwargs['s'] -= current_num
        elif index == 2:
            if current_num != 0:
                kwargs['d'] /= current_num
        elif index == 3:
            kwargs['m'] *= current_num
    sorted_result = sorted(kwargs.items(),key= lambda x:(-x[1], x[0]))

    return '\n'.join(f"{key}: {value:.1f}" for  key,value in sorted_result )



print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))