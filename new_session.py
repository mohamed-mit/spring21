import threading
from IPython.display import display
import ipywidgets as widgets
import time
from zmq.eventloop.ioloop import IOLoop

progress = widgets.FloatProgress(value=0, min=0, max=7200)
display(progress)

def run(progress, ioloop):
    def update_progress(i, progress=progress):
        progress.value = i

    for i in range(60):
        time.sleep(1)
        ioloop.add_callback(update_progress, i)

def start_session(*args, **kwargs):
    print("Session started, will remain active for two hours as counted by the progress bar")
    thread = threading.Thread(target=run, args=(progress, IOLoop.instance()))
    thread.start()