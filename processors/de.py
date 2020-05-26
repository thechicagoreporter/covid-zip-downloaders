"""
Download Delawares's COVID ZIP code data
"""
import click
import requests
from urllib.parse import urlparse, parse_qs

URL_ROOT = 'https://services1.arcgis.com/PlCPCPzGOwulHUHo/arcgis/rest/services/FinalZip2_View/FeatureServer/0/query'
PARAMS = {
	'cacheHint': ['true'],
	'f': ['geojson'],
	'maxRecordCountFactor': ['2'],
	'outFields': ['*'],
	'outSR': ['102100'],
	'quantizationParameters': ['{"mode":"view","originPosition":"upperLeft","tolerance":1.0583354500042346,"extent":{"xmin":-75.78875639999997,"ymin":38.45103980000001,"xmax":-75.04875820000005,"ymax":39.83951600000005,"spatialReference":{"wkid":4326,"latestWkid":4326}}}'],
	'resultOffset': ['0'],
	'resultRecordCount': ['4000'],
	'returnGeometry': ['true'],
	'spatialRel': ['esriSpatialRelIntersects'],
	'where': ["Dates > timestamp '2020-04-19 03:59:59'"]
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