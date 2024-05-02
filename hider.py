class Hider:
    def __init__(self):
        self.classes = [
            'clock leaflet-control',
            'leaflet-control-layers-toggle',
            'button--markers',
            'button--players',
            'leaflet-control-coordinates leaflet-control',
            'leaflet-control-button leaflet-control-link leaflet-control'
        ]

    def hide(self, driver):
        for class_name in self.classes:
            script = f'''var element = document.getElementsByClassName('{class_name}');
                        element[0].style.display = 'none';'''
            driver.execute_script(script)
