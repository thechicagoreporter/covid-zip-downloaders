"""
Download Florida's COVID ZIP code data
"""
import click
import requests
from urllib.parse import urlparse, parse_qs

URL_ROOT = 'https://services1.arcgis.com/CY1LXxl9zlJeBuRZ/arcgis/rest/services/COVID_19_Cases_in_Florida_by_Zip_Code/FeatureServer/0/query'
PARAMS = {
	'f': ['geojson'],
	'where': ['1=1'],
	'returnGeometry': ['true'],
	'spatialRel': ['esriSpatialRelIntersects'],
	'maxAllowableOffset': ['4891'],
	'geometry': ['{"xmin":-10018754.171396948,"ymin":2504688.542852983,"xmax":-7514065.628548959,"ymax":5009377.08570097,"spatialReference":{"wkid":102100,"latestWkid":3857}}'],
	'geometryType': ['esriGeometryEnvelope'],
	'inSR': ['102100'],
	'outFields': ['*'],
	'outSR': ['102100'],
	'resultType': ['tile']
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