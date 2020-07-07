# gisops-plugin-tutorial
Following https://gis-ops.com/qgis-3-plugin-tutorial-plugin-development-reference-guide/ on how to create a QGIS plugin


# open Qgis
(outside container)
```
/plugin_dev/run_qgis.sh
```
plugin_dev/Dockerfile Copies the plugins to the QGIS image so it can be loaded when launching QGIS, they are specified indivdualy atm so will need to add new plugins to it


# open Qt
(outside container)
```
./plugin_dev/run_qt.sh
```

# zip plugin
(in container)
```
zip -r dist/quick_api_v0.1.zip quick_api
```

# after editing gui

##  Compile resource.qrc
You will have to compile the resources.qrc to Python code, so that your plugin understands which files are available from the Qt resource store. This will basically just byte encode the images into the format that QGIS can read:

pyrcc5 -o resources.py resources.qrc#


## Compile GUI

Now, that you did changes to the resources.qrc store in Qt Designer, you unfortunately have to rebuild your GUI logic a little, otherwise a very annoying bug will be triggered.

First, you need to compile the UI file to a Python file.

```
pyuic5 --from-imports --resource-suffix '' quick_api_dialog_base.ui > quick_api_dialog_base.py
```
    --pyuic5 translates the quick_api_dialog_base.ui file to the Python representation
    --from-imports lets the resources.py file be imported from . (see last line in the new file quick_api_dialog_base.py)
    --resource-suffix '' will import resources.py (i.e. without a suffix), while the default would try to import resource_rc.py

To use the new file, in ./quick_api_dialog.py, remove these lines:

```
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'quick_api_dialog_base.ui'))
```

and add an import statement for your new quick_api_dialog_base.py file:

from .quick_api_dialog_base import Ui_QuickApiDialogBase

Also, remove FORM_CLASS from the QuickApiDialog class constructor and replace it with Ui_QuickApiDialogBase.