import model,time

def step():
    if time.time() - model.go_to_next_lvl > 2.5 and model.sostoynie == model.SOSTOYNIE_POTEMNENIE_WAR:
        model.sostoynie=model.SOSTOYNIE_START_WAR