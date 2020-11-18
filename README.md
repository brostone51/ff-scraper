# ff-scraper

A super simple webscraper for fantasy statistics from a certain popular football
stats website. Technically, any site that has a `<table>` of stats, with a `<tr>`
that has `<th>` that define the header values and subsequent `<tr>` with `<td>` that
define statistics for those header values for a row will be parseable.

A sample invocation of the project would be:

```bash
python . ./inputs.txt
```

Which will write `.csv` files to the current directory for each input row.

## Input file

A sample input file is given at `./inputs.sample.txt`. Each line in the input file
should have 3 comma separated values. The first, is the name you want the output
`.csv` file to have. As an example, you might want `2019qb` or `2020wrt`. The second
value should be the url to fetch the HTML data from. The final argument is the id
of the table element where the data can be found. An example might be `rushing` or
`passing`.
