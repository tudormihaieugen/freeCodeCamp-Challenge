def arithmetic_arranger(problems, ok=False):
    # check problem list
    first = ''
    second = ''
    sum_x = ''
    lines = ''
    # check if there are more than 5 problems
    if len(problems) > 5:
        return 'Error: Too many problems.'
    # split problems to single problem
    for i in problems:
        a = i.split()
        n1 = a[0]
        n2 = a[2]
        sign = a[1]
        # check the length of the number (max 4)
        if len(n1) > 4 or len(n2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # check the input as valid digits
        if not n1.isnumeric() or not n2.isnumeric():
            return "Error: Numbers must only contain digits."

        if sign == '+' or sign == '-':
            if sign == "+":
                sums = str(int(n1) + int(n2))
            else:
                sums = str(int(n1) - int(n2))
            # set length of sum and top, bottom and line values
            length = max(len(n1), len(n2)) + 2
            top = str(n1).rjust(length)
            bottom = sign + str(n2).rjust(length - 1)
            line = ''
            res = str(sums).rjust(length)
            for s in range(length):
                line += '-'
            # add to the overall string
            if i != problems[-1]:
                first += top + '    '
                second += bottom + '    '
                lines += line + '    '
                sum_x += res + '    '
            else:
                first += top
                second += bottom
                lines += line
                sum_x += res
        else:
            return "Error: Operator must be '+' or '-'."
    # using rstrip function for right align
    first.rstrip()
    second.rstrip()
    lines.rstrip()
    if ok:
        sum_x.rstrip()
        arranged_problems = first + '\n' + second + '\n' + lines + '\n' + sum_x
    else:
        arranged_problems = first + '\n' + second + '\n' + lines
    return arranged_problems


print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))
