def do_add(base):
    def add(increase):
        return base + increase  # 此处换成 print 会输出一个None？？？
    return add

a = do_add(23)
print a(100)
