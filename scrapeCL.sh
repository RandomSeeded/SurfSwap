#!/bin/bash

# Scrape craigslist (run through crontab)

#!/bin/bash
parent_path=$( cd "$(dirname "${BASH_SOURCE}")" ; pwd -P )
cd "$parent_path"
python3 ./server/clScraper.py

