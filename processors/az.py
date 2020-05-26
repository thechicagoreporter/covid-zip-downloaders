"""
Download Arizona's COVID ZIP code data
"""
import click
import requests
from urllib.parse import urlparse, parse_qs

URL_ROOT = 'https://services1.arcgis.com/mpVYz37anSdrK4d8/arcgis/rest/services/CVD_ZIPS_FORWEBMAP/FeatureServer/0/query'
PARAMS = {
	'cacheHint': ['true'],
	'f': ['geojson'],
	'maxRecordCountFactor': ['4'],
	'outFields': ['*'],
	'outSR': ['102100'],
	'quantizationParameters': ['{"mode":"view","originPosition":"upperLeft","tolerance":1.058335450004235,"extent":{"xmin":-12781513.5765,"ymin":3675969.810800001,"xmax":-12138832.7603,"ymax":4441610.475400001,"spatialReference":{"wkid":102100,"latestWkid":3857}}}'],
	'resultOffset': ['0'],
	'resultRecordCount': ['4000'],
	'returnGeometry': ['true'],
	'spatialRel': ['esriSpatialRelIntersects'],
	'where': ['1=1']
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
