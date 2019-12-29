# pymdb-rename
This project is in current initial development, not currently in a working full-functioning state.

## requirements
* imdbpy

For convenience a *requirements.txt* has been added to ease import

`python3 -m pip install -r requirements.txt`

or

`make install`

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
  * *file* - options for file output
    * *level* - log level for the output log file
    * *format* - represents how the output will be formatted for the file, see (https://docs.python.org/3/library/logging.html#logrecord-attributes)
  * *stdout* - options for STDOUT output
    * *level* - log level for STDOUT
    * *format* - represents how the output will be formatted for STDOUT, see (https://docs.python.org/3/library/logging.html#logrecord-attributes)

## string format
You can set your movie string format in *config.yml*.  

* *{n}* - name
* *{y}* - year

# tests
To run the unit tests...

`make tests` 