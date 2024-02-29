def fun1(a: int, **kwargs):
    print(f'fun1-a:{a}')
    print('fun1-kwargs:{}'.format(kwargs))

    kwargs['file_name'] = "file_name_test"
    fun2(4, **kwargs)


def fun2(b: int, **kwargs):
    print('fun2-b:%s' % b)
    print(f'fun2-kwargs:{kwargs}')


if __name__ == '__main__':
    fun1(3, file_id=45)
