import veiw,model,controller,time,controller2,view2,model2

while True:
    time.sleep(1/100)
    if model.sostoynie==model.SOSTOYNIE_OSVETLENIE_WAR or model.sostoynie==model.SOSTOYNIE_START_WAR:
        controller2.controller2()
        model2.step()
        view2.view2()
    else:
        controller.control()
        model.step()
        veiw.veiw()
