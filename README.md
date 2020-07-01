# HLTV Scraper

A web scraper designed specifically for hltv.org

## Some general information

This particular web scraper makes use of the selenium web driver and pandas to return a dataframe with data according to the arguments listed below.
Please note that there is no support for rotating proxies at this moment time, and I hope to add this at a later date. For now, it uses a random time delay
between scraping pages in order to extract data. I have tested it by running it for a full day without being blocked by hltv, so it proves to work well, however for
large data sets (particularly using `scrape_range()`), this does mean that it can take hours to extract certain dataframes.

## Getting started

To import this file, use `import hltv_scraper`. The main functions that you want to use are:

- `scrape(driver, category, date_range, map)`
- `scrape_range(driver, category, date_range, map)`

The `driver` argument will accept any selenium webdriver instance, and needs to be running before calling these functions.
Take a look at the docstring for the two functions to get a better idea of what arguments to pass in using `help(scrape)` / `help(scrape_range)`.

Briefly, the scraper will look at the 'stats' page, and will aim to collect data from any of these subcategories:

- Teams
- Matches
- Players

There is currently no option to clean dataframes using this scraper, so any functions carried out on the datasets will have to be cleaned by the user.

## Have Fun!
