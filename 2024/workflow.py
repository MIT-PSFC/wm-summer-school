#!/usr/bin/env python3

"""
Database preparation workflow for the 2024 W&M Summer School
"""

from disruption_py.handlers import CModHandler
from disruption_py.settings.shot_ids_request import DatabaseShotIdsRequest
from disruption_py.settings.shot_settings import ShotSettings

handler = CModHandler()

shot_ids_request = DatabaseShotIdsRequest(
    "select distinct shot from disruption_warning"
)

shot_settings = ShotSettings(efit_tree_name="efit18")

df = handler.get_shots_data(
    shot_ids_request=shot_ids_request,
    shot_settings=shot_settings,
    output_type_request="dataframe",
)

df.to_csv("cmod.csv", index=False)

print(df)
