import os
c = get_config()

# Kernel config
c.IPKernelApp.pylab = 'inline'  # if you want plotting support always

# Notebook config
#c.NotebookApp.certfile = os.path.join(os.getcwd(), u'mycert.pem')
#c.NotebookApp.ip = '*'
c.NotebookApp.open_browser = True
c.NotebookManager.notebook_dir = os.path.join(os.env("HOME"), "Desktop", "Tutorial")
# It's a good idea to put it on a known, fixed port
c.NotebookApp.port = 9999
#c.NotebookApp.password = u'sha1:60e7d2645fb4:97064d28bad2a4a12950055c830d9637b652c9ec'
