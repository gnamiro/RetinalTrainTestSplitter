import os, os.path
import argparse
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from distutils.dir_util import copy_tree
import shutil


def get_args():
  parser = argparse.ArgumentParser(description='FundusPath')
  parser.add_argument('--images_path',
                      default='./Dataset')
  parser.add_argument('--output_path', default='./datasets/fundus')
  parser.add_argument('--random_state', default=29)
  parser.add_argument('--test_size', default=0.08)

  return parser.parse_args()


if __name__ == '__main__':
  args = get_args()

  good_fundus_images = './Dataset/good'
  
  train_path = f"{args.output_path}/train/good"
  test_path = f'{args.output_path}/test'

  # os.makedirs(train_path, exist_ok=True)
  # os.makedirs(f"{test_path}/good", exist_ok=True)
  # # os.makedirs(f"{test_path}/disease", exist_ok=True)
  # # os.makedirs(f"{test_path}/ambiguous", exist_ok=True)


  # copy_tree(f'{args.images_path}/disease', test_path + '/disease')
  # copy_tree(f'{args.images_path}/ambiguous', test_path + '/ambiguous')

  good_images = [name for name in os.listdir(good_fundus_images)]
  print(len(good_images))
  data = list(zip(*[iter(good_images)]*1))
  images_df = pd.DataFrame(data, columns=['healthy_fundus'])

  number_of_files = len(good_images)
  print(images_df.head())

  np.random.seed(args.random_state)
  msk = np.random.rand(number_of_files) < args.test_size
  train_files, test_files = images_df[~msk], images_df[msk]

  print(len(train_files))

  for index, _file in train_files.iterrows():
    shutil.copy2(f'{good_fundus_images}/{_file.healthy_fundus}', f'{train_path}')

  for _file in test_files:
    shutil.copy2(f'{good_fundus_images}/{_file.healthy_fundus}', f'{test_path}/good')    

