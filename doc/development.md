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

# Useful commands
- Generate py from ui `pyuic5 -x ui/MainView.ui -o app/src/views/MainView.py`

# Mockups
- [Adobe](https://xd.adobe.com/view/58ec34d0-bdb9-48e5-4ff2-9323147e4448-2edd/screen/4d0b6bb8-7a5e-40d9-ab21-65cd9f8995f1/)