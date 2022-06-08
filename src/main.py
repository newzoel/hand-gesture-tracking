import argparse

import handTrackingImage as HandTrackImg
import handTrackingVideo as HandTrackVid


def main():
    "Main Method"
    argparser = argparse.ArgumentParser(
        description='Hand Tracking Module')
    #positional argument
    argparser.add_argument(
        'input',
        default='online',
        help='Type of Input [online, offline]'
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
    if(args.input != 'online'):
        HandTrackImg.handTrackingImage(args.path)
    else:
        HandTrackVid.handTrackingVideo(args.path)


if __name__ == '__main__':
    main()