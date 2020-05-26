# COVID ZIP code data downloaders

This rig downloads COVID ZIP code data from often-hidden data feeds or quasi-public Mapserver instances.

# Requirements

* GNU Make.
* Python 3.7+.
* Pipenv (unless overriden; see the `PYENV` variable in the Makefile to use something a different environment manager). 

# Install

```
cp .env.example .env
make install
```

Customizing the .env file is not necessary at this time.

# Get started

Run `make help` for basic information on running the various commands.

```
make help
```

# Download raw data snapshots

```
make snapshot
```

This will download files like `data/external/fl-latest.json`.

`make all` is currently an alias for this command, but it's likely more steps will be added for a "full" build.

You can tag data downloads:

```
make TAG=davids-download snapshot
```

This will download files like `data/external/fl-davids-download.json`.

Similarly, the tag could be set to a numeric timestamp, like this:

```
make TAG=`date '+%s'` snapshot
```

This will download files like `data/external/fl-1590467891.json`.

# Architecture

The `processors` directory is a series of Python scripts. These scripts can do basically whatever they want or need as long as they write some kind of JSON or GeoJSON data to a file, though the simple download routines in the existing scrapers are all pretty similar.

The only requirement is that they must have the same basic command line interface to be run in an automated fashion with GNU Make:

```
python processors/SCRIPT.py OUTPUTFILE
```

This also means we're not limited to states. Add a file called `il_cookcounty.py` or `france.py` and this rig will happily run it.

By default and convention, these scripts use the Python [click](https://click.palletsprojects.com/en/7.x/) library to help manage command line arguments, file input/output arguments, etc.

The main impetus for this architecture is to allow many developers to work more of less independently. We assume that these downloaders will diverge if they handle edge cases and issues specific to a given data source; some level of abstraction may be achievable, but our bias is towards opening this up to many hands and sandboxing each downloader to encourage broad forms of participation.