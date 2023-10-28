import activ_object


class Tp_object(activ_object.Activ_object):
    def __init__(self,x,y,w,h,tp_x,tp_y,igroc):
        activ_object.Activ_object.__init__(self,self.tp,x,y,w,h,"picture/img.png")
        self.tp_x=tp_x
        self.tp_y=tp_y
        self.igroc=igroc

    def tp(self,data):
        self.igroc.rect_igroc.x=self.tp_x
        self.igroc.rect_igroc.y=self.tp_y

    @classmethod
    def make_portal(my_class,x,y,w,h,x_1,y_1,igroc,obshie):
        a=my_class(x,y,w,h,x_1,y_1,igroc)
        b=my_class(x_1,y_1,w,h,x,y,igroc)
        obshie+= [a,b]


