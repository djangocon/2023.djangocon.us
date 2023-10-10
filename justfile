set dotenv-load := false

alias social := screenshots

# Replace DOMAIN with your Netlify link if our templates are not deployed yet.

DOMAIN := "https://2023.djangocon.us"
IMAGE_SIZE := "1024x512"

# IMAGE_SIZE = "1400x700"

@_default:
    just --list

@build:
    docker-compose build

@down:
    docker-compose down

@fmt:
    just --fmt --unstable

@lint:
    pre-commit run --all-files

@logs *ARGS:
    docker-compose logs {{ ARGS }}

@screenshots:
    python bin/process.py generate-shots > ./shots.yml
    shot-scraper multi --no-clobber ./shots.yml

@test:
    bundle exec rake test

@start *ARGS:
    just up --detach {{ ARGS }}

@stop *ARGS:
    just down {{ ARGS }}

@up *ARGS:
    docker-compose up {{ ARGS }}

@update:
    rm -f ./bin/requirements.txt
    pip install -r ./bin/requirements.in
    pip-compile ./bin/requirements.in
