# Development

## New action 

1. Create new view in designer and generate .py file to `app/src/views`
1. Move your .ui file from designer to ui directory
1. Create new controller/function in controller e.g `def index():`
1. Add this urgent lines to function
    ```python
    def index(self):
        file_name = "MainView" # File name from `app/src/views`
        view = self.prepareView(file_name) # build view, we can use `view` variable to modify view elements 
    
        return self.render() # show view
    ```
1. Run `python start.py` to start application 


## Add now "subpage" (like settings, video)
1. Open `ui/MainView.ui` in `designer` program
1. Find `page_main` QStackedWidget 
1. Add new `QWidget` to the list
1. Set `objectName` like `view_<name>`
1. Add new `QPushButton`
1. Set `objectName` like `nav_<name>`
1. Save changes
1. Generate `.py` from `.ui`
1. Go to controller and copy part with navigation
    ```python
    view.nav_main.clicked.connect(lambda: view.page_main.setCurrentWidget(view.view_main))
    ```
1. Past and change name to the new ones
1. Create file in `app/src/services/viewExtension` with name <controllerName><viewName>
    ```python
    main_view_settings = MainViewSettings()
    main_view_settings.configViewSettings(view)
    ```
1. Modify new view as you wish


## Add new listener

1. Create file in `app/src/listeners` directory
1. Create class inside the file with the same name
1. Add method
1. Add config method for loader
1. Run event `EventDispatcher().getDispatcher().raise_event("onKernelStart")`

Eg. class
```python
class MyListener:
    def eventList(self):
        return {
            "onKernelStart": { # event name, method will be triggered when subscriber raise it
                "action": self.myFunction, #send method as a callback
                "priority": -200 # priority, some listeners should be called earlier than another (e.g. db init should be first)
            }
        }
    def myFunction(self):
        pass
```

# Useful commands
- Generate py from ui `pyuic5 -x ui/MainView.ui -o app/src/views/MainView.py`

## Generating .py from .ui using Windows 10
1. Directory for pyuic5
- [Microsoft Store]`C:\Users\you\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_##########\LocalCache\local-packages\Python39(your-version)\Scripts`
- [Desktop Standard] `C:\Users\you\AppData\Roaming\Python\Python3(your-version)\Scripts`
- [Anaconda]   `Anaconda3\Library\bin`
1. Use CMD for \Scripts or \bin directory then
`pyuic5 -x MainView.ui -o MainView.py`
1. Put .py file into the views folder.
1. If needed import .qrc (below) 

## Importing .qrc file using Windows 10
1. Get \Scripts or \bin directory then use CMD:
- 'pyrcc5 sample.qrc -o sample.py'
1. Put .py file into the project folder.
1. import sample.py file into your MainView.

# Mockups
- [Adobe](https://xd.adobe.com/view/2e1cf53e-92ed-4b14-afd1-b0833650f5c8-7b4f/)