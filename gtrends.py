import os, sys


def squeeze(fdir):
    """
    :param fdir:
    :return:
    """
    if fdir[-4:].lower() == ".csv":
        sep = ","
    elif fdir[-4:].lower() == ".tsv":
        sep = "\t"
    else:
        raise Exception("The file name should have one of the following extensions: .csv .tsv")
    f = open(fdir)
    header = []
    d = dict()
    for idx, line in enumerate(f.readlines()):
        if idx < 2:
            continue
        elif idx == 2:
            header = line.strip().split(sep)[1:]
        else:
            if line.strip() == "":
                break
            else:
                row = line.strip().split(sep)
                event_date = row[0]
                event_year = event_date.split('-')[0].strip()
                if event_year not in d:
                    d[event_year] = dict()
                    for h in header:
                        d[event_year][h] = []
                for hid, v in enumerate(row[1:]):
                    h = header[hid]
                    if v =="<1":
                        vv = 0.5
                    else:
                        vv = float(v)
                    d[event_year][h].append(vv)
    return d


def aggregate(d):
    """
    :param d: dict from squeeze
    :return: aggregated dict
    """
    for y in d.keys():
        for h in d[y].keys():
            d[y][h] = sum(d[y][h]) * 1.0 / len(d[y][h])
    return d


def export(d):
    years = d.keys()
    header = d[years[0]].keys()
    line = ",".join(header)
    line = "year,"+line
    print line
    lines = [line+"\n"]
    for y in sorted(years):
        line = y
        for h in header:
            line += ",%.2f" % (d[y][h])
        print line
        line += "\n"
        lines.append(line)


def workflow(fdir):
    d = squeeze(fdir)
    d = aggregate(d)
    export(d)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Expecting the path to your csv file")
    else:
        workflow(sys.argv[1])



