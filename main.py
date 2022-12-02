import veiw,model,controller,time,controller2,view2

while True:
    time.sleep(1/100)
    if model.sostoynie==model.SOSTOYNIE_OSVETLENIE_WAR or model.sostoynie==model.SOSTOYNIE_START_WAR:
        view2.view2()
        controller2.controller2
    controller.control()
    model.step()
    veiw.veiw()
