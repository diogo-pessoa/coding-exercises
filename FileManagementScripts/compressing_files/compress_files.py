import gzip
import shutil
import sys
import os
from pathlib import Path

class CompressFiles:

    def gzip_dir(self, log_dir: str) -> None:
        for p in Path(log_dir).iterdir():
            if p.is_file() and not p.name.endswith(".gz"):
                gz = p.with_name(p.name + ".gz")
                with p.open("rb") as f_in, gzip.open(gz, "wb") as f_out:
                    shutil.copyfileobj(f_in, f_out)
                print(f"{p} -> {gz}")

def main():
    compress_files = CompressFiles()
    # Compresses files recursively in a dir
    logs_path = sys.argv[1]

    if not os.path.exists(logs_path):
        print(f'Could not find source dir, check path: {logs_path}')
        sys.exit(2)
    try:
        compress_files. gzip_dir(logs_path)
    except OSError as err:
        print(f'there was a problem: \t {err}')
        sys.exit(2)


if __name__ == "__main__":
    main()