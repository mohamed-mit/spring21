import threading
from IPython.display import display,clear_output, HTML
import ipywidgets as widgets
import time
from zmq.eventloop.ioloop import IOLoop
import time
total = 7200
progress = widgets.FloatProgress(value=0, min=0, max=total)
display(progress)


def run(progress, ioloop):
    def update_progress(i, progress=progress):
        progress.value = i

    for i in range(total):
        time.sleep(1)
        #remaining = time.strftime('%H:%M:%S', time.gmtime(total-i))
        #s = "Session will expire in "+remaining
        #clear_output(wait=True)
        #display(HTML(s), display_id = True)
        #display(progress)
        ioloop.add_callback(update_progress, i)
        


def start_session(*args, **kwargs):
    print("Session started, will remain active for two hours as counted by the progress bar")
    thread = threading.Thread(target=run, args=(progress, IOLoop.instance()))
    thread.start()