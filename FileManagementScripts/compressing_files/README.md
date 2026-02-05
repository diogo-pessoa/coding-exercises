Snippet to remove '.gz' from the middle of the filename. Happened because file had date as suffix, and file format
mid-string. After gunzip recursively, I ran the loop below to clean the file.  

```bash
 for f in *.gz.*; do
  mv -- "$f" "${f/.gz/}"
done

```


Python version of simple file compression

[compress_files.py](compress_files.py)

Alternative in bash:

