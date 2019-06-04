import argparse

from flask import Flask

from ecountry.server.config import Config

app = Flask(__name__)


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', '-c', default='ecountry.conf')
    return parser


def main():
    args = get_parser().parse_args()
    config = Config(args.config)
    app.run(
        host=config.get('server', 'host'),
        port=config.get('server', 'port'),
        debug=config.get('server', 'debug')
    )


if __name__ == '__main__':
    main()
