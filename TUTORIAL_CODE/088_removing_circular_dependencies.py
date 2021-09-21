# dialog.py
import app

class Dialog(object):
    def __init__(self, save_dir):
        self.save_dir = save_dir
    # ...

save_dialog = Dialog(app.prefs.get('save_dir'))

def show():
    # ...

##############################################

    # app.py
    import dialog

    class Prefs(object):
        # ...
        def get(self, name):

    # ...

    prefs = Prefs()
    dialog.show()

# app

Traceback (most recent call last):
  File "main.py", line 4, in <module>
    import app
  File "app.py", line 4, in <module>
    import dialog
  File "dialog.py", line 16, in <module>
    save_dialog = Dialog(app.prefs.get('save_dir'))
AttributeError: 'module' object has no attribute 'prefs'

#### reorder imports

# app.py
class Prefs(object):
    # ...

prefs = Prefs()

import dialog  # Moved
dialog.show()

# but avoid

##### Import, Configure, Run

# dialog.py
import app

class Dialog(object):
    # ...

save_dialog = Dialog()

def show():
    # ...

def configure():
    save_dialog.save_dir = app.prefs.get('save_dir')

# app.py
import dialog

class Prefs(object):
    # ...

prefs = Prefs()

def configure():
    # ...

    # main.py
    import app
    import dialog

    app.configure()
    dialog.configure()

    dialog.show()

### dynamic import

# dialog.py
class Dialog(object):
    # ...

save_dialog = Dialog()

def show():
    import app  # Dynamic import
    save_dialog.save_dir = app.prefs.get('save_dir')
    # ...

# app.py
import dialog

class Prefs(object):
    # ...
prefs = Prefs()
dialog.show()

