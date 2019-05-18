import numpy as np
import tensorflow as tf
from sklearn import  datasets
from keras.models import load_model
from flask_restful import reqparse
from keras import backend as K


class IrisController:
    def __init__(self):
        global model,graph,target_names
        K.clear_session()
        model=load_model('iris/saved_model/iris_model.h5')
        graph=tf.get_default_graph()
        target_names=datasets.load_iris().targer_names
    def service_model(self):
        parser=reqparse.RequestParser()
        parser.add_argument('sepal_length',required=True,type=float)
        parser.add_argument('sepal_width', required=True, type=float)
        parser.add_argument('petal_length', required=True, type=float)
        parser.add_argument('petal_width', required=True, type=float)
        args=parser.parse_args()
        features=[args['sepal_length'],
                 args['sepal_width'],
                 args['petal_length'],
                 args['petal_width']]
        features=np.reshape(features,(1,4)) # 전치 ;행과 열 바꿈
        with graph.as_default():
            Y_pred=model.predict_classes(features)
        result={'species': target_names[Y_pred[0]]}
        return result

