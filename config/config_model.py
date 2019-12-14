class ConfigOperator:

    # Overridable -- handle load config event
    @staticmethod
    def load(config_model_name):
        pass

    # Overridable -- handle save config event
    @staticmethod
    def save(config_model):
        pass

    # Overridable -- handle first load config
    @staticmethod
    def update_all_config():
        pass
