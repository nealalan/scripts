def print_format_table():
    """
    prints table of formatted text format options

    # print("\033[5;31;39mCONGRATS, YOU'RE RIGHT! \033[0m ")
    """
    for style in range(8):
        for fg in range(30,38):
            s1 = ''
            for bg in range(37,48):
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
            print(s1)
        print('\n')

print_format_table()
