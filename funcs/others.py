import math
from speedtest import Speedtest
from discord.embeds import Embed


def calculate(input):
    if 'pi' in input:
        input = input.replace('pi', str(math.pi))
    if '圓周率' in input:
        input = input.replace('圓周率', str(math.pi))
    if 'π' in input:
        input = input.replace('π', str(math.pi))
    if input[-3:] == '取整數':
        input = input[:-3]
        return '=' + str(int(eval(input)))
    elif '取到小數第' in input:
        temp_index = 0
        for index in range(len(input)):
            if input[index] == '第':
                temp_index = index + 1
                break

        count = len(input) - temp_index - 1
        valid = eval(input[temp_index:-1])

        input = input[:-(count + 6)]
        real_ans = str(eval(input))

        dot_index = 0
        floatNum = 0
        for index in range(len(real_ans)):
            if real_ans[index] == '.':
                dot_index = index
                floatNum = real_ans[dot_index + 1:]

        trimmed_ans = real_ans[:dot_index + 1] + floatNum[:valid]

        return '=' + str(trimmed_ans)
    else:
        return '=' + str(eval(input))


def report():
    embed=Embed(title='表單回報', url='https://forms.gle/9Q6aDDGXcQ2kftYy5', description='謝謝你願意回報或回饋\n請提交至標題連結表單')
    embed.set_thumbnail(url='https://i.imgur.com/ALXeVez.png')

    return embed

