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
  parser.add_argument('--eye_dir', default='left')
  parser.add_argument('--output_path', default='./datasets/fundus')
  parser.add_argument('--random_state', default=29)
  parser.add_argument('--test_size', default=0.08)

  return parser.parse_args()

def copy_good_samples(good_images):
  data = list(zip(*[iter(good_images)]*1))
  images_df = pd.DataFrame(data, columns=['healthy_fundus'])

  number_of_files = len(good_images)
  print(images_df.head())
  msk = np.random.rand(number_of_files) < args.test_size
  train_files, test_files = images_df[~msk], images_df[msk]

  print(len(train_files))
  num = 0
  for index, _file in train_files.iterrows():
    # print(index)
    num += 1
    shutil.copy2(f'{good_fundus_images}/{_file.healthy_fundus}', f'{train_path}')
    if(num > 510):
      break

  num = 0
  for index, _file in test_files.iterrows():
    # print(index)
    num += 1
    shutil.copy2(f'{good_fundus_images}/{_file.healthy_fundus}', f'{test_path}/good')  
    if(num > 30):
      break

def copy_disease_samples(disease_images):
  data = list(zip(*[iter(disease_images)]*1))
  images_df = pd.DataFrame(data, columns=['unhealthy_fundus'])

  number_of_files = len(good_images)
  print(images_df.head())
  num = 0
  for index, _file in images_df.iterrows():
    # print(index)
    num += 1
    shutil.copy2(f'{disease_fundus_images}/{_file.unhealthy_fundus}', f'{test_path}/disease')
    if(num > 100):
      break

def getEyes(path, direction):
  _list = []
  for name in os.listdir(path):
    if(name.find(direction) != -1):
      _list.append(name)
    
  return _list

if __name__ == '__main__':
  args = get_args()
  eye_dir = '_1.jpg' if args.eye_dir =='left' else '_2.jpg'

  np.random.seed(args.random_state)
  good_fundus_images = './Dataset/good'
  disease_fundus_images = './Dataset/disease'
  
  train_path = f"{args.output_path}/train/good"
  test_path = f'{args.output_path}/test'

  os.makedirs(train_path, exist_ok=True)
  os.makedirs(f"{test_path}/good", exist_ok=True)
  os.makedirs(f"{test_path}/disease", exist_ok=True)
  # os.makedirs(f"{test_path}/disease", exist_ok=True)
  # os.makedirs(f"{test_path}/ambiguous", exist_ok=True)


  # copy_tree(f'{args.images_path}/disease', test_path + '/disease')
  # copy_tree(f'{args.images_path}/ambiguous', test_path + '/ambiguous')

  # good_images = [name for name in os.listdir(good_fundus_images)]
  good_images = getEyes(good_fundus_images, eye_dir)
  print(len(good_images))
  copy_good_samples(good_images)

  # disease_images = [name for name in os.listdir(disease_fundus_images)]
  disease_images = getEyes(disease_fundus_images, eye_dir)
  print(len(disease_images))
  copy_disease_samples(disease_images)


