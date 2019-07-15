import pandas as pd
import numpy as np
import re as re

from features.base import Feature, get_arguments, generate_features

Feature.dir = 'features'


class Molecule_size(Feature):
    def create_features(self):
        # self.train[''] = train['Pclass']
        # self.test['Pclass'] = test['Pclass']
        molecule_name_array = np.unique(structures["molecule_name"])

        atom_size_list = []
        molecule_name_list = []

        for molecule_name in molecule_name_array:
            atom_size = np.amax(structures[structures["molecule_name"] == molecule_name]["atom_index"])
            atom_size_list.append(atom_size)
            molecule_name_list.append(molecule_name)


if __name__ == '__main__':
    args = get_arguments()

    train = pd.read_feather('../data/input/train.feather')
    test = pd.read_feather('../data/input/test.feather')
    structures = pd.read_feather('../data/input/structures.feather')

    generate_features(globals(), args.force)