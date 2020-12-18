# chillput() by iLLVAN
# function to prompt for inputs and chill, it checks if user inputs are floatable, integers, contain floatable words etc
# the while loops at the end can be copied and modified (question and break condition)
# i hate typing backslashes - and for readability - thats why i do this first:
def n():
    print('\n')

# YOU NEED THIS
# input-ok-dictionary placed outside function, for check
dinpok = dict()
# list of answers - for indexed storage of valid answers
lanswe = list()

# CHILLPUT funtion
def chillput():
    # quest is defined when you call the function, scroll down for this
    new = input(quest)
    dinpok['ans'] = (new)
    # checking if single chararacters are floatable and counting characters
    listnew = list(new)
    dinpok['charcount'] = len(listnew)
    dinpok['charfloat'] = False
    for char in listnew:
        try:
            fchar = float(char)
            dinpok['charfloat'] = True
        except:
            continue
    # checking if words are floatable and counting words
    splitwords = new.split()
    dinpok['wordcount'] = len(splitwords)
    dinpok['wordfloat'] = False
    for word in splitwords:
        try:
            fword = float(word)
            dinpok['wordfloat'] = True
        except:
            continue
    # checking if word is integer
    dinpok['wordint'] = False
    for word in splitwords:
        try:
            iword = int(word)
            dinpok['wordint'] = True
        except:
            continue
    # check if is integer
    dinpok['isint'] = False
    if dinpok['wordint'] is True and dinpok['wordcount'] == 1:
        dinpok['isint'] = True
    # check if is float
    dinpok['isfloat'] = False
    if dinpok['wordfloat'] is True and dinpok['wordcount'] == 1 and dinpok['isint'] is False:
        dinpok['isfloat'] = True
    # check if is 'None'
    dinpok['isnone'] = False
    for i in ['None','NONE','none']:
        if i == new :
            dinpok['isnone'] = True
    # check if is 'Y/N' yes gives back True no gives back False - '0' and '1' work as well
    dinpok['yntf'] = None
    for i in ['Y','y','Yes','YES','yes','1']:
        if i == new :
            dinpok['yntf'] = True
    for i in ['N','n','No','NO','no','0']:
        if i == new :
            dinpok['yntf'] = False

    # PRINT RESULTS (for visualization only - use what you need - comment them out w/o affecting T/F results)
    n()
    n()
    print(new)
    if dinpok['wordcount'] > 0:
        print('words:', dinpok['wordcount'], 'characters:', dinpok['charcount'])
        if dinpok['isfloat'] is True:
            print('its a float (floatable)')
        else:
            print('its not a float')
            if dinpok['isint'] is True:
                print('--- but its floatable since it is an int')
        if dinpok['isint'] is True:
            print('its an integer - can be converted to an integer without loss')
        else:
            print('its not an integer')
        if dinpok['charfloat'] is True:
            print('contains floatable characters')
        else:
            if dinpok['charcount'] > 1 :
                print('contains no floatable characters - could be a word')
            else:
                print('its a letter')
        if dinpok['wordfloat'] is True and dinpok['wordcount'] > 1 :
            print('has floatable parts separated by whitespace')
        elif dinpok['wordfloat'] is True and dinpok['wordcount'] == 1 :
            print('might be numerical')
        else:
            print('contains no floatable word separated by whitespace')
        if dinpok['wordint'] is True and dinpok['wordcount'] == 1:
            print('only contains numbers (might have whitespace)')
        elif dinpok['wordint'] is True:
            print('contains words which are integers separated by whitespace')
        else:
            print('contains no words which are integers separated by whitespace')
        if dinpok['isnone'] is True:
            print('its none')
        if dinpok['yntf'] is False:
            print('no - false')
        elif dinpok['yntf'] is True:
            print('yes - true')
    # if you wanna see your dict, print it now:
        # n()
        # print(dinpok)
    else:
        print('no input')

# ----- FUNCTION CALL / example use of function / first question
n()
print('hello')
while True:
    quest = 'got number? '
    chillput()
        # condition for break options:
        # T/F: 'isint''isfloat''charfloat''wordfloat''wordint''isnone''yntf'
        # for counts: 'wordcount' 'charcount' use <>=!
    if dinpok['isint'] is True:
        # adding the answer to the list
        lanswe.append(dinpok['ans'])
        break
    # error message
    else:
        n()
        print('integers work ')
# ----- second question
n()
# clearing dinpok first
dinpok = dict()
print('hello again')
while True:
    quest = 'you like it? '
    chillput()
        # condition for break options:
        # T/F: 'isint''isfloat''charfloat''wordfloat''wordint''isnone' and 'yntf'
        # counts: 'wordcount' 'charcount'
    if dinpok['yntf'] is False or dinpok['yntf'] is True:
        # adding the answer to the list - TAKING T/F IN CASE OF 'yntf'!
        dinpok['ans'] = dinpok['yntf']
        lanswe.append(dinpok['ans'])
        break
    # error message
    else:
        n()
        print('its a y/n question')
# ----- PRINT ANSWERS
n()
print(lanswe)
# ------ EXIT
exit = input('press enter to exit')
