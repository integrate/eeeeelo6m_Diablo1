import real_world_object


class Activ_object(real_world_object.Real_world_object):
    def __init__(self,activaciy,x,y,w,h,cartinka,nospawn={},base_nospawn=0):
        real_world_object.Real_world_object.__init__(self,x,y,w,h,cartinka,nospawn,base_nospawn,True)
        self.activaciy=activaciy

    def activate(self,data):
        self.activaciy(data)
