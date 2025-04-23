#!/usr/bin/env python3

"""
Database preparation workflow for the 2025 W&M Summer School
"""

from disruption_py.workflow import get_shots_data

df = get_shots_data(
    tokamak="cmod",
    shotlist_setting="disruption_warning",
)

df.to_csv("cmod.csv", index=False)

print(df)
