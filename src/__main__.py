#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Main entry point of the software. Chooses the algorithm to apply and the inputs
and outputs
"""
# Libraries
import os
import platform
from cli.controller.main import controller


if __name__ == "__main__":
    # Prepare coding
    if platform.system() == "Windows":
        os.system("chcp 65001")

    # Trigger main controller
    controller()
