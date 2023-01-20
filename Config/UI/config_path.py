import json

with open('Config/UI/config_ui.json') as config_file:
    config_data = json.load(config_file)

class page_path_configuration :
    
    def get_url_page(environment, page):
        url = config_data[environment][page]
        return url