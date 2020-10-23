from app.src.controller.MainViewController import MainViewController

from app.src.listeners.ExerciseTimeListener import ExerciseTimeListener

# @todo use normal event system
a = ExerciseTimeListener()
a.onKernelStart()

ctl = MainViewController()
ctl.index()
