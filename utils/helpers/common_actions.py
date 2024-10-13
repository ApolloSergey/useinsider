from datetime import datetime, timedelta


class CommonActions(object):

    """
    All miscellaneous common actions
    """

    @staticmethod
    def strtobool(string):
        string = string.casefold()
        if string in ('y', 'yes', 't', 'true', 'on', '1'):
            return True
        elif string in ('n', 'no', 'f', 'false', 'off', '0'):
            return False
        else:
            raise ValueError(f"Invalid truth value: {string}")

    @staticmethod
    def get_time():
        """
        Returns the date and time
        @return: the date and time
        """
        return datetime.now()

    @staticmethod
    def get_date(date_format="%m/%d/%Y"):
        """
        Returns the date in format "%m/%d/%Y"
        @return: the date
        """
        today_date = datetime.now()
        return today_date.strftime(date_format)

    @staticmethod
    def get_new_year(date_format="%Y", time=365):
        """
        Returns the date in format "%Y"
        @return: the date
        """
        today_date = datetime.now()
        today_date.strftime(date_format)
        next_year = today_date + timedelta(days=time)
        return next_year.strftime(date_format)
