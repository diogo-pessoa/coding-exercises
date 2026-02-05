import os
import re
import shutil
import sys
import uuid
from datetime import date


class FileModifier:
    _date_suffix_re = re.compile(r"\.(\d{4}-\d{2}-\d{2})$")

    def move_files(self, tmp_path: str, final_path: str) -> None:
        os.replace(tmp_path, final_path)

    def rename_file(self, filename: str, datestr: str | None = None) -> str:
        if datestr is None:
            datestr = date.today().isoformat()

        filename = self._date_suffix_re.sub("", filename)

        if filename.endswith(".gz"):
            base = filename[:-3]
            return f"{base}.{datestr}.gz"

        return f"{filename}.{datestr}"


def main() -> None:
    if len(sys.argv) < 2:
        print("usage: python renaming_files.py <log_dir>")
        sys.exit(2)

    log_dir = sys.argv[1]
    if not os.path.isdir(log_dir):
        print("could not access log directory, check log_dir argument")
        sys.exit(2)

    try:
        file_manager = FileModifier()
        log_files = os.listdir(log_dir)
        print(f"checking existing logs: {log_files}")

        dest_dir = os.path.join(os.curdir, "renamed_logs")
        os.makedirs(dest_dir, exist_ok=True)

        datestr = date.today().isoformat()

        for filename in sorted(log_files):
            src_path = os.path.join(log_dir, filename)
            if not os.path.isfile(src_path):
                continue

            final_name = file_manager.rename_file(filename, datestr)
            final_path = os.path.join(dest_dir, final_name)

            tmp_path = os.path.join(dest_dir, f".tmp-{uuid.uuid4().hex}-{final_name}")

            shutil.copy2(src_path, tmp_path)
            file_manager.move_files(tmp_path, final_path)

            print(f"copied {src_path} -> {final_path}")

    except OSError as error:
        print(error)
        sys.exit(2)


if __name__ == "__main__":
    main()
