student_list = [2342,3433,1234]
teacher_list = [1231, 2333]
work_list = ['eat']
while True:
    input_num = int(input('please enter your last 4 numbers'))
    print(input_num)
    if input_num in student_list:
        print('Welcome')
        break
    elif input_num in teacher_list:
        print('Your work is {}'.format(worklist[0]))
        break
    else:
        print('I think your number is wrong, try again')
