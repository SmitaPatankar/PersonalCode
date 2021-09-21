import argparse


def parse_args(args):
    parser = argparse.ArgumentParser()
    for arg in args:
        parser.add_argument(
            arg.get("option"), default=arg.get("default"), help=arg.get("help")
        )
    args = parser.parse_args()
    return args


args = parse_args(
        [
            {"option": "--id", "help": "Identification Number"},
            {
                "option": "--name",
                "help": "Name",
            }
        ]
    )

print(args.id)
print(args.name)

# PYTHON argparse_basics.py --id 1 --name smita
# 1
# smita
