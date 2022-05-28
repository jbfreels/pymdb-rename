# pymdb-rename

This project is in current initial development, not currently in a working full-functioning state, but getting closer by the day.

I started this project because I recently migrated from Arch Linux as my main OS to macOS X. Linux conveniently allows you access to FileBot 4.7 which has a nag-screen, but no monetary requirement to use. While FileBot does a TON of stuff, I only utilized the AMC script to rename media files I burned from copies of my DVD/Blu-Ray or downloads. IMO, $40 because I'm too lazy to rename my own files is a little much.

There are a few other projects out there that utilize similar functionatliy, but I just wanted something super basic. Give it an input, rename to output. That's it.

## requirements

- imdbpy - should be evident
- pathlib - for _touch_ function, utilized in unit tests to generate dummy files for testing

For convenience a _requirements.txt_ has been added to ease import

`python3 -m pip install -r requirements.txt`

or

`make install`

## config

There's an included 'config.yml.example', rename to 'config.yml' to get started. The example config file contains documentation.

The config file is placed with the python script.

## string format

You can set your movie string format in _config.yml_.

- _{n}_ - name
- _{y}_ - year

## tests

To run the unit tests...

`make test`
