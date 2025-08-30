#!/usr/bin/env python3

from pol import getC13_16 as getCenario
from pot import create_graph

create_graph(*getCenario())
