#!/usr/bin/env python
import subprocess
from multiprocessing import Pool
import os
def run(task):
        src = "/home/student-00-12f467239548/data/prod/"+task
        dest = "/home/student-00-12f467239548/data/prod_backup/"+task
        subprocess.call(["rsync", "-arq", src, dest])
tasks = os.listdir("/home/student-00-12f467239548/data/prod")
p = Pool(len(tasks))
p.map(run,tasks)
