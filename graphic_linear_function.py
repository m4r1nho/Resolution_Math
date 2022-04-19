from matplotlib import pyplot as plt  # importing the lib


def graphic_linear_function():
    formula_y = str(input('Enter the ƒ(x): '))

    # Applying mathematical theory
    # differentiating uppercase and lowercase
    if 'X' or 'x' in formula_y:
        if 'X' in formula_y:
            separate = (formula_y.index('X'))  # found the X for separate values
        if 'x' in formula_y:
            separate = (formula_y.index('x'))  # found the x for separate values
    else:
        print('This is not a linear function because it does not have the value x')
        exit()
    # exist a variable 'separate' for separate the 'a' and 'b'
    # ƒ(x) = ax+b
    a = formula_y[:separate]  # before X
    b = formula_y[separate + 1:]

    # Applying mathematical theory
    if a == '':
        print('This is not a linear function because it does not have the value x')
        exit()
    a = float(a)

    # you can if you don't have the b, so when you don't have it's worth 0
    if b == '':
        b = 0
    b = float(b)

    x = [-2, -1, 0, 1, 2]  # cases of x
    y = []
    for i in range(len(x)):  # get values y accordingly function
        value = x[i] * a
        value = value + b
        y.append(value)

    # the graphic, needed to do like this to have four squares that is in coordinates
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    plt.plot(x, y, marker='o')  # to plot with the vectors
    plt.title('Linear Function')
    plt.show()


graphic_linear_function()  # execute the def
