# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 19:11:13 2020

@author: Liu Tianzi
"""

import torch
from daoctor.machinelearning.model import resnet34
from PIL import Image
from torchvision import transforms
import matplotlib.pyplot as plt
import json
import os
from numpy import *
from daoctor.machinelearning import ori_path


def img_predict(img_path):

    data_transform = transforms.Compose(
        [transforms.Resize(256),
         transforms.ToTensor(),
         transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])

    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    # root_path = './all/'

    # create model
    model = resnet34(num_classes=6).to(device)
    # load model weights
    weights_path = ori_path+"/resNet34.pth"
    assert os.path.exists(weights_path), "file: '{}' dose not exist.".format(weights_path)
    model.load_state_dict(torch.load(weights_path, map_location=device))


    # read class_indict
    try:
        json_file = open(ori_path+'/class_indices.json', 'r')
        class_indict = json.load(json_file)
    except Exception as e:
        print(e)
        exit(-1)


    # load image
    #img_path = "./DSC17_2800.JPG"
    img_path=str(img_path)
    assert os.path.exists(img_path), "file: '{}' dose not exist.".format(img_path)
    img = Image.open(img_path).convert('RGB')
    plt.imshow(img)
    # [N, C, H, W]
    img = data_transform(img)
    # expand batch dimension
    img = torch.unsqueeze(img, dim=0)


    model.eval()
    with torch.no_grad():
        output = torch.squeeze(model(img.to(device))).cpu()
        predict = torch.softmax(output, dim=0)
        predict_cla = torch.argmax(predict).cpu().numpy()
    ImgIdentResult = class_indict[str(predict_cla)][1:]
    PredictAccuracy=[]
   # PredictAccuracy.append((predict[predict_cla].cpu()*100).numpy())
    PredictAccuracy.append(round(predict[predict_cla].cpu().tolist() * 100, 2))
    #PredictAccuracy = predict[predict_cla].cpu().numpy()
    PredictAccuracy=array(PredictAccuracy).tolist()

    #print(ImgIdentResult, PredictAccuracy)
    return ImgIdentResult, PredictAccuracy

