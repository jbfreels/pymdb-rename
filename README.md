# pymdb-rename

## requirements
* imdbpy

For convenience a *requirements.txt* has been added to ease import

`python3 -m pip install -r requirements.txt`

## config
* *out_path* - where the output will go, if None, output will go to the folder where the input file resides
* *action* - What to do with the file
  * *copy* - copy the file to *out_path*
  * *move* - move the file to *out_path*
  * *test* - don't do anything, just show what will happen
* *movie_format* - represents how the output filname will be formatted, see *string format* below
* *movie_exts* - valid filename extensions for movies
* *logger*
  * *path* - output path for the logfile
  * *filelevel* - level for the log file
  * *stdoutlevel* - level for screen output
  * *format* - represents how the output will be formatted, see (https://docs.python.org/3/library/logging.html#logrecord-attributes)

## string format
You can set your movie string format in *config.yml*.  I've tried my best to clone the same format FileBot utilizes for convenience.

* *{n}* - name
* *{y}* - year
