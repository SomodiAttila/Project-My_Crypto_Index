# Project-My_Crypto_Index
I created a crypto index based on financial, social media and development metrics.

## Goal

The goal of this project was to create an index where I don't just take into consideration the financial metrics but also social media and development.

## Index methodology

- I used the 90 day average of: **financial metrics** (market cap, volume) and **community metrics** (social media, development) to select the 10 cryptos of the index.
- *Social media metrics*: total of twitter, reddit, telegram, bitcointalk (could have also used sentiment analysis)
- *Development metrics*: tracking the number of GitHub events that the project organization generated (could have also used web traffic, number of developers, etc.)
- The index only includes layer 1 solutions.
- Used the *Fisher price index* for calculating the index value.
- Since it is a draft project for the index, it does not include any divisor tuning or more advanced data from more expensive API packages.
- I automated the calculation with the *index_calculation* script to calculate the given days value every day at 17:00 CET.

## Data

I used the **Coinmarketcap API** for the financial metrics and the **Sanbase API** for the community metrics.

More info about how the community metrics are calculated, can be found here:
- github activity (https://academy.santiment.net/metrics/development-activity/)
- social media (https://academy.santiment.net/sanbase/social-trends-search/#gatsby-focus-wrapper)
