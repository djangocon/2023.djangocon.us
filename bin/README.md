# HOWTO: import schedule from pretalx

## Prerequisites

1. Clone this repo (assumed path: `~/code/<year.djangocon.us>`)
2. Clone https://github.com/djangocon/pretalx-api-import (assumed path: `~/code/pretalx-api-import`)
3. Set up virtual environments in both repos
4. In this repo, `pip install wheel && pip install -r bin/requirements.txt`
   (You can put the two repos wherever, but it's easiest if they're in the same directory)

## Load the data

1. Download both the schedule and speaker list (confirmed talks only) as JSON
2. Import speakers: from the pretalx-api-import folder, run `python main.py speakers /path/to/pretalx-speakers.json --output-folder ../<year>.djangocon.us`
3. Import schedule: from the pretalx-api-import folder, run `python main.py main /path/to/pretalx-sessions.json --output-folder ../<year>.djangocon.us`
4. Generate breaks/lunch/etc.: from this repo: run `python bin/process.py generate-2023-placeholders --create-keynotes 2023-10-15` (`2023-10-15` is the Sunday before talks start, which is usually tutorial day but is not for 2023)
5. Reformat: `python bin/process.py fmt`
6. Commit the `_schedule` folder
