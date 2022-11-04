import veiw,model,controller,time

while True:
    time.sleep(1/100)
    controller.control()
    model.step()
    veiw.veiw()
