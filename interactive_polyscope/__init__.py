import time
import asyncio
import traceback

import ipykernel.eventloops
import polyscope as ps
import nest_asyncio
nest_asyncio.apply()

show = False
user_cb = None

def patched_show():
    global show
    show = True

def patched_set_user_callpack(callback):
    global user_cb
    user_cb = callback

@ipykernel.eventloops.register_integration('polyscope')
def loop_ps(kernel):
    event_loop = asyncio.get_event_loop()
    poll_interval = kernel._poll_interval
    last = time.time()
    og_show = ps.show
    og_set_cb = ps.set_user_callback
    ps.show = patched_show
    ps.set_user_callback = patched_set_user_callpack

    def poll():
        nonlocal last
        now = time.time()
        if now-last > poll_interval:
            last = now
            loop = asyncio.get_event_loop()
            loop.run_until_complete(kernel.do_one_iteration())

    def cb():
        poll()
        if user_cb is not None:
            try:
                user_cb()
            except:
                traceback.print_exc()

    def run_polyscope():
        global show
        nonlocal last
        last = time.time()

        ps.init()
        og_set_cb(cb)
        while True:
            if show:
                show = False
                og_show()
            else:
                now = time.time()
                time_delta = kernel._poll_interval-(now-last)
                if time_delta > 0:
                    time.sleep(time_delta)
                poll()

    run_polyscope()
