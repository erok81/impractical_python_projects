''' THE OBJECTIVE:
    Write code that finds the letters hidden after punctuation marks in a null cipher and lets
    the user choose the number of letters after a punctuation mark to search for a solution.'''


import re

test_string_1 = '''Dear bean junky: it has come to my attention, like some of us,\
iguanas are green. keen to find out, everyone has started painting themselves green.\
because of this, everyone now smells like peas, animal dung, nd trousers. send help'''

test_string_2 = '''Worthie Sir John: Hope, that is the beste comfort of the afflicted,
cannot much, I fear me, help you now. That I would saye to you,
is this only: if ever I may be able to requite that I do owe you,
stand not upon asking me. 'Tis not much I can do: but what I
can do, bee you verie sure I wille. I knowe that, if deathe comes,
if ordinary men fear it, it frights not you, accounting for it for a
high honour, to have such a rewarde of your loyalty. Pray yet that
you may be spared this soe bitter, cup. I fear not that you will
grudge any sufferings; onlie if bie submission you can turn them
away, 'tis the part of a wise man. Tell me, an if you can, to do for
you anythinge that you wolde have done. The general goes back
on Wednesday. Restinge your servant to command. R.T.'''


def decode(message, num):

split = re.split('[,:?.!]', message)

    decoded = ''
    for word in split[1:]:
        if word[0] == ' ':
            decoded += word[num + 1]
        else:
            decoded += word[num]

    return decoded