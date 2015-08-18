#!/usr/bin/env python
# coding: utf-8

# http://qiita.com/lethe2211/items/6cbade2bc547649bc040 (in Japanese)
# http://stackoverflow.com/questions/12547683/python-3-eof-when-reading-a-line-sublime-text-2-is-angry
def get_input():
    print('Please input data. You input EOF if finish to.')
    print('NOTE: Ctrl-D on Unix. On the other hand, Enter after Ctrl-Z on Windows')
    '''
    >>> help(input)
    Help on built-in function input in module builtins:

    input(...)
        input([prompt]) -> string

        Read a string from standard input.  The trailing newline is stripped.
        If the user hits EOF (Unix: Ctl-D, Windows: Ctl-Z+Return), raise EOFError.
        On Unix, GNU readline is used if enabled.  The prompt string, if given,
        is printed without a trailing newline before reading.
    '''

    while True:
        # https://docs.python.org/3/reference/simple_stmts.html#grammar-token-yield_stmt
        try:
            yield input('> ')
        # https://docs.python.org/3/library/exceptions.html#EOFError
        except EOFError:
            break

if __name__ == '__main__':
    data = list(get_input())
    print('---')
    print("\n".join(data))
