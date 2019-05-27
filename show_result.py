import sys
from argparse import ArgumentParser

import matplotlib.pyplot as plt
import pandas as pd

def show_result(res):
    res = res.reset_index(drop=True)
    res = res.reindex(list(range(res.shape[0])))
    plot = res.plot(title='2048 average score')
    plot.set_xlabel("per 1000")
    plot.set_ylabel("avg score")
    
    plt.show()


def main(args):
    source1 = pd.read_csv(args.file_name1, index_col=0, names=["idx", "before_state"])
    source2 = pd.read_csv(args.file_name2, index_col=0, names=["idx", "after_state"])
    source = pd.concat([source1, source2], axis=1, sort=False)
    show_result(source)


def get_args():
    parser = ArgumentParser()
    parser.add_argument("file_name1", help="your csv file name", type=str, default='')
    parser.add_argument("file_name2", help="your csv file name", type=str, default='')
    return parser.parse_args()


if __name__ == "__main__":
    main(get_args())

    sys.stdout.flush()
    sys.exit()
