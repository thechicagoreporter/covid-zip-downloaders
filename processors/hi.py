"""
Download Hawaii's COVID ZIP code data
"""
import click
import requests
from urllib.parse import urlparse, parse_qs

URL_ROOT = 'https://services.arcgis.com/HQ0xoN0EzDPBOEci/arcgis/rest/services/covid_web_map/FeatureServer/0/query'
PARAMS = {
	'f': ['geojson'],
	'where': ['1=1'],
	'returnGeometry': ['true'],
	'spatialRel': ['esriSpatialRelIntersects'],
	'outFields': ['*'],
	'maxRecordCountFactor': ['2'],
	'outSR': ['102100'],
	'resultOffset': ['0'],
	'resultRecordCount': ['4000'],
	'cacheHint': ['true'],
	'quantizationParameters': ['{"mode":"view","originPosition":"upperLeft","tolerance":4.777061637456608,"extent":{"xmin":-17839020.866323866,"ymin":2142384.0950807394,"xmax":-17224704.327052422,"ymax":2539547.753445243,"spatialReference":{"wkid":102100,"latestWkid":3857}}}']
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