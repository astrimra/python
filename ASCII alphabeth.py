#!/usr/bin/python3
__author__ = 'Niklas'
# -*- coding: utf-8 -*-
from sys import argv

split = [0,        10,       20,      29,       39,      48,      57,       67,       77,  82,      91,      100,     109,      119,     128,      138,      148,      158,      168,     177,     186,      196,      206,       217,      227,     236,     245, 250, 255,          269,      279,      289, 294, 299,303, 308,    316,    324,  330,  336,       347,   354,      364,      374,      384,     393,      403,     412,      422,      432]
line = ["   ###    ########   ######  ########  ######## ########  ######   ##     ## ####       ## ##    ## ##       ##     ## ##    ##  #######  ########   #######  ########   ######  ######## ##     ## ##     ## ##      ## ##     ## ##    ## ########      ####       ####### ## #####     ###         ####      ##                    ### ###     #####      ##    #######   #######  ##        ########  #######  ########  #######   ####### ",
        "  ## ##   ##     ## ##    ## ##     ## ##       ##       ##    ##  ##     ##  ##        ## ##   ##  ##       ###   ### ###   ## ##     ## ##     ## ##     ## ##     ## ##    ##    ##    ##     ## ##     ## ##  ##  ##  ##   ##   ##  ##       ##       ####      ####      ##    ##  ##   ##       ####     ####                  ##     ##   ##   ##   ####   ##     ## ##     ## ##    ##  ##       ##     ## ##    ## ##     ## ##     ##",
        " ##   ##  ##     ## ##       ##     ## ##       ##       ##        ##     ##  ##        ## ##  ##   ##       #### #### ####  ## ##     ## ##     ## ##     ## ##     ## ##          ##    ##     ## ##     ## ##  ##  ##   ## ##     ####       ##        ####     ## ##     ## ##  ##    ###                   ##                  ##       ## ##     ##    ##          ##        ## ##    ##  ##       ##            ##   ##     ## ##     ##",
        "##     ## ########  ##       ##     ## ######   ######   ##   #### #########  ##        ## #####    ##       ## ### ## ## ## ## ##     ## ########  ##     ## ########   ######     ##    ##     ## ##     ## ##  ##  ##    ###       ##       ##          ##     ##  ###### ##  #  ## ##     ## #### ####          #######         ##       ## ##     ##    ##    #######   #######  ##    ##  #######  ########     ##     #######   ########",
        "######### ##     ## ##       ##     ## ##       ##       ##    ##  ##     ##  ##  ##    ## ##  ##   ##       ##     ## ##  #### ##     ## ##        ##  ## ## ##   ##         ##    ##    ##     ##  ##   ##  ##  ##  ##   ## ##      ##      ##                 #######     ##  ## ## ######### #### ####      ##                  ##       ## ##     ##    ##   ##               ## #########       ## ##     ##   ##     ##     ##        ##",
        "##     ## ##     ## ##    ## ##     ## ##       ##       ##    ##  ##     ##  ##  ##    ## ##   ##  ##       ##     ## ##   ### ##     ## ##        ##    ##  ##    ##  ##    ##    ##    ##     ##   ## ##   ##  ##  ##  ##   ##     ##     ##           ####  ##    ##     ##    ##  ##     ##  ##   ##  ### ####                  ##     ##   ##   ##     ##   ##        ##     ##       ##  ##    ## ##     ##   ##     ##     ## ##     ##",
        "##     ## ########   ######  ########  ######## ##        ######   ##     ## ####  ######  ##    ## ######## ##     ## ##    ##  #######  ##         ##### ## ##     ##  ######     ##     #######     ###     ###  ###  ##     ##    ##    ########      #### ###    ######  ##### ## ##     ## ##   ##   ###  ##          #######   ### ###     #####    ###### #########  #######        ##   ######   #######    ##      #######   ####### ",
]

def word(mystr):
    print()
    a = []
    for n in mystr:
        pos = ord(n)
        newPos = pos
        if 65 <= pos <= 65+25 or 97 <= pos <= 97+25:
            newPos -= 65 if pos < 97 else 97

        if 48 <= pos <= 58:
            newPos = 39 + pos - 48

        newPos = 26 if pos == 32 else newPos
        newPos = 27 if pos == 33 else newPos
        newPos = 28 if pos == 198 or pos == 230 else newPos
        newPos = 29 if pos == 216 or pos == 248 else newPos
        newPos = 30 if pos == 197 or pos == 229 else newPos
        newPos = 31 if pos == 44 else newPos
        newPos = 32 if pos == 59 else newPos
        newPos = 33 if pos == 46 else newPos
        newPos = 34 if pos == 58 else newPos
        newPos = 35 if pos == 45 else newPos
        newPos = 36 if pos == 95 else newPos
        newPos = 37 if pos == 40 else newPos
        newPos = 38 if pos == 41 else newPos

        if 0 <= newPos <= 48:
            a.append(newPos)

    for n in range(len(line)):
        l = line[n]
        for i in a:
            print(l[split[i]:split[i+1]], end="")
        print()
    print()

myword = " ".join(argv[1:]) if len(argv) > 1 else "-"

if myword == "-":
    while myword != "":
        myword = (input("Hva skal oversettes? (enter for å avslutte)\n") or "")
        if myword != "":
            word(myword)
else:
    word(myword)