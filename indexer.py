#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

base = [x[0] for x in os.walk("./base")]
tags = {'ope':[], 'sel':[], 'rep':[], 'vet':[], 'cha':[], 'str':[], 'mat':[], 'arq':[]}

with open("./indice.md", "w+") as saida:
    saida.write("# @qxcode\n\nArquivo a ser gerado automaticamente a partir dos títulos das questões.")
    for i in range(1,len(base)):
        with open(base[i] + "/Readme.md", "r") as readme:
            texto = readme.readlines()
            tags[texto[1].strip()[4:7]].append((("- [%s](%s/Readme.md#qxcode)\n" % (texto[1].strip()[3:], base[i]))))

    for tag in tags:
        tags[tag] = sorted(tags[tag], key=lambda x : int(x[18]))
        saida.write("\n\n")
        saida.write("## %s\n" % tag)
        for questao in tags[tag]:
            saida.write(questao)
