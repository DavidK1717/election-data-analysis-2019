### 2019 UK election data analysis using Python
#### plot_ge_age_eu_csv.py
Creates scatter graph from raw csv files. Constituencies are represented by dots, coloured according to party (hold and gain). The positions of the dots correspond to the leave vote in the 2016 EU referendum for the constituency (x axis), and the percentage of the constituency population in the selected age range. The age range can be changed using the variables age_start and age_end.

The graph shows how constituencies with an older population and higher leave vote were more likely to vote Conservative and vice versa for Labour (see png).
#### plot_ge_age_eu_con_lab_csv.py
Same as above but filters for Conservative and Labour parties only.

#### Requirements
* matplotlib
* pandas
* seaborn

#### CSV files (relevant fields only)

##### constituency_headline.csv

<table>
<thead>
	<tr>
		<th>Column</th>
		<th>Description</th>
	</tr>
</thead>
<tbody>
	<tr>
		<td>ons</td>
		<td>Ordnance survey constituency identifier</td>
	</tr>
	<tr>
		<td>wp</td>
		<td>Winning party short identifier</td>
	</tr>
	<tr>
		<td>wpp</td>
		<td>Winning party at previous election short identifier</td>
	</tr>
	<tr>
		<td>flash</td>
		<td>Result as in "GAIN FROM LAB", "HOLD" etc</td>
	</tr>
</tbody>
</table>

Source: webscraped from [https://www.bbc.co.uk/news/election/2019/results](https://www.bbc.co.uk/news/election/2019/results). See [https://github.com/DavidK1717/election-webscraper2019](https://github.com/DavidK1717/election-webscraper2019)

##### Age_by_year_data.csv

<table>
<thead>
	<tr>
		<th>Column</th>
		<th>Description</th>
	</tr>
</thead>
<tbody>
	<tr>
		<td>PCON11CD</td>
		<td>Ordnance survey constituency identifier</td>
	</tr>
	<tr>
		<td>Age_year</td>
		<td>Single year of age</td>
	</tr>
	<tr>
		<td>Age_percent</td>
		<td>Percentage of people in the constituency of the given single year of age</td>
	</tr>
</tbody>
</table>

Source: <a href="https://commonslibrary.parliament.uk/local-data/constituency-statistics-population-by-age/" target="_blank">House of Commons Library</a>

##### eureferendum_constituency.csv

<table>
<thead>
	<tr>
		<th>Column</th>
		<th>Description</th>
	</tr>
</thead>
<tbody>
	<tr>
		<td>ons_code</td>
		<td>Ordnance survey constituency identifier</td>
	</tr>
	<tr>
		<td>leave_to_use</td>
		<td>Leave vote as a % of total vote in EU referendum</td>
	</tr>
</tbody>
</table>

Source: <a href="https://commonslibrary.parliament.uk/parliament-and-elections/elections-elections/brexit-votes-by-constituency/" target="_blank">House of Commons Library</a>
