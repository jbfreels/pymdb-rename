# pymdb-rename
This project is in current initial development, not currently in a working full-functioning state, but getting closer by the day.

I started this project because I recently migrated from Arch Linux as my main OS to macOS X.  Linux conveniently allows you access to FileBot 4.7 which has a nag-screen, but no monetary requirement to use.  While FileBot does a TON of stuff, I only utilized the AMC script to rename media files I burned from copies of my DVD/Blu-Ray or downloads.  IMO, $40 because I'm too lazy to rename my own files is a little much.  

There are a few other projects out there that utilize similar functionatliy, but I just wanted something super basic.  Give it an input, rename to output.  That's it.  

## requirements
* imdbpy

For convenience a *requirements.txt* has been added to ease import

`python3 -m pip install -r requirements.txt`

or

`make install`

## config
There's an included 'config.yml.example', rename to 'config.yml' to get started. 
* *action* - What to do with the file
  * *copy* - copy the file
  * *move* - move the file
  * *test* - don't do anything, just show what will happen
* *clean* - clean up clutter
  * *enabled* - true/false will clean folder when folder is passed as input
  * *min_size* - nuke everything under the specified size in MegaBytes
  * *max_size* - 
  * *exts* - list of filetypes to always delete
* *movie_format* - represents how the output filname will be formatted, see *string format* below
* *movie_exts* - list of valid filename extensions for movies
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