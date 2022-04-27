import argparse
import os

from actions_toolkit import core
import mosspy

def run_moss(args):
    # Setup env
    userid = os.environ['INPUT_USER_ID']
    # Initialize MOSS
    m = mosspy.Moss(userid, args.l)
    # Base files
    for filepath in args.b:
        m.addBaseFile(filepath)
    # Submission Files
    for filepath in args.files:
        if '*' in filepath:
            m.addFilesByWildcard(filepath)
        else:
            m.addFile(filepath)
    # Send request
    url = m.send()
    # Download report
    m.saveWebPage(url, f"report.html")
    mosspy.download_report(url, ".")
    report = []
    with open('report.html', "r") as f:
        report = f.readlines()
    return report

def parse_args():
    parser = argparse.ArgumentParser(
        'action-moss',
        description='run MOSS checker',
        usage='file1 file2 file3 ... [-l language] [-d] [-b basefile1] ... [-b basefilen] [-m #] [-c "string"]'
    )
    parser.add_argument(
        'files',
        nargs='+'
    )
    parser.add_argument(
        '-l',
        required=False,
        help="Specifies the source language of the tested programs.",
        type=str,
        default='c',
    )
    parser.add_argument(
        '-d',
        required=False,
        help="Specifies that submissions are by directory, not by file.",
        action='store_true',
    )
    parser.add_argument(
        '-b',
        required=False,
        help="Names a base file. Multiple -b options are allowed.",
        action='append',
        nargs='*',
        default=[]
    )
    parser.add_argument(
        '-m',
        required=False,
        help="Tthe maximum number of times a given passage may appear before it is ignored",
        type=int,
        default=10,
    )
    parser.add_argument(
        '-c',
        required=False,
        help="Supplies a comment string that is attached to the generated report.",
        type=str,
    )
    parser.add_argument(
        '-n',
        required=False,
        help="Determines the number of matching files to show in the results.",
        type=int,
        default=250,
    )
    return parser.parse_args(os.environ['INPUT_ARGS'].split(' '))

def main():
    try:
        args = parse_args()
        report = run_moss(args)
        core.set_output('report', report)
    except Exception as e:
        core.set_failed(str(e))
        
if __name__ == "__main__":
    main()
