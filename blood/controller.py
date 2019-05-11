from blood.model import BloodModel
class BloodController:
    def __init__(self,weight, age):
        self._model=BloodController()
        self._weight=weight
        self._age=age

    def blood(self):
        weight=self._weight
        age=self._age
        print("들어온 weight={},age={}".format(weight,age))

        sess=tf.Session()
        saver