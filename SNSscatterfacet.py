import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

def sns_scatterfacet():
    """
    :input: calls filehelper, which provides and saves last valid file+PWD.
    'named' is the variable used to call the plot Fn

    :return: scatterplot
    """
    csv_path = filehelper()
    dfd = pd.read_csv(csv_path)
    named = sns.catplot(x="Group", y="Relative fold change", col="Target",
                        hue="Type",
                        kind="strip", data=dfd,
                        jitter=True, dodge=True)
    plt.ylim([0, 5])
    plt.show(named)

def filehelper():
    """
    Main purpose of filehelper is to check and handle the cache;
    which gives the last known valid input, good for rapidly testing
    SNS plots

    save_path is hardcoded, you'll need to change it per computer
    input_PWD/filename.csv, only csv is accepted
    output "Z", is the csv file to be fed into SNS plot.

    """
    save_path = '/Users/smoran/Documents/PyCache/SNStemp.rtf'

    if os.path.isfile(save_path):
        with open(save_path, "r") as file1:
            print("last valid file path accessed:")
            print(file1.readlines()[-1])
    else:
        print('Writing new cache')
        with open("SNStemp.rtf", "w+") as f:
            f.write("No prior entries")
            f.close()

    csv_path = input("Specify file pathway:")
    try:
        if os.path.exists(csv_path):
            with open(save_path, "w") as file1:
                file1.write(csv_path)
                return csv_path
    except FileNotFoundError:
        print ('{} not valid directory'.format(csv_path))
        exit()

sns_scatterfacet()