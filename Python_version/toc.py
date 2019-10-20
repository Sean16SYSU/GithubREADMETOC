import os

import os


def toc(file='README.md',
        stpath='.',
        stopwith='dir',
        withlink=True,
        firstNotInSet=['.', '_']):
    def toc_f(stpath='.',
              stopwith='dir',
              withlink=True,
              firstNotInSet=['.', '_']):
        def rec_toc_f(stpath='.', stopwith='dir'):
            totalstr_arr = []
            for _, dirs, files in os.walk(stpath):
                for dir_name in dirs:
                    if dir_name[0] in firstNotInSet:
                        continue
                    if withlink:
                        totalstr_arr += [
                            '* [' + dir_name + ']({0})'.format(
                                os.path.join(stpath, dir_name)[1:])
                        ]
                    else:
                        totalstr_arr += ['* ' + dir_name]
                    tmpstr = rec_toc_f(os.path.join(stpath, dir_name),
                                       stopwith=stopwith)
                    if tmpstr is None or len(tmpstr) == 0:
                        continue
                    tmpstr = list(map(lambda x: '   ' + x, tmpstr))
                    totalstr_arr += tmpstr

                if stopwith == 'file':
                    for file in files:
                        if file[0] in firstNotInSet:
                            continue
                        file_name = os.path.splitext(file)[0]
                        if withlink:
                            totalstr_arr += [
                                '* [' + filename + ']({0})'.format(
                                    os.path.join(stpath, filename)[1:])
                            ]
                        else:
                            totalstr_arr += ['* ' + filename]
            return totalstr_arr

        tarr = rec_toc_f(stpath, stopwith)
        return '\n'.join(tarr)

    toc = toc_f(stpath=stpath,
                stopwith=stopwith,
                withlink=withlink,
                firstNotInSet=firstNotInSet)
    with open('README.md', 'r', encoding='utf-8') as f:
        data = f.read()
    if '[toc]' in data:
        toc = toc_f(stpath=stpath,
                    stopwith=stopwith,
                    withlink=withlink,
                    firstNotInSet=firstNotInSet)

        data = data.replace('[toc]', toc)
        with open('README.md', 'w', encoding='utf-8') as f:


if __name__ == '__main__':
    toc()