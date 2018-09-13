import os
from rappy.utils import ArgParser


if __name__ == '__main__':

    sid_file = '/Volumes/USB_SECURE1/Data/David/Pancreas/Imaging/patid_sid.csv'

    sids = {}
    header = True
    with open(sid_file, 'r') as f:
        for line in f.readlines():
            if header:
                header = False
                continue
            items = line.strip().split(',')
            sids[items[0]] = items[1]

    src_file = '/Volumes/USB_SECURE1/Data/David/Pancreas/ClinicalData/SarcopeniaOriginal.csv'

    lines = []
    header = []
    with open(src_file, 'r') as f:
        for line in f.readlines():
            if len(header) == 0:
                header = line.strip().split(',')
                continue
            items = line.strip().split(',')
            items[0] = sids[items[0]]
            lines.append(items)

    header[0] = 'SID'
    header = ','.join(header)

    dst_file = '/Volumes/USB_SECURE1/Data/David/Pancreas/ClinicalData/SarcopeniaOriginalRenamed.csv'

    with open(dst_file, 'w') as f:
        f.write(header + '\n')
        for line in lines:
            f.write(','.join(line) + '\n')
