#!/usr/bin/env python3

import os
from nicegui import ui

upload = ui.upload(label='Select a file to extract directory from')

def handle_upload(e):
    file = e.files[0]
    directory_path = os.path.dirname(file.name)
    ui.label(f'Selected directory: {directory_path}')

upload.on('change', handle_upload)
