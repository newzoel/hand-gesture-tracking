import argparse

import handTrackingImage as HandTrackImg


def main():
    "Main Method"
    argparser = argparse.ArgumentParser(
        description='Hand Tracking Module')
    #positional argument
    argparser.add_argument(
        'input-type',
        default='online',
        help='Type of Input'
    )
    #optional argument
    argparser.add_argument(
        '-p',
        '--path',
        action='store',
        help='directory path for input data'
    )
    argparser.add_argument(
        '-s',
        '--save-to',
        action='store',
        metavar='OUT',
        help='directory path to save output'
    )

    args = argparser.parse_args()
    if(args.path != None):
        HandTrackImg.handTrackingImage(args.path)




if __name__ == '__main__':
    main()