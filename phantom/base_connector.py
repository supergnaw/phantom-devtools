from typing import Any

from action_result import ActionResult


class BaseConnector:
    def __init__(self) -> None:
        return

    def _apply_credential_management(self, config) -> None:
        return

    def _apply_environment_variables(self, config) -> None:
        return

    def _cleanse_param(self, parameters: dict[str, dict[str, Any]]) -> None:
        return

    def _cleanse_parameters(self, parameters) -> None:
        return

    def _count_failures(self, container) -> None:
        return

    def _create_state_file(self, path) -> None:
        return

    def _decrypt_dict_key(self, dict_name: str, dictionary: dict, key_name: str, dec_key: str = None) -> None:
        return

    def _get_phantom_base_url(self) -> str:
        return ""

    def _get_phantom_home(self) -> str:
        return ""

    def _handle_action(self, in_json, handle) -> bool:
        return True

    def _handle_cancel(self, signum, frame) -> None:
        return

    def _handle_ingest_summary(self) -> None:
        return

    def _init_ingestion_dicts(self) -> None:
        return

    def _is_action_ingestion(self) -> bool:
        return True

    def _is_app_json(self, json_file_path, connector_py) -> bool:
        return True

    def _load_app_json(self) -> dict:
        return {}

    def _load_credential_manager(self, name) -> None:
        return

    def _load_input_json(self) -> None:
        return

    def _parse_action_info(self) -> None:
        return

    def _post_container(self, container) -> None:
        return

    def add_action_result(self, action_result: ActionResult) -> ActionResult:
        """
        Add an ActionResult object to the connector run result. Returns the object added.

        :param action_result: The ActionResult object to add to the connector run.
        :return: ActionResult
        """
        return action_result

    # todo: figure out the return type of this function
    def append_to_message(self, message: str) -> None:
        """
        Appends a string to the current result message.

        :param message: The string to append to the existing message.
        :return: Unknown
        """
        return

    def debug_print(self, tag: str, dump_object: Any = "") -> None:
        """
        Dumps a pretty printed version of the 'dump_object' in the <syslog>/phantom/spawn.log file, where <syslog>
        typically is /var/log/.

        :param tag: The string that is prefixed before the dump_object is dumped.
        :param dump_object: The dump_object to dump. If the object is a list, dictionary and so on it is automatically
            pretty printed.
        :return:
        """
        return

    def error_print(self, tag: str, dump_object: Any = "") -> None:
        """
        Dumps an ERROR as a pretty printed version of the 'dump_object' in the <syslog>/phantom/spawn.log file, where
        <syslog> typically is /var/log/. Do not use this API to dump an error that is handled by the App. By default,
        the log level of the platform is set to ERROR.

        :param tag: The string that is prefixed before the dump_object is dumped.
        :param dump_object: The dump_object to dump. If the object is a list, dictionary and so on it is automatically
            pretty printed.
        :return:
        """
        return

    def finalize(self) -> None:
        """
        Optional function that can be implemented by the AppConnector. Called by the BaseConnector after all the
        elements in the parameter list are processed.

        :return:
        """
        return

    def get_action_identifier(self) -> str:
        """
        Returns the action identifier that the AppConnector is supposed to run.

        :return: action_identifier
        """
        return ""

    def get_action_name(self) -> str:
        return ""

    def get_action_results(self) -> [ActionResult]:
        """
        Returns the list of ActionResult objects added to the connector run.

        :return: [ActionResult]
        """
        return []

    def get_app_config(self) -> dict:
        """
        Returns the app configuration dictionary.

        :return: config
        """
        return {}

    def get_app_id(self) -> str:
        """
        Returns the appid of the app that was specified in the app JSON.

        :return: appid
        """
        return "00000000-0000-0000-0000-000000000000"

    def get_app_json(self) -> dict:
        """
        Returns the complete app JSON as a dictionary.

        :return: app_json
        """
        return {}

    def get_app_name(self) -> str:
        return ""

    # todo: figure out the return type of this function
    def get_app_run_id(self) -> None:
        """
        Returns the current app run id.

        :return: Unknown
        """
        return

    def get_asset_id(self) -> str:
        """
        Returns the current asset ID passed in the connector run action JSON.

        :return: asset_id
        """
        return ""

    # todo: figure out the return type of this function
    def get_ca_bundle(self) -> None:
        """
        Returns the current CA bundle file.

        :return: Unknown
        """
        return

    def get_config(self) -> dict:
        """
        Returns the current connector run configuration dictionary.

        :return: config
        """
        return {}

    def get_connector_id(self) -> str:
        """
        Returns the appid of the app that was specified in the app JSON.

        :return: appid
        """
        return ""

    def get_container_id(self) -> int:
        """
        Returns the current container ID passed in the connector run action JSON.

        :return: id
        """
        return 0

    # todo: figure out the return type of this function
    def get_container_info(self, container_id: int = None) -> None:
        """
        Returns info about the container. If container_id is not passed, returns info about the current container.

        :param container_id: ID of the container to get info of
        :return: Unknown
        """
        return

    def get_current_param(self) -> dict:
        """
        Returns the current parameter dictionary that the app is working on.

        :return: param
        """
        return {}

    # todo: figure out the return type of this function
    def get_current_param_context(self) -> None:
        return

    # todo: figure out the return type of this function
    def get_phantom_base_url(self) -> str:
        return ""

    # todo: figure out the return type of this function
    def get_phantom_home(self) -> str:
        return ""

    # todo: figure out the return type of this function
    def get_product_installation_id(self) -> None:
        """
        Returns the unique ID of the Splunk SOAR (On-premises) product installation.

        :return: Unknown
        """
        return

    # todo: figure out the return type of this function
    def get_product_name(self) -> None:
        return

    # todo: figure out the return type of this function
    def get_product_vendor(self) -> None:
        return

    # todo: figure out the return type of this function
    def get_product_version(self) -> None:
        """
        Returns the version of Splunk SOAR (On-premises).

        :return: Unknown
        """
        return

    # todo: figure out the return type of this function
    def get_product_version_regex(self) -> None:
        return

    def get_state(self) -> dict:
        """
        Gets the current state dictionary of the asset. Will return None if load_state() has not been previously called.

        :return: state
        """
        return {}

    def get_state_dir(self) -> str:
        """
        Gets the full current state file path.

        :return: path
        """
        return ""

    def get_state_file_path(self) -> str:
        """
        An app might require the state directory to create files to access during action executions. It can use the
        state directory returned by this API to store such files.

        :return: path
        """
        return ""

    def get_status(self) -> bool:
        """
        Gets the current status of the connector run. Returns either phantom.APP_SUCCESS or phantom.APP_ERROR.

        :return: status
        """
        return True

    def get_status_message(self) -> str:
        """
        Gets the current status message of the connector run.

        :return: message
        """
        return ""

    def handle_action(self, param: dict) -> bool:
        """
        Every AppConnector is required to implement this function. It is called for every parameter dictionary in the
        parameter list.

        :param param: The current parameter dictionary that needs to be acted on.
        :return: status
        """
        return True

    # todo: figure out the return type of this function
    def handle_cancel(self) -> None:
        """
        Optional function that can be implemented by the AppConnector. It is called if the action is cancelled.

        :return: Unknown
        """
        return

    # todo: figure out the return type of this function
    def handle_exception(self, exception: Exception) -> None:
        """
        Optional function that can be implemented by the AppConnector. Called if the BaseConnector::_handle_action
        function code throws an exception that is not handled.

        :param exception: The Python exception object.
        :return: Unknown
        """
        pass

    def initialize(self) -> None:
        """
        Optional function that can be implemented by the AppConnector. It is called once before starting the parameter
        list iteration, for example, before the first call to AppConnector::handle_action().

        :return:
        """
        return

    def is_action_cancelled(self) -> bool:
        """
        Returns 'True' if the connector run was cancelled. Otherwise, it returns as 'False'.

        :return: is_cancelled
        """
        return False

    def is_fail(self) -> bool:
        """
        Returns 'True' if the status of the connector run result is failure. Otherwise, it returns as 'False'.

        :return: is_fail
        """
        return False

    def is_poll_now(self) -> bool:
        """
        The on_poll action is called during Poll Now and scheduled polling. Returns 'True' if the current on_poll is run
        through the Poll Now button. Otherwise, it returns as 'False'.

        :return: is_poll_now
        """
        return True

    def is_success(self) -> bool:
        """
        Returns 'True' if the status of the Connector Run result is success. Otherwise, it returns as 'False'.

        :return: is_success
        """
        return True

    def load_state(self) -> dict | None:
        """
        Loads the current state file into the state dictionary. If a state file does not exist, it creates one with the
        app_version field. This returns the state dictionary. If an error occurs, it returns None.

        :return: state
        """
        return {}

    # todo: figure out the return type of this function
    def lock(self, param, action_result) -> None:
        return

    def remove_action_result(self, action_result: ActionResult) -> ActionResult:
        """
        Removes an ActionResult object from the connector run result. Returns the removed object.

        :param action_result: The ActionResult object that is to be removed from the connector run.
        :return: ActionResult
        """
        return action_result

    def save_artifact(self, artifact) -> tuple[bool, str, int]:
        """
        Save an artifact to Splunk SOAR (On-premises).

        :param artifact: Dictionary containing information about an artifact.
        :return: [status, message, id]
        """
        True, "success", 0

    # todo: figure out the return type of this function
    def save_artifact_ingest(self, label, data, id, name, type, severity, container_id, start_time,
                             kill_chain=None) -> None:
        return

    def save_artifacts(self, artifacts: list[dict]) -> tuple[bool, str, list[int]]:
        """
        Save a list of artifacts to Splunk SOAR (On-premises).

        :param artifacts: A list of dictionaries that each contain artifact data. Don't set the run_automation key for
            any artifacts, because the API will automatically set this value to 'False' for all but the last artifact in
            the list to start any active playbooks after the last artifact is ingested.
        :return: [status, message, [id_list]
        """
        return True, "success", [0]

    def save_container(self, container, fail_on_duplicate: bool = False) -> tuple[bool, str, int]:
        """
        Save a container and artifacts to Splunk SOAR (On-premises).

        :param container: Dictionary containing info about a container. To ingest a container and artifacts in a single
            call, add a key called artifacts to the container dictionary. This key contains a list of dictionaries, each
            item in the list representing a single artifact. Don't set the run_automation key for the container or
            artifacts. The API will automatically set this value to 'False' for all but the last artifact in the list to
            start any active playbooks after the last artifact is ingested.
        :param fail_on_duplicate: Affects behavior when attempting to save a container that is an exact duplicate of an
            existing container.
                - When True, returns phantom.APP_ERROR
                - When False or not provided, returns phantom.APP_SUCCESS
        :return: [status, message, id]
        """
        return True, "success", 0

    # todo: figure out the return type of this function
    def save_container_ingest(self, id, container, name, type, start_time, severity, sensitivity='green',
                              kill_chain=None) -> None:
        return

    def save_containers(self, containers, fail_on_duplicate: bool = False) -> tuple[bool, str, list[dict]]:
        """
        Save a list of containers to the phantom platform.

        :param containers: A list of dictionaries that each contain information about a container. Each dictionary
            follows the same rules as the input to save_container.
        :param fail_on_duplicate: Affects behavior when attempting to save a container that is an exact duplicate of an
            existing container and no other containers in the group were successfully saved.
                - When True, returns phantom.APP_ERROR
                - When False or not provided, returns phantom.APP_SUCCESS
        :return: [status, message, [{"success": bool, "message": str, "id": int},...]
        """
        return True, "success", [{"success": True, "message": "success", "id": 0}]

    # todo: figure out the return type of this function
    def save_progress(self, progress_str_const: str, *unnamed_format_args, **named_format_args) -> None:
        """
        This function sends a progress message to the Splunk SOAR core, which is saved in persistent storage.

        :param progress_str_const: The progress message to send to the Spunk Phantom core. Typically, this is a short
            description of the current task.
        :param unnamed_format_args: The various parameters that need to be formatted into the progress_str_config
            string.
        :param named_format_args: The various parameters that need to be formatted into the progress_str_config string.
        :return: Unknown
        """
        return

    # todo: figure out the return type of this function
    def save_state(self, state: dict) -> None:
        """
        Writes a given dictionary to a state file that can be loaded during future app runs. This is especially crucial
        with ingestion apps. The saved state is unique per asset. An app_version field will be added to the dictionary
        before saving.

        :param state: The dictionary to write to the state file.
        :return: Unknown
        """
        return

    # todo: figure out the return type of this function
    def send_progress(self, progress_str_const: str, *unnamed_format_args, **named_format_args) -> None:
        """
        This function sends a progress message to the Splunk SOAR core. It is written to persistent storage, but is
        overwritten by the message that comes in through the next send_progress call. Use this function to send messages
        that need not be stored over a period of time like percent completion messages while downloading a file.

        :param progress_str_const: The progress message to send to the Splunk SOAR core. Typically, this is a short
            description of the current task being carried out.
        :param unnamed_format_args: The various parameters that need to be formatted into the progress_str_config
            string.
        :param named_format_args: The various parameters that need to be formatted into the progress_str_config string.
        :return: Unknown
        """
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

    def set_status_save_progress(self, status_code: bool, status_message: str = '', exception=None,
                                 *unnamed_format_args, **named_format_args) -> bool:
        """
        Helper function that sets the status of the connector run. This needs to be phantom.APP_SUCCESS or
        phantom.APP_ERROR. This function sends a persistent progress message to the Splunk SOAR Core in a single call.
        Returns the status_code set.

        :param status_code: The status to set of the connector run. It is either phantom.APP_SUCCESS or
            phantom.APP_ERROR.
        :param status_message: The message to set. Typically, this is a short description of the error or success.
        :param exception: The Python exception object that has occurred. BaseConnector will convert this exception
            object to string format and append it to the message.
        :param unnamed_format_args: The various parameters that need to be formatted into the status_message string.
        :param named_format_args: The various parameters that need to be formatted into the status_message string.
        :return: status
        """
        return status_code

    def set_validator(self, contains, validator) -> tuple[bool, str]:
        """
        Sets the validator of a particular contains, this is set for the current connector run only. Call this from the
        initialize function.

        :param contains:
        :param validator:
        :return: [status, message]
        """
        return True, "success"

    # todo: figure out the return type of this function
    def telemetry_print(self, tag, dump_object='') -> None:
        return

    # todo: figure out the return type of this function
    def unknown_action(self) -> None:
        return

    # todo: figure out the return type of this function
    def unlock(self) -> None:
        return

    # todo: figure out the return type of this function
    def update_summary(self, summary) -> None:
        """
        Update the connector run summary dictionary with the passed dictionary.

        :param summary: The Python dictionary that needs to be updated to the current connector run summary.
        :return: Unknown
        """
        return

    def validate_parameters(self, param: dict[str, dict[str, Any]]) -> bool:
        """
        BaseConnector uses this function to validate the current parameter dictionary based on the contains of the
        parameter. The AppConnector can override it to specify its own validations.

        :param param:
        :return: bool
        """
        return True
