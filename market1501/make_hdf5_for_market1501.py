# -*- coding: utf-8 -*-
import os
import h5py
import numpy as np
from PIL import Image

def make_positive_index_market1501(train_or_test = 'train',user_name = 'ubuntu'):
    f = h5py.File('market1501_positive_index.h5')
    path_list = get_image_path_list(train_or_test = train_or_test, system_user_name = user_name)
    #0512: delete the last thumbs.db
    #path_list.pop(-1)
    index = []
    i = 0
    while i < len(path_list):
        j = i + 1
        # e.g.: 0002_c3s1_....
        # 0513: the first 4digit is the identity number
        while j < len(path_list) and path_list[j][0:4] == path_list[i][0:4]:
            # the 7th digit is the camera number, images should be taken from different cameras
            if path_list[j][6] != path_list[i][6]:
                #since using assymmetry comparison, use both (a,b) and (b,a)
                index.append([path_list[i],path_list[j]])
                index.append([path_list[j],path_list[i]])
                print len(index)
            j += 1
        i += 1
    print 'transforming the list to the numpy array......'
    # convert from list to a 1xN matrix
    index = np.array(index)
    print 'shuffling the numpy array......'
    np.random.shuffle(index)
    print 'storing the array to HDF5 file......'
    # [1] dataset name, [2] dataset content
    f.create_dataset(train_or_test,data = index)


def make_test_hdf5(user_name='ubuntu'):
    with h5py.File('test.h5') as f:
        path_list = get_image_path_list(train_or_test='test')
        #0512: delete the last thumbs.db
        #path_list.pop(-1)
        i = path_list[0][0:4]  #identity
        c = path_list[0][6]    #camera
        temp = []
        # 0512: using identity id as group name e.g.: "0001"
        fi = f.create_group(i)
        
        #use the following for loop to create a group for each of the 1501 identity
        for path in path_list:
            print path
            if path[0:4] == i:
                if path[6] == c:
                    temp.append(np.array(Image.open('./dataset/market1501/bounding_box_test/' + path)))
                else:
                    print len(temp)
                    # 0512: use camera id as the dataset name of this group
                    fi.create_dataset(c,data = np.array(temp))
                    temp = []
                    c = path[6]
                    print c
                    temp.append(np.array(Image.open('./dataset/market1501/bounding_box_test/' + path)))
            else:
                fi.create_dataset(c,data = np.array(temp))
                i = path[0:4]
                # 0512: create a new group according to the next identity
                fi = f.create_group(i)                
                print i
                c = path[6]
                print c
                temp = []
                temp.append(np.array(Image.open('./dataset/market1501/bounding_box_test/' + path)))
    
    
    
def get_image_path_list(train_or_test = 'train',system_user_name = 'ubuntu'):
    if train_or_test == 'train':
        folder_path = './dataset/market1501/bounding_box_train'
    elif train_or_test == 'test':
        folder_path = './dataset/market1501/bounding_box_test'
    elif train_or_test == 'query':
        folder_path = './dataset/market1501/query'
    assert os.path.isdir(folder_path)
    if train_or_test == 'train' or train_or_test == 'query':
        #return sorted(os.listdir(folder_path))
        #sort the list in ascending order in ascII names
        path_list = sorted(os.listdir(folder_path))
    elif train_or_test == 'test':
        #return sorted(os.listdir(folder_path))[6617:]
        # 0513: start from 6618th image, the first 6617 imgs are distractors or junks of DPM detector
        path_list = sorted(os.listdir(folder_path))[6617:]
    #0512: delete the last thumbs.db
    path_list.pop(-1)
    return path_list

def get_data_for_cmc(user_name = 'ubuntu'):
    with h5py.File('test.h5','r') as f:
        A = []
        B = []
        id_list = f.keys()
        for i in id_list:
            c_list = f[i].keys()
            c1,c2 = np.random.choice(c_list,2)
            A.append(f[i][c1][np.random.randint(f[i][c1].shape[0])])
            B.append(f[i][c2][np.random.randint(f[i][c2].shape[0])])
        return np.array(A)/255.,np.array(B)/255.

if __name__ == '__main__':
    user_name = raw_input('input your system user name:')
    make_positive_index_market1501('train',user_name=user_name)
    make_positive_index_market1501('test',user_name=user_name)
    make_test_hdf5(user_name=user_name)
