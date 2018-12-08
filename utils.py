import numpy as np
from os import walk
import os, shutil
from os.path import splitext
import pandas as pd
from scipy.io import loadmat

def load_file(file_path):
    if splitext(file_path)[1] == '.mat':
        # print('        Loading ', file_path)
        x = loadmat(file_path)
        return x
    elif splitext(file_path)[1] == '.csv':
        # print('        Loading ', file_path)
        data = pd.read_csv(file_path)
        return data
    else:
        # print('        ', 'unsupported format')
        return None

def get_data(dataset=None):
    data = {}
    for x in walk('data'):
        if x[0] == 'data':
            for datasets in x[1]:
                data[datasets] = {}
        else:
            splt = x[0].split('/')
            if len(splt) == 3:
                if splt[1] != 'ofc-3':
                    for subject in x[1]:
                        data[splt[1]][subject] = {}
                else:
                    for tpe in x[1]:
                        data[splt[1]][tpe] = {}
            elif splt[1] != 'ofc-3':
                if len(splt) == 4:
                    for sess in x[1]:
                        data[splt[1]][splt[3]][sess] = {}
                elif len(splt) == 5:
                    # Load .mat files
                    for file in x[2]:
                        data[splt[1]][splt[3]][splt[4]][file] = load_file('/'.join(splt) + '/' + file)
            else:
                if len(splt) == 4:
                    if splt[3] == 'data_behav':
                        # Load .csv files
                        for file in x[2]:
                            data[splt[1]][splt[3]][file] = load_file('/'.join(splt) + '/' + file)
                    else:
                        # Load .mat file
                        for file in x[2]:
                            data[splt[1]][splt[3]][file] = load_file('/'.join(splt) + '/' + file)
    return data[dataset] if dataset else data

def delete_files_in_folder(folder):
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            else:
                os.rmdir(file_path)
        except Exception as e:
            print(e)
            return False
    return True
