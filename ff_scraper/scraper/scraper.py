import requests
from bs4 import BeautifulSoup


def scrape(url: str, table_id: str) -> tuple:
    """ Scrapes the :url for the provided :table_id. Returns a tuple of (labels,
        stats)

    The first item in the returned list is the headers for the data. Each 
    subsequent item is the stats for a particular player. We assume that the 
    first <tr> within the table contains the <th> that describes the columns. 
    We assume each <tr> thereafter contains the <td>'s that describe the data 
    for a particular player for that row.

    Args:
        url (str): The url of the html page containing the stats
        table_id (str): The id of the table on the apge

    Returns:
        tuple: A tuple of (list, list) where [0] is a list of the column headers
            and [1] is a list of lists of the player statistics from the rows.
    """

    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    stats_table = soup.find(id=table_id)
    rows = stats_table.findAll('tr')
    stat_headers = [i.getText() for i in rows[0].findAll('th')]
    stat_lines = []
    for row in rows[1:]:
        stat_lines.append([col.getText() for col in row.findAll('td')])

    return (stat_headers, stat_lines)
    
