import argparse
import os

from file_synch import run

parser = argparse.ArgumentParser(description="Parser for a simple file synch app")
parser.add_argument("--original_root_folder", "-o",
                    type=str,
                    help="full path to root directory you wish to synch",
                    required=True)
parser.add_argument("--replica_root_folder", "-r",
                    type=str,
                    help="full path to root directory of the replica folder",
                    required=True)
parser.add_argument("--synch_period", "-p",
                    type=int,
                    help="synch period in seconds",
                    required=True)
parser.add_argument("--log_file_path", "-l",
                    type=str,
                    help="full path to a log file (include the file extension, if any")


def check_args(ogn_root, rep_root, log_file):
    return (os.path.isdir(ogn_root) and
            os.path.isdir(rep_root) and
            (log_file is None or os.path.isdir(log_file)))


if __name__ == "__main__":
    args = parser.parse_args()

    ogn_folder: str = args.original_root_folder
    rep_folder: str = args.replica_root_folder
    log: str = args.log_file_path
    period: int = args.log_file_path

    if check_args(ogn_folder, rep_folder, log):
        run(ogn_folder, rep_folder, period, log)
