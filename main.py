import veiw,model,controller,time,controller2,view2,model2
# def sjd(word,/,word_2,abvgaga,*args,a,c,**kwargs):
#     for a in args:
#         print(word+' '+a)
# sjd('ку','a','a','s','f','r','x','n')
# exit()


while True:
    # time.sleep(1/300)

    if model.sostoynie==model.SOSTOYNIE_START_WAR:
        controller2.controller2()
        model2.step()
        view2.view2()
    else:
        controller.control()
        model.step()
        veiw.veiw()
