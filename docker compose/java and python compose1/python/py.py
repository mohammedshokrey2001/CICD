# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd


def main():
    i = 0
    salaries = []
    names = []
    with open('data/ww.txt', 'r') as f:
        lines = f.readlines()

    for contents in lines:
        contents = str(contents)
        contents = contents.replace("\n","")
        if i % 2 == 0:

            names.append(contents)
        else:
            salaries.append(contents)
        i += 1


    df = pd.DataFrame(list(zip(names, salaries)), columns=['Names', 'Salaries'])
    print(df)


if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
