import os

def get_large_files(start_path='.', size_limit_mb=1):
    large_files = []
    size_limit_bytes = size_limit_mb * 1024 * 1024
    for dirpath, _, filenames in os.walk(start_path):
        if '.git' in dirpath or 'node_modules' in dirpath or '__pycache__' in dirpath:
            continue
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if not os.path.islink(fp):
                size = os.path.getsize(fp)
                if size > size_limit_bytes:
                    large_files.append((fp, size))
    
    large_files.sort(key=lambda x: x[1], reverse=True)
    for fp, size in large_files:
        print(f"{fp}: {size / (1024*1024):.2f} MB")

get_large_files()
