import configparser

config = configparser.RawConfigParser()
config.read('D:\\Peettam\\MySiteBook\\Configuration\\config.ini')


class Readconfig:

    @staticmethod
    def get_url():
        return config.get("msb Login", "msb_URL")

    @staticmethod
    def get_phone_number():
        return config.get("msb Login", "msb_phone_number")

    @staticmethod
    def get_password():
        return config.get("msb Login", "msb_password")

    @staticmethod
    def get_homepage_title():
        return config.get("msb HomePage", "homepage_title")

    @staticmethod
    def get_sample_project_name():
        return config.get("msb Choices", "sample_project_name")

    @staticmethod
    def get_check_out_title():
        return config.get('msb Choices', 'check_out_title')
