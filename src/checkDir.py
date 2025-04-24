import os

def is_in_directory(work_dir, target_path):
    work_dir = os.path.abspath(work_dir)
    target_path = os.path.abspath(target_path)
    return os.path.commonpath([work_dir]) == os.path.commonpath([work_dir, target_path])
