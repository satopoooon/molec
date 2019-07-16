import pandas as pd
import numpy as np
import re as re

from features.base import Feature, get_arguments, generate_features

Feature.dir = 'features'


class MoleculeSize(Feature):

    def create_features(self):

        molecule_name_array = np.unique(structures["molecule_name"])

        atom_size_list = []
        molecule_name_list = []

        for molecule_name in molecule_name_array:
            atom_size = np.amax(structures[structures["molecule_name"] == molecule_name]["atom_index"])
            atom_size_list.append(atom_size)
            molecule_name_list.append(molecule_name)

        molecule_df = pd.DataFrame()
        molecule_df["molecule_name"] = molecule_name_list
        molecule_df["atom_size"] = atom_size_list

        self.train = merge_df(train, molecule_df, "molecule_name", "molecule_name")
        self.test = merge_df(test, molecule_df, "molecule_name", "molecule_name")


def merge_df(df1, df2, column1, column2):
    df = pd.merge(df1, df2, how="left",
                  left_on=column1,
                  right_on=column2)
    return df


if __name__ == '__main__':
    args = get_arguments()

    train = pd.read_feather('../data/input/train.feather')
    test = pd.read_feather('../data/input/test.feather')
    structures = pd.read_feather('../data/input/structures.feather')

    generate_features(globals(), args.force)