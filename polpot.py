#!/usr/bin/env python3

# Altere GTFO para o seu cenário de experimento #
# Ex: Cenário 1 a 4, altere GTFO para getC1_4 # #
from pol import GTFO as getCenario
from pot import create_graph

# # # # # # # # # # # # # # # # # # # # # # # # #


create_graph(*getCenario())
