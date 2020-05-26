"""
Download Illinois' COVID ZIP code data
"""
import click
import requests
from urllib.parse import urlparse, parse_qs

URL_ROOT = 'https://www.dph.illinois.gov/sitefiles/COVIDZip.json'
PARAMS = {
	'nocache': 1,
}


@click.command()
@click.argument('output_file', type=click.File('w'))
def download(output_file):
	response = requests.get(URL_ROOT, params=PARAMS)
	if response.ok:
		output_file.write(response.text)
		click.echo(f'Success: {response.url}')
		click.echo(f'Wrote {output_file.name}')
	else:
		click.echo(f'Error: {response.url}')
		click.echo(f'Could not write {output_file.name}')


if __name__ == '__main__':
    download()