# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 01:13:10 2019

@author: DataStunner
"""
import cv2
import numpy as np 
import pandas as pd
from scipy.ndimage import rotate

class load_images:
    def __init__(self, image_path):
        self.image_path = image_path
    def trans_rot(self, image, angles = [90, 180, 270]):
        """ Return rotated images for given angles. 
        """
        res = [image]
        for angle in angles:
            res.append(rotate(image, angle))
        return(res)
    def load_from_gt(self, gt, img_name, gt_name, img_size = 384, 
                     rot = False, norm = True):
        for image_name in gt['img_name'].values:
            try:
                image = cv2.imread(image_name)
                image = cv2.cvtColor(cv2.resize(image(img_size, 
                                                      img_size), 
                                                      0, 0,
                                                      cv2.INTER_LINEAR), 
                                                      cv2.COLOR_BGR2RGB)
                image = image.astype(np.float32)
                if norm:
                    image = np.multiply(image, 1.0/255.0)
                label = gt[gt['img_name'] == image_name]['gt_name'].values
                if rot:
                    image = self.trans_rot(image)
                    n_rots = len(images)
                    label = [label]*n_rots
                    image_name = [image_name]*n_rots
                    self.images.extend(image)
                    self.img_names.extend(image_name)
                    self.labels.extend(label)
                else:
                    self.images.append(image)
                    self.img_names.append(image_name)
                    self.labels.append(label)
            except:
                print('{} is not readable')
            

