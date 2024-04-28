from typing import Any


class ActionResult:
    def __init__(self):
        pass

    def _debug_data_to_string(self, item) -> None:
        return

    def _get_exception_str(self, exception) -> None:
        return

    def add_data(self, item: dict) -> dict:
        """
        Adds a data item as a dictionary to the list. Returns the item added.

        :param item: This is a dictionary that needs to be added as a new element to the current data list.
        :return: item
        """
        return item

    # todo: figure out the return type of this function
    def add_debug_data(self, item: Any) -> None:
        """
        Adds a debug data item to the list. The item will be converted to a string object through the str(...) call
        before it is added to the list. This list is dumped in the spawn.log file if the action result fails.

        :param item:
        :return: Unknown
        """
        return

    def add_exception_details(self, exception: Exception) -> bool:
        """
        Adds details of an exception into the action result. These details are appended to the message in the resultant
        dictionary. Returns the current status code of the object.

        :param exception: The Python exception object that has occurred. ActionResult will convert this exception object
            to string format and append it to the message.
        :return: status
        """
        return True

    # todo: add param details
    def add_extra_data(self, item: dict) -> dict:
        """
        Adds an extra data item as a dictionary to the list. Extra data is different from data that is added through the
        add_data(...) API. Apps can add data as extra data if the data is huge and none of it is rendered. Typically,
        this is something that needs to be recorded and can potentially be used from a playbook, but not rendered.
        Returns the item added.

        :param item:
        :return: item
        """
        return item

    # todo: figure out the return type of this function
    def append_to_message(self, message_str: str) -> None:
        """
        Appends the text to the message.

        :param message_str: The string to append to the existing message.
        :return: Unknown
        """
        return

    # todo: figure out the return type of this function
    def dump_debug_data(self) -> None:
        return

    def get_data(self) -> list:
        """
        Gets the current data list.

        :return: data
        """
        return []

    # todo: figure out the return type of this function
    def get_data_size(self) -> None:
        """
        Gets the current data list size.

        :return: Unknown
        """
        return

    def get_debug_data(self) -> list:
        """
        Gets the current debug data list.

        :return: data
        """
        return []

    # todo: figure out the return type of this function
    def get_debug_data_size(self) -> None:
        """
        Gets the current debug data list size.

        :return: Unknown
        """
        return

    def get_dict(self) -> dict:
        """
        Creates a dictionary from the current state of the object. This is usually called from BaseConnector.

        :return: state
        """
        return {}

    def get_extra_data(self) -> list:
        """
        Gets the current extra data list.

        :return: data
        """
        return []

    # todo: figure out the return type of this function
    def get_extra_data_size(self) -> None:
        """
        Gets the current extra data list size.

        :return: Unknown
        """
        return

    def get_message(self) -> str:
        """
        Gets the current action result message.

        :return: message
        """
        return ""

    def get_param(self) -> dict:
        """
        Gets the current parameter dictionary.

        :return: param
        """
        return {}

    def get_status(self) -> bool:
        """
        Gets the current result. It returns either phantom.APP_SUCCESS or phantom.APP_ERROR.

        :return: status
        """
        return True

    def get_summary(self) -> dict:
        """
        Returns the current summary dictionary.

        :return: summary
        """
        return {}

    def is_fail(self) -> bool:
        """
        Returns 'True' if the ActionResult status is a failure.

        :return: is_fail
        """
        return False

    def is_success(self) -> bool:
        """
        Returns 'True' if the ActionResult status is success.

        :return: is_success
        """
        return True

    def set_base_connector(self, obj) -> None:
        return

    def set_data_size(self, size) -> None:
        return

    def set_debug_data_size(self, size) -> None:
        return

    def set_extra_data_size(self, size) -> None:
        return

    # todo: figure out the return type of this function
    def set_param(self, param_dict: dict) -> None:
        """
        Sets the parameter dictionary with the passed param_dict. This overwrites the current parameter dictionary.

        :param param_dict: The Python dictionary that overwrites the current parameter.
        :return: Unknown
        """
        return

    def set_param_context(self, param_context) -> None:
        return

    def set_result_index(self, result_index) -> None:
        return

    def set_status(self, status_code: bool, status_message: str = '', exception: Exception = None, *unnamed_format_args,
                   **named_format_args) -> bool:
        """
        Sets the status of the connector run result, phantom.APP_SUCCESS or phantom.APP_ERROR. Optionally, you can set
        the message. If an exception object is specified, it is recorded in the connector run result. It will replace
        any status and message previously saved in the object. Returns the status_code set.

        :param status_code: The status to set of the connector run. It is either phantom.APP_SUCCESS or
            phantom.APP_ERROR.
        :param status_message: The message to set. Typically, this is a short description of the error or success.
        :param exception: The Python exception object that has occurred. BaseConnector will convert this exception
            object to string format and append to the message.
        :param unnamed_format_args: The various parameters that need to be formatted into the status_message string.
        :param named_format_args: The various parameters that need to be formatted into the status_message string.
        :return: status
        """
        return status_code

    def set_summary(self, summary: dict) -> dict:
        """
        Replaces the summary with the passed summary dictionary. Returns the summary set.

        :param summary: The Python dictionary that overwrites the current summary.
        :return: dict
        """
        return summary

    # todo: figure out the return type of this function
    def update_data(self, item: dict) -> None:
        """
        Extends the data list with elements in the item list.

        :param item:
        :return: Unknown
        """
        return

    # todo: figure out the return type of this function
    def update_extra_data(self, item: dict) -> None:
        """
        Extends the extra data list with elements in the item list.

        :param item:
        :return: Unknown
        """
        return

    # todo: figure out the return type of this function
    def update_param(self, param_dict: dict) -> None:
        """
        Updates the parameter dictionary with 'param_dict'

        :param param_dict: The Python dictionary that is to be updated into the current parameter.
        :return: Unknown
        """
        return

    def update_summary(self, summary: dict) -> dict:
        """
        Updates the summary with the passed summary dictionary. Returns the updated summary.

        :param summary: The Python dictionary that updates the current summary.
        :return: summary
        """
        return summary
