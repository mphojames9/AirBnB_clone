#!/usr/bin/python3
"""create a unique FileStorage instance for your application"""
from models.engine.file_storage import FileStorage

"""An instance of FileStorage"""
storage = FileStorage()
storage.reload()
