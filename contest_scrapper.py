import requests
from bs4 import BeautifulSoup


contest_url = 'https://codeto.win/contest/43/problem/M'

codetowin_session = "eyJpdiI6Im1tMXVKdjFPZUJZMTlKUXVhUEV6NXc9PSIsInZhbHVlIjoid2I5R0ljZ2JUSElXenZweU9iRjd3VTFkbkVYdTdhZTVmcGZ2YUd4cnhXaExBYk5oc2t5Q2h2TDF5ckFsM3RMUnBQWW1vbFRSSUhYaGNQVGpxYlc0NnBVWXlLaEU5Nk9TVlRjVWViK3NXSTJIMGoxcEtvUFloTlRFSVhRaGZrdDMiLCJtYWMiOiIyYjAyZDE4ZWUzZGRlZDgwMDZhNGE5MjVhYTEzYTYyN2NhMTk5NThjZjMyYTAzNzk5NTVhY2IwNzM5ZDY4YjU5In0%3D"
XSRF_TOKEN = "eyJpdiI6ImdEUmZzR2NxUnora1EwMFdaRElpRHc9PSIsInZhbHVlIjoiVVFNdzNOWW5SUTN2WnNLMEt3YzFxUVpXSE1PZU9RdndFS0RSejJpS0FWaWRlcGlscm1MWXdxWmxtSk5zK2hER2htbVwvTmd2cVVoUUdwdWJZeDdXUENyejFmTTFndHUrc1ViMnpyZzRxWEw4SDl2SDJ0bEN2clp2MkQxNkRzT1BIIiwibWFjIjoiZWEzYTE1Y2Y4ZmEzMDI3NzA0ZWQ2ZjI0OTJjOGVjNjZkN2VkYjU0M2ZiYzA1Mjk3MDVhODg4NTAxNjdjMzc5MCJ9"

cookies = {
	'codetowin_session': codetowin_session,
	'XSRF-TOKEN':XSRF_TOKEN

}

content = requests.get(
	url=contest_url,
	cookies=cookies
	).content

soup = BeautifulSoup(content,'lxml').find_all('div',class_='row')[1]

problem_name = soup.find_all('div', class_="col s12 m8 center")[0].select('h4')[0].text.strip()
problem_statement = soup.select('div#statement')[0]
problem_input = soup.select('div#input_format')[0].select('p')[0]
problem_output = soup.select('div#output_format')[0].select('p')[0]
samples = soup.select('div#samples')[0].find_all('div',class_='row')

markdown = f'''# [{problem_name}]({contest_url})

{problem_statement}

## Input
 
{problem_input}

## Output
 
{problem_output}

## Samples

'''

for sample in samples:
	_sample = f'''### Input

```
{sample.find_all('div',class_='sample')[0].text.strip()}
```

### Output

```
{sample.find_all('div',class_='sample')[1].text.strip()}

```
'''
	markdown +=_sample

markdown += f'''## My Approach
```c++

```
'''

with open(f"{problem_name.replace(' ','-').replace('.','')}.md",'w') as f:
	f.write(markdown)