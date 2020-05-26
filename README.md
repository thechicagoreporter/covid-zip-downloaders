# COVID ZIP code data downloaders

This rig downloads COVID ZIP code data from often-hidden data feeds or quasi-public Mapserver instances.

# Requirements

* Python 3.7+.
* Pipenv is used by default. Other Python environment tools could be used; see the `PYENV` variable in the Makefile for more information. 
* PostgreSQL / Postgis (if data loading desired).

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

You can tag data downloads:

```
make TAG=davids-download snapshot
```

This will download files like `data/external/fl-davids-download.json`.

```
make TAG=`date '+%s'` snapshot
```

This will download files like `data/external/fl-1590467891.json`.

# Architecture

The `processors` directory is a series of Python scripts. These scripts can do basically whatever, though Mapserver downloads are all pretty similar.

They must have the same basic command line interface to be run in an automated fashion with GNU Make:

```
python processors/SCRIPT.py OUTPUTFILE
```