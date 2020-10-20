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

# Useful commands
- Generate py from ui `pyuic5 -x ui/mainView.ui -o app/src/views/mainView.py`
