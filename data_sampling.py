import os
import pandas as pd


def main():
    df = pd.read_csv(os.path.join('data', 'train.csv'))

    usr = df['installation_id'].drop_duplicates()

    sel_usr = usr.sample(170)

    sel_df = df.loc[df['installation_id'].isin(sel_usr)]

    sel_df.to_csv(os.path.join('data', 'sample_train.csv'), index=False)


if __name__ == '__main__':
    main()
