#此文件没啥用 只是为了验证一些代码对不对
def from_file_get_date(file_name):
    f = None

    try:
        f = open(file_name,'r')
        line = f.readline()
        user_date = eval(line)
        return user_date
    except Exception as e:
        print(e)
    finally:
        if not f:
            f.close()

if __name__ == '__main__':
    result = from_file_get_date('user_date.txt')
    print(type(result))
    print(result)
