# "abc": "(<class 'module'>) <module 'abc' from '/home/phantomuser/phantom/usr/python39/lib/python3.9/abc.py'>",
# "compat": "(<class 'module'>) <module 'phantom_common.compat' from '/home/phantomuser/phantom/pycommon3/phantom_common/compat.pyc'>",
# "copy": "(<class 'module'>) <module 'copy' from '/home/phantomuser/phantom/usr/python39/lib/python3.9/copy.py'>",
# "glob": "(<class 'module'>) <module 'glob' from '/home/phantomuser/phantom/usr/python39/lib/python3.9/glob.py'>",
# "inspect": "(<class 'module'>) <module 'inspect' from '/home/phantomuser/phantom/usr/python39/lib/python3.9/inspect.py'>",
# "install_info": "(<class 'module'>) <module 'phantom_common.install_info' from '/home/phantomuser/phantom/pycommon3/phantom_common/install_info.pyc'>",
# "json": "(<class 'module'>) <module 'simplejson' from '/home/phantomuser/phantom/usr/python39/lib/python3.9/site-packages/simplejson/__init__.py'>",
# "logging": "(<class 'module'>) <module 'logging' from '/home/phantomuser/phantom/usr/python39/lib/python3.9/logging/__init__.py'>",
# "os": "(<class 'module'>) <module 'os' from '/home/phantomuser/phantom/usr/python39/lib/python3.9/os.py'>",
# "ph_consts": "(<class 'module'>) <module 'phantom.consts' from '/home/phantomuser/phantom/lib3/phantom/consts.pyc'>",
# "ph_engine": "(<class 'module'>) <module 'phantom.ph_engine' from '/home/phantomuser/phantom/lib3/phantom/ph_engine.pyc'>",
# "ph_jsons": "(<class 'module'>) <module 'phantom.json_keys' from '/home/phantomuser/phantom/lib3/phantom/json_keys.pyc'>",
# "ph_progress": "(<class 'module'>) <module 'phantom.progress' from '/home/phantomuser/phantom/lib3/phantom/progress.pyc'>",
# "ph_redact": "(<class 'module'>) <module 'phantom.redact' from '/home/phantomuser/phantom/lib3/phantom/redact.pyc'>",
# "ph_status": "(<class 'module'>) <module 'phantom.status' from '/home/phantomuser/phantom/lib3/phantom/status.pyc'>",
# "ph_utils": "(<class 'module'>) <module 'phantom.utils' from '/home/phantomuser/phantom/lib3/phantom/utils.pyc'>",
# "phproc": "(<class 'module'>) <module 'phantom_common.phproc' from '/home/phantomuser/phantom/pycommon3/phantom_common/phproc.pyc'>",
# "random": "(<class 'module'>) <module 'random' from '/home/phantomuser/phantom/usr/python39/lib/python3.9/random.py'>",
# "re": "(<class 'module'>) <module 're' from '/home/phantomuser/phantom/usr/python39/lib/python3.9/re.py'>",
# "requests": "(<class 'module'>) <module 'requests' from '/home/phantomuser/phantom/usr/python39/lib/python3.9/site-packages/requests/__init__.py'>",
# "requests_exceptions": "(<class 'module'>) <module 'requests.exceptions' from '/home/phantomuser/phantom/usr/python39/lib/python3.9/site-packages/requests/exceptions.py'>",
# "shutil": "(<class 'module'>) <module 'shutil' from '/home/phantomuser/phantom/usr/python39/lib/python3.9/shutil.py'>",
# "signal": "(<class 'module'>) <module 'signal' from '/home/phantomuser/phantom/usr/python39/lib/python3.9/signal.py'>",
# "sjson": "(<class 'module'>) <module 'simplejson' from '/home/phantomuser/phantom/usr/python39/lib/python3.9/site-packages/simplejson/__init__.py'>",
# "string": "(<class 'module'>) <module 'string' from '/home/phantomuser/phantom/usr/python39/lib/python3.9/string.py'>",
# "subprocess": "(<class 'module'>) <module 'subprocess' from '/home/phantomuser/phantom/usr/python39/lib/python3.9/subprocess.py'>",
# "tempfile": "(<class 'module'>) <module 'tempfile' from '/home/phantomuser/phantom/usr/python39/lib/python3.9/tempfile.py'>",
# "time": "(<class 'module'>) <module 'time' (built-in)>",
# "traceback": "(<class 'module'>) <module 'traceback' from '/home/phantomuser/phantom/usr/python39/lib/python3.9/traceback.py'>",
# "urlparse": "(<class 'module'>) <module 'urllib.parse' from '/home/phantomuser/phantom/usr/python39/lib/python3.9/urllib/parse.py'>",
# "uuid": "(<class 'module'>) <module 'uuid' from '/home/phantomuser/phantom/usr/python39/lib/python3.9/uuid.py'>",

# "config": "(<class 'phantom.utils.PylibConfig'>) <phantom.utils.PylibConfig object at 0x7f111f6e6130>",
# "connector_obj": "(<class 'NoneType'>) None",
# "logger": "(<class 'logging.Logger'>) <Logger phantom.utils (WARNING)>",
# "ph_ingest": "(<class 'NoneType'>) None",
# "ph_ipc": "(<class 'NoneType'>) None",
# "platform_encryption_backend": "(<class 'phantom_common.encryption.on_prem.OnPremEncryptionStore'>) <phantom_common.encryption.on_prem.OnPremEncryptionStore object at 0x7f111f0da7f0>",
# "print_function": "(<class '__future__._Feature'>) _Feature((2, 6, 0, 'alpha', 2), (3, 0, 0, 'alpha', 0), 1048576)",
# "unicode_literals": "(<class '__future__._Feature'>) _Feature((2, 6, 0, 'alpha', 2), (3, 0, 0, 'alpha', 0), 2097152)",

import typing
import collections


def ABC():
    return


ACTION_ID_INGEST_ON_POLL: str = "on_poll"
ACTION_ID_INGEST_ON_RECEIVE: str = "on_receive"
ACTION_ID_TEST_ASSET_CONNECTIVITY: str = "test_asset_connectivity"
ACTION_RESULT_HEADERS: frozenset = frozenset(
    {'message', 'action', 'app', 'summary', 'app_run_id', 'app_id', 'asset', 'result_data', 'status', 'action_run_id',
     'asset_id', 'name'})
ACTION_RESULT_KEYS: frozenset = frozenset(
    {'action_results', 'message', 'action', 'app', 'oid', 'summary', 'app_run_id', 'app_id', 'asset', 'result_data',
     'status', 'action_run_id', 'asset_id', 'name'})
ACTION_RESULT_KEYS_NO_FLATTENING: frozenset = frozenset(
    {'message', 'action', 'app', 'summary', 'app_run_id', 'app_id', 'asset', 'result_data', 'status', 'action_run_id',
     'asset_id', 'name'})
ACTION_RESULT_KEYS_YES_FLATTENING: frozenset = frozenset({'action_results', 'oid'})
ACTION_RESULT_KEY_ACTION: str = "action"
ACTION_RESULT_KEY_ACTION_RESULTS: str = "action_results"
ACTION_RESULT_KEY_ACTION_RUN_ID: str = "action_run_id"
ACTION_RESULT_KEY_APP: str = "app"
ACTION_RESULT_KEY_APP_ID: str = "app_id"
ACTION_RESULT_KEY_APP_RUN_ID: str = "app_run_id"
ACTION_RESULT_KEY_ASSET: str = "asset"
ACTION_RESULT_KEY_ASSET_ID: str = "asset_id"
ACTION_RESULT_KEY_MESSAGE: str = "message"
ACTION_RESULT_KEY_NAME: str = "name"
ACTION_RESULT_KEY_OID: str = "oid"
ACTION_RESULT_KEY_RESULT_DATA: str = "result_data"
ACTION_RESULT_KEY_STATUS: str = "status"
ACTION_RESULT_KEY_SUMMARY: str = "summary"


def APILocation(value, names=None, *, module=None, qualname=None, type=None, start=1):
    return


APPS_STATE_PATH: str = "/home/phantomuser/phantom/local_data/app_states"
APP_DEFAULT_ARTIFACT_LABEL: str = "artifact"
APP_DEFAULT_ARTIFACT_TYPE: str = "network"
APP_DEFAULT_CONTAINER_LABEL: str = "incident"
APP_ERROR: bool = False
APP_ERROR_STR: str = "failed"
APP_ERR_ACTION_APP_CONFIG_DICT_NOT_FOUND: str = "No App config dictionary present in Action JSON"
APP_ERR_ACTION_CONFIG_DICT_NOT_FOUND: str = "No Config dictionary present in Action JSON"
APP_ERR_ACTION_DICT_MULTI_FOUND: str = "Multiple action infos for '{action_id}' in App JSON should contain only one"
APP_ERR_ACTION_DICT_NOT_FOUND: str = "Unknown action. Unable to find action info for '{action_id}' in App JSON"
APP_ERR_ALL_CMDS: str = "100% of action executions failed"
APP_ERR_APP_JSON_LOAD: str = "Failed to load the app JSON"
APP_ERR_ASSET_ID_LOCK_INVALID: str = "Asset configuration (like the 'asset id') not found in the configuration sent to the app"
APP_ERR_CMD_EXEC: str = "Action execution failed"
APP_ERR_CONNECTOR_RUN_JSON_LOAD: str = "Failed to load the connector run JSON. Missing or invalid '{key}'"
APP_ERR_CONN_RUN: str = "Connector run failed"
APP_ERR_DECRYPT_KEY: str = "Unable to decrypt {dict_name} key '{key}'"
APP_ERR_DECRYPT_KEY_NO_KEY: str = "Decryption key not passed. Unable to decrypt {dict_name} key '{key}'"
APP_ERR_EXCEPTION_OCCURED: str = "Exception Occurred"
APP_ERR_FILE_ADD_TO_VAULT: str = "Failed to add file to vault"
APP_ERR_INGEST_MODULE_NOT_FOUND: str = "Splunk SOAR ingest module not found"
APP_ERR_INITIALIZE_DID_NOT_RETURN_A_VALUE: str = "{classname}::initialize() did not return a 'mandotary' status code"
APP_ERR_JSON_ACTION_PARAM_DICT_NOT_FOUND: str = "Parameter dict not found for action '{action_id}' in App JSON"
APP_ERR_JSON_CONFIG_DICT_NOT_FOUND: str = "No configuration dictionary present in the app JSON"
APP_ERR_LOCK_ACQUIRE: str = "Failed to acquire lock"
APP_ERR_LOCK_ACQUIRE_NAMED: str = "Failed to acquire lock named '{lock_name}' for Action: '{action_name}', App: '{app_name}'"
APP_ERR_LOCK_DATA_PATH_INVALID: str = "Data path: {0} value cannot be used as a lock name"
APP_ERR_LOCK_KEY_NOT_FOUND: str = "Key '{key_name}' not found in the {dict_type} JSON sent to the app"
APP_ERR_LOCK_MODULE_UNAVAILABLE: str = "Backend module required to carry out Lock/UnLock operations is unavailable"
APP_ERR_LOCK_OBJECT_ALREADY_USED: str = "Object already used once, multiple uses of object is not allowed"
APP_ERR_LOCK_OBJECT_NAME_NONE: str = "Lock name not set. Please lock first"
APP_ERR_LOCK_OBJECT_UNLOCKED: str = "Object not in locked state. Unlock operation not possible"
APP_ERR_NYI: str = "Not yet implemented"
APP_ERR_UNK_CMD: str = "Unknown Action: {action_identifier}"
APP_INGEST_ACTIONS: list = ['on_poll', 'poll_now']
APP_INITIALIZE_RETURNED_ERROR: str = "{classname}::initialize() returned error"
APP_JSON_ACTIONS: str = "actions"
APP_JSON_ACTION_CANCELLED: str = "action_cancelled"
APP_JSON_ACTION_IDENTIFIER: str = "identifier"
APP_JSON_ACTION_NAME: str = "action"
APP_JSON_ALLOW_LIST: str = "allow_list"
APP_JSON_APP_CONFIG: str = "app_config"
APP_JSON_APP_ID: str = "appid"
APP_JSON_APP_NAME: str = "name"
APP_JSON_APP_RUN_ID: str = "app_run_id"
APP_JSON_ARRAY_ITEMS: str = "items"
APP_JSON_ARTIFACT_COUNT: str = "artifact_count"
APP_JSON_ART_DUP: str = "artifacts_duplicate"
APP_JSON_ART_FAIL: str = "artifacts_failed"
APP_JSON_ART_SUCC: str = "artifacts_successful"
APP_JSON_ASSET_ID: str = "asset_id"
APP_JSON_CONFIG: str = "config"
APP_JSON_CONFIGURATION: str = "configuration"
APP_JSON_CONFIGURATION_REQUIRED: str = "required"
APP_JSON_CONFIG_PARAMETERS: str = "parameters"
APP_JSON_CONNECTOR: str = "main_module"
APP_JSON_CONTAINER_COUNT: str = "container_count"
APP_JSON_CONTAINER_ID: str = "container_id"
APP_JSON_CONTAINS: str = "contains"
APP_JSON_CONT_DUP: str = "containers_duplicate"
APP_JSON_CONT_FAIL: str = "containers_failed"
APP_JSON_CONT_SUCC: str = "containers_successful"
APP_JSON_DATA: str = "data"
APP_JSON_DATA_TYPE: str = "data_type"
APP_JSON_DEBUG_LEVEL: str = "debug_level"
APP_JSON_DEC_KEY: str = "dec_key"
APP_JSON_DESCRIPTION: str = "description"
APP_JSON_DEVICE: str = "device"
APP_JSON_DOMAIN: str = "domain"
APP_JSON_DOWNLOAD: str = "download"
APP_JSON_ENDPOINT: str = "endpoint"
APP_JSON_END_TIME: str = "end_time"
APP_JSON_ENV_VARS: str = "environment_variables"
APP_JSON_ERROR_DETAILS: str = "error_details"
APP_JSON_EXCEPTION_OCCURED: str = "exception_occured"
APP_JSON_EXTRA_DATA: str = "extra_data"
APP_JSON_HASH: str = "hash"
APP_JSON_HOST: str = "host"
APP_JSON_HOSTNAME: str = "hostname"
APP_JSON_INFO: str = "info"
APP_JSON_INGEST_CONNECTOR_ID: str = "ingest_app_id"
APP_JSON_IP: str = "ip"
APP_JSON_IPC_ACTION_NAME: str = "action"
APP_JSON_IPC_ACTION_RUN_ID: str = "action_run_id"
APP_JSON_IPC_APP_RUN_ID: str = "connector_run_id"
APP_JSON_IPC_RESULT: str = "result"
APP_JSON_IPC_RESULT_DATA: str = "result_data"
APP_JSON_IP_HOSTNAME: str = "ip_hostname"
APP_JSON_IP_MACADDRESS: str = "ip_macaddress"
APP_JSON_LABEL: str = "label"
APP_JSON_LOCK: str = "lock"
APP_JSON_LOCK_CONCURRENCY: str = "concurrency"
APP_JSON_LOCK_DATA_PATH: str = "data_path"
APP_JSON_LOCK_DEFAULT_NAME: str = "default_name"
APP_JSON_LOCK_ENABLED: str = "enabled"
APP_JSON_LOCK_NAME: str = "name"
APP_JSON_LOCK_TIMEOUT: str = "timeout"
APP_JSON_MACADDRESS: str = "macaddress"
APP_JSON_MACHINE_IP_NAME: str = "machine_ip_name"
APP_JSON_MACHINE_NAME: str = "machine_name"
APP_JSON_MESSAGE: str = "message"
APP_JSON_NAME: str = "name"
APP_JSON_PARAMETERS: str = "parameters"
APP_JSON_PARAM_CONTEXT: str = "context"
APP_JSON_PASSWORD: str = "password"
APP_JSON_PATH: str = "path"
APP_JSON_PID: str = "pid"
APP_JSON_PORT: str = "port"
APP_JSON_PROCESS: str = "process"
APP_JSON_PRODUCT_NAME: str = "product_name"
APP_JSON_PRODUCT_VENDOR: str = "product_vendor"
APP_JSON_PRODUCT_VERSION_REGEX: str = "product_version_regex"
APP_JSON_RESULT_DATA: str = "result_data"
APP_JSON_RESULT_SUMMARY: str = "result_summary"
APP_JSON_RES_PARAMS: str = "parameter"
APP_JSON_RUN_AUTOMATION: str = "run_automation"
APP_JSON_SERVER: str = "server"
APP_JSON_SIZE: str = "size"
APP_JSON_START_TIME: str = "start_time"
APP_JSON_STATE: str = "state"
APP_JSON_STATUS: str = "status"
APP_JSON_SUMMARY: str = "summary"
APP_JSON_SYSTEM: str = "system"
APP_JSON_TIMEZONE: str = "timezone"
APP_JSON_TOTAL_OBJECTS_SUCCESS: str = "total_objects_successful"
APP_JSON_TOTAL_OBJECTS_TO_ACT_ON: str = "total_objects"
APP_JSON_TYPE: str = "type"
APP_JSON_URL: str = "url"
APP_JSON_USERNAME: str = "username"
APP_JSON_VAULT_ID: str = "vault_id"
APP_JSON_VERIFY: str = "verify_server_cert"
APP_NO_CMDS_FOUND: str = "No action executions found"
APP_PROG_ADDING_TO_VAULT: str = "Adding file to vault"
APP_PROG_CONNECTED_TO_SERVER: str = "Connected to server: '{server}'"
APP_PROG_CONNECTING_TO_ELLIPSES: str = "Connecting to {}..."
APP_PROG_CONNECTING_WITH_URL: str = "URL = '{}'"
APP_PROG_DOWNLOADING_FILE_FROM_TO: str = "Saving file from {src} to {dest}"
APP_PROG_FILE_SIZE: str = "File size = {value} {type}"
APP_PROG_FINISHED_DOWNLOADING_STATUS: str = "Finished downloading {value} {type}"
APP_PROG_LOADED_CONFIG: str = "Loaded action execution configuration"
APP_SUCCESS: bool = True
APP_SUCCESS_STR: str = "success"
APP_SUCC_ALL_CMDS: str = "100% of action executions succeeded"
APP_SUCC_CMD_EXEC: str = "Action execution succeeded"
APP_SUCC_CONN_RUN: str = "Connector run successful"
APP_SUCC_FILE_ADD_TO_VAULT: str = "File added to vault"
APP_SUCC_FILE_DOWNLOAD: str = "File download successful"
APP_SUCC_PROGRESS: int = 1
APP_SUCC_PROGRESS_STR: str = "running"
APP_SUCC_SOME_CMDS: str = "Errors: {total_failures}"
APP_SUCC_STOP: int = 2
APP_SUCC_STOP_STR: str = "stop"
ARTIFACT_BATCH_SIZE: int = 100
ASSET_HTTPS_PROXY: str = "ASSET_HTTPS_PROXY"
ASSET_HTTP_PROXY: str = "ASSET_HTTP_PROXY"


def ActionCancelException(reason_msg=None) -> None:
    return


def ActionResult(param=None) -> None:
    return


def Any(*args, **kwds):
    return


def BaseConnector() -> None:
    return


CEF_JSON: dict = {'act': {'contains': []}, 'app': {'contains': []}, 'applicationProtocol': {'contains': []},
                  'baseEventCount': {'contains': []}, 'bytesIn': {'contains': []}, 'bytesOut': {'contains': []},
                  'cat': {'contains': []}, 'cn1': {'contains': []}, 'cn1Label': {'contains': []},
                  'cn2': {'contains': []}, 'cn2Label': {'contains': []}, 'cn3': {'contains': []},
                  'cn3Label': {'contains': []}, 'cnt': {'contains': []}, 'cs1': {'contains': []},
                  'cs1Label': {'contains': []}, 'cs2': {'contains': []}, 'cs2Label': {'contains': []},
                  'cs3': {'contains': []}, 'cs3Label': {'contains': []}, 'cs4': {'contains': []},
                  'cs4Label': {'contains': []}, 'cs5': {'contains': []}, 'cs5Label': {'contains': []},
                  'cs6': {'contains': []}, 'cs6Label': {'contains': []}, 'destinationAddress': {'contains': ['ip']},
                  'destinationDnsDomain': {'contains': ['domain']}, 'destinationHostName': {'contains': ['host name']},
                  'destinationMacAddress': {'contains': ['mac address']}, 'destinationNtDomain': {'contains': []},
                  'destinationPort': {'contains': ['port']}, 'destinationProcessName': {'contains': ['process name']},
                  'destinationServiceName': {'contains': ['process name']},
                  'destinationTranslatedAddress': {'contains': ['ip']},
                  'destinationTranslatedPort': {'contains': ['port']}, 'destinationUserId': {'contains': []},
                  'destinationUserName': {'contains': ['user name']}, 'destinationUserPrivileges': {'contains': []},
                  'deviceAction': {'contains': []}, 'deviceAddress': {'contains': ['ip']},
                  'deviceCustomDate1': {'contains': []}, 'deviceCustomDate1Label': {'contains': []},
                  'deviceCustomDate2': {'contains': []}, 'deviceCustomDate2Label': {'contains': []},
                  'deviceCustomNumber1': {'contains': []}, 'deviceCustomNumber1Label': {'contains': []},
                  'deviceCustomNumber2': {'contains': []}, 'deviceCustomNumber2Label': {'contains': []},
                  'deviceCustomNumber3': {'contains': []}, 'deviceCustomNumber3Label': {'contains': []},
                  'deviceCustomString1': {'contains': []}, 'deviceCustomString1Label': {'contains': []},
                  'deviceCustomString2': {'contains': []}, 'deviceCustomString2Label': {'contains': []},
                  'deviceCustomString3': {'contains': []}, 'deviceCustomString3Label': {'contains': []},
                  'deviceCustomString4': {'contains': []}, 'deviceCustomString4Label': {'contains': []},
                  'deviceCustomString5': {'contains': []}, 'deviceCustomString5Label': {'contains': []},
                  'deviceCustomString6': {'contains': []}, 'deviceCustomString6Label': {'contains': []},
                  'deviceDirection': {'contains': []}, 'deviceDnsDomain': {'contains': ['domain']},
                  'deviceEventCategory': {'contains': []}, 'deviceExternalId': {'contains': []},
                  'deviceFacility': {'contains': []}, 'deviceHostname': {'contains': ['host name']},
                  'deviceInboundInterface': {'contains': []}, 'deviceMacAddress': {'contains': ['mac address']},
                  'deviceOutboundInterface': {'contains': []}, 'deviceProcessName': {'contains': ['process name']},
                  'deviceTranslatedAddress': {'contains': ['ip']}, 'dhost': {'contains': ['host name']},
                  'dmac': {'contains': ['mac address']}, 'dntdom': {'contains': ['domain']}, 'dpriv': {'contains': []},
                  'dproc': {'contains': ['process name']}, 'dpt': {'contains': ['port']}, 'dst': {'contains': ['ip']},
                  'duid': {'contains': []}, 'duser': {'contains': ['user name']}, 'dvc': {'contains': ['ip']},
                  'dvchost': {'contains': ['host name']}, 'end': {'contains': []}, 'endTime': {'contains': []},
                  'externalId': {'contains': []}, 'eventOutcome': {'contains': []}, 'fileCreateTime': {'contains': []},
                  'fileHash': {'contains': ['hash']}, 'fileHashMd5': {'contains': ['md5']},
                  'fileHashSha1': {'contains': ['sha1']}, 'fileHashSha256': {'contains': ['sha256']},
                  'fileHashSha512': {'contains': ['sha512']}, 'fileId': {'contains': []},
                  'fileModificationTime': {'contains': []}, 'fileName': {'contains': ['file name']},
                  'filePath': {'contains': ['file path']}, 'filePermission': {'contains': []},
                  'fileSize': {'contains': []}, 'fileType': {'contains': []}, 'fname': {'contains': ['file name']},
                  'fsize': {'contains': []}, 'in': {'contains': []}, 'message': {'contains': []},
                  'msg': {'contains': []}, 'oldfileCreateTime': {'contains': []}, 'oldfileHash': {'contains': ['hash']},
                  'oldfileId': {'contains': []}, 'oldfileModificationTime': {'contains': []},
                  'oldfileName': {'contains': ['file name']}, 'oldfilePath': {'contains': ['file path']},
                  'oldfilePermission': {'contains': []}, 'oldfileType': {'contains': []}, 'oldfsize': {'contains': []},
                  'out': {'contains': []}, 'outcome': {'contains': []}, 'proto': {'contains': []},
                  'receiptTime': {'contains': []}, 'request': {'contains': []},
                  'requestClientApplication': {'contains': []}, 'requestCookies': {'contains': []},
                  'requestMethod': {'contains': []}, 'requestURL': {'contains': ['url']}, 'rt': {'contains': []},
                  'shost': {'contains': ['host name']}, 'smac': {'contains': ['mac address']},
                  'sntdom': {'contains': ['domain']}, 'sourceAddress': {'contains': ['ip']},
                  'sourceDnsDomain': {'contains': ['domain']}, 'sourceHostName': {'contains': ['host name']},
                  'sourceMacAddress': {'contains': ['mac address']}, 'sourceNtDomain': {'contains': []},
                  'sourcePort': {'contains': ['port']}, 'sourceServiceName': {'contains': []},
                  'sourceTranslatedAddress': {'contains': ['ip']}, 'sourceTranslatedPort': {'contains': ['port']},
                  'sourceUserId': {'contains': []}, 'sourceUserName': {'contains': ['user name']},
                  'sourceUserPrivileges': {'contains': []}, 'spriv': {'contains': []}, 'spt': {'contains': ['port']},
                  'src': {'contains': ['ip']}, 'start': {'contains': []}, 'startTime': {'contains': []},
                  'suid': {'contains': []}, 'suser': {'contains': ['user name']}, 'transportProtocol': {'contains': []},
                  'vaultId': {'contains': ['vault id']}}
CEF_NAME_MAPPING: dict = {'act': 'deviceAction', 'app': 'applicationProtocol', 'applicationProtocol': 'app',
                          'baseEventCount': 'cnt', 'bytesIn': 'in', 'bytesOut': 'out', 'cat': 'deviceEventCategory',
                          'cn1': 'deviceCustomNumber1', 'cn1Label': 'deviceCustomNumber1Label',
                          'cn2': 'deviceCustomNumber2', 'cn2Label': 'deviceCustomNumber2Label',
                          'cn3': 'deviceCustomNumber3', 'cn3Label': 'deviceCustomNumber3Label', 'cnt': 'baseEventCount',
                          'cs1': 'deviceCustomString1', 'cs1Label': 'deviceCustomString1Label',
                          'cs2': 'deviceCustomString2', 'cs2Label': 'deviceCustomString2Label',
                          'cs3': 'deviceCustomString3', 'cs3Label': 'deviceCustomString3Label',
                          'cs4': 'deviceCustomString4', 'cs4Label': 'deviceCustomString4Label',
                          'cs5': 'deviceCustomString5', 'cs5Label': 'deviceCustomString5Label',
                          'cs6': 'deviceCustomString6', 'cs6Label': 'deviceCustomString6Label',
                          'destinationAddress': 'dst', 'destinationDnsDomain': 'destinationDnsDomain',
                          'destinationHostName': 'dhost', 'destinationMacAddress': 'dmac',
                          'destinationNtDomain': 'dntdom', 'destinationPort': 'dpt', 'destinationProcessName': 'dproc',
                          'destinationServiceName': 'destinationServiceName',
                          'destinationTranslatedAddress': 'destinationTranslatedAddress',
                          'destinationTranslatedPort': 'destinationTranslatedPort', 'destinationUserId': 'duid',
                          'destinationUserName': 'duser', 'destinationUserPrivileges': 'dpriv', 'deviceAction': 'act',
                          'deviceAddress': 'dvc', 'deviceCustomDate1': 'deviceCustomDate1',
                          'deviceCustomDate1Label': 'deviceCustomDate1Label', 'deviceCustomDate2': 'deviceCustomDate2',
                          'deviceCustomDate2Label': 'deviceCustomDate2Label', 'deviceCustomNumber1': 'cn1',
                          'deviceCustomNumber1Label': 'cn1Label', 'deviceCustomNumber2': 'cn2',
                          'deviceCustomNumber2Label': 'cn2Label', 'deviceCustomNumber3': 'cn3',
                          'deviceCustomNumber3Label': 'cn3Label', 'deviceCustomString1': 'cs1',
                          'deviceCustomString1Label': 'cs1Label', 'deviceCustomString2': 'cs2',
                          'deviceCustomString2Label': 'cs2Label', 'deviceCustomString3': 'cs3',
                          'deviceCustomString3Label': 'cs3Label', 'deviceCustomString4': 'cs4',
                          'deviceCustomString4Label': 'cs4Label', 'deviceCustomString5': 'cs5',
                          'deviceCustomString5Label': 'cs5Label', 'deviceCustomString6': 'cs6',
                          'deviceCustomString6Label': 'cs6Label', 'deviceDirection': 'deviceDirection',
                          'deviceDnsDomain': 'deviceDnsDomain', 'deviceEventCategory': 'cat',
                          'deviceExternalId': 'deviceExternalId', 'deviceFacility': 'deviceFacility',
                          'deviceHostname': 'dvchost', 'deviceInboundInterface': 'deviceInboundInterface',
                          'deviceMacAddress': 'deviceMacAddress', 'deviceOutboundInterface': 'deviceOutboundInterface',
                          'deviceProcessName': 'deviceProcessName',
                          'deviceTranslatedAddress': 'deviceTranslatedAddress', 'dhost': 'destinationHostName',
                          'dmac': 'destinationMacAddress', 'dntdom': 'destinationNtDomain',
                          'dpriv': 'destinationUserPrivileges', 'dproc': 'destinationProcessName',
                          'dpt': 'destinationPort', 'dst': 'destinationAddress', 'duid': 'destinationUserId',
                          'duser': 'destinationUserName', 'dvc': 'deviceAddress', 'dvchost': 'deviceHostname',
                          'end': 'endTime', 'endTime': 'end', 'externalId': 'externalId', 'eventOutcome': 'outcome',
                          'fileCreateTime': 'fileCreateTime', 'fileHash': 'fileHash', 'fileHashMd5': 'fileHashMd5',
                          'fileHashSha1': 'fileHashSha1', 'fileHashSha256': 'fileHashSha256',
                          'fileHashSha512': 'fileHashSha512', 'fileId': 'fileId',
                          'fileModificationTime': 'fileModificationTime', 'fileName': 'fileName',
                          'filePath': 'filePath', 'filePermission': 'filePermission', 'fileSize': 'fSize',
                          'fileType': 'fileType', 'fname': 'fileName', 'fsize': 'fileSize', 'in': 'bytesIn',
                          'message': 'msg', 'msg': 'message', 'oldfileCreateTime': 'oldfileCreateTime',
                          'oldfileHash': 'oldfileHash', 'oldfileId': 'oldfileId',
                          'oldfileModificationTime': 'oldfileModificationTime', 'oldfileName': 'oldfileName',
                          'oldfilePath': 'oldfilePath', 'oldfilePermission': 'oldfilePermission',
                          'oldfileType': 'oldfileType', 'oldfsize': 'oldfsize', 'out': 'bytesOut',
                          'outcome': 'eventOutcome', 'proto': 'transportProtocol', 'receiptTime': 'rt',
                          'request': 'requestURL', 'requestClientApplication': 'requestClientApplication',
                          'requestCookies': 'requestCookies', 'requestMethod': 'requestMethod', 'requestURL': 'request',
                          'rt': 'receiptTime', 'shost': 'sourceHostName', 'smac': 'sourceMacAddress',
                          'sntdom': 'sourceNtDomain', 'sourceAddress': 'src', 'sourceDnsDomain': 'sourceDnsDomain',
                          'sourceHostName': 'shost', 'sourceMacAddress': 'smac', 'sourceNtDomain': 'sntdom',
                          'sourcePort': 'spt', 'sourceServiceName': 'sourceServiceName',
                          'sourceTranslatedAddress': 'sourceTranslatedAddress',
                          'sourceTranslatedPort': 'sourceTranslatedPort', 'sourceUserId': 'suid',
                          'sourceUserName': 'suser', 'sourceUserPrivileges': 'spriv', 'spriv': 'sourceUserPrivileges',
                          'spt': 'sourcePort', 'src': 'sourceAddress', 'start': 'startTime', 'startTime': 'start',
                          'suid': 'sourceUserId', 'suser': 'sourceUserName', 'transportProtocol': 'proto'}
CONTAINS_VALIDATORS: dict = {'domain': "<function is_domain at 0x7f111f104940>",
                             'ip': "<function is_ip at 0x7f111f104790>", 'hash': "<function is_hash at 0x7f111f104820>",
                             'sha1': "<function is_sha1 at 0x7f111f104550>",
                             'sha256': "<function is_sha256 at 0x7f111f1045e0>",
                             'sha512': "<function is_sha512 at 0x7f111f104670>",
                             'md5': "<function is_md5 at 0x7f111f104700>",
                             'host name': "<function is_hostname at 0x7f111f1049d0>",
                             'mac address': "<function is_mac at 0x7f111f1044c0>",
                             'url': "<function is_url at 0x7f111f1048b0>",
                             'email': "<function is_email at 0x7f111f104a60>"}
CUSTOM_FUNCITON_RESULT_KEY_OID: str = "oid"
CUSTOM_FUNCTION_RESULT_HEADERS: frozenset = frozenset(
    {'message', 'status', 'oid', 'custom_function_run_id', 'custom_function_name', 'name'})
CUSTOM_FUNCTION_RESULT_KEY_CUSTOM_FUNCTION_NAME: str = "custom_function_name"
CUSTOM_FUNCTION_RESULT_KEY_CUSTOM_FUNCTION_RUN_ID: str = "custom_function_run_id"
CUSTOM_FUNCTION_RESULT_KEY_MESSAGE: str = "message"
CUSTOM_FUNCTION_RESULT_KEY_NAME: str = "name"
CUSTOM_FUNCTION_RESULT_KEY_STATUS: str = "status"


def ConnectorResult(base_connector=None) -> None:
    return


DATA_PATH_MAP: dict = {'custom_function_result.loop_state': 'loop_state',
                       'custom_function_result': 'custom_function_results.*',
                       'action_result.data': 'result_data.*.data', 'action_result.loop_state': 'loop_state',
                       'action_result.summary': 'result_data.*.summary',
                       'action_result.parameter': 'result_data.*.parameter',
                       'action_result.message': 'result_data.*.message', 'action_result.status': 'result_data.*.status',
                       'action_result.context': 'result_data.*.context', 'action_result.id': 'result_data.*.id',
                       'summary': 'result_summary', 'artifact:*.cef': 'cef'}
DEFAULT_LOCK_TIMEOUT: int = 1200
DEFAULT_REST_BASE_URL: str = "https://127.0.0.1/rest/"


def DataType(value, names=None, *, module=None, qualname=None, type=None, start=1):
    return


def DeprecationStatus(value, names=None, *, module=None, qualname=None, type=None, start=1):
    return


ENCRYPTED_DATA_TYPE: list = ['password']


def Enum(value, names=None, *, module=None, qualname=None, type=None, start=1):
    return


FILTERED_PLAYBOOK_INPUT_RESULTS_DP_IDENTIFIER: str = "filtered-playbook_input_results:"
FILTERED_PLAYBOOK_OUTPUT_RESULTS_DP_IDENTIFIER: str = "filtered-playbook_output_results:"
GET_ALL: str = "all"
GET_NEW: str = "new"
INVALID_FOR_ONPREM_STATE: str = "INVALID_FOR_ONPREM_STATE"


def Iterator():
    return


def JSONDecodeError(msg, doc, pos):
    return


def JsonTranslator(skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, sort_keys=False, indent=None,
                   separators=None, encoding='utf-8', default=None, use_decimal=True, namedtuple_as_object=True,
                   tuple_as_array=True, bigint_as_string=False, item_sort_key=None, for_json=False, ignore_nan=False,
                   int_as_string_bitcount=None, iterable_as_array=False):
    return


KILL_CHAIN_ACTIONS_ON_OBJECTIVES: str = "actions_on_objectives"
KILL_CHAIN_CNC: str = "cnc"
KILL_CHAIN_DELIVERY: str = "delivery"
KILL_CHAIN_EXPLOITATION: str = "exploitation"
KILL_CHAIN_INSTALLATION: str = "installation"
KILL_CHAIN_LIST: list = ['reconnaissance', 'weaponization', 'delivery', 'exploitation', 'installation', 'cnc',
                         'actions_on_objectives']
KILL_CHAIN_RECON: str = "reconnaissance"
KILL_CHAIN_WEAPONIZATION: str = "weaponization"
MAX_COUNT_VALUE: int = 4294967295
NAMED_PLAYBOOK_INPUT_DP_IDENTIFIER: str = ":playbook_input:"
NAMED_PLAYBOOK_OUTPUT_DP_IDENTIFIER: str = ":playbook_output:"
NOTE_FORMAT_HTML: str = "html"
NOTE_FORMAT_MARKDOWN: str = "markdown"
ON_FINISH_FN_NAME: str = "on_finish"


def ObjectParameterContext(data_path: str = '', config: dict[str, dict[str, typing.Any]] = None,
                           data: dict[str, typing.Any] = None, hidden_keys: set[str] = None) -> None:
    return


def Optional(*args, **kwds):
    return


PHANTOM_APP_STATES: str = "/home/phantomuser/phantom/local_data/app_states"
PHANTOM_BASE_URL: str = "https://localhost:8443"
PHANTOM_ENCODING: str = "utf-8"
PHANTOM_HOME: str = "/home/phantomuser/phantom"
PLAYBOOK_INFO_DATA_FIELD: str = "launching_user"
PLAYBOOK_INPUT_DP_IDENTIFIER: str = "playbook_input:"
PLAYBOOK_INPUT_RESULTS_DATA_FIELD: str = "playbook_input_results"
PLAYBOOK_INPUT_RUN_NAME_KEY: str = ":playbook_input:"
PLAYBOOK_OUTPUT_RESULTS_DATA_FIELD: str = "playbook_output_results"
PLAYBOOK_OUTPUT_RUN_NAME_KEY: str = ":playbook_output:"
PLAYBOOK_RUN_NAME_KEY: str = "playbook"
PRODUCT_NAME: str = "Splunk SOAR"


def ParameterContext(data_path: str = '', config: dict[str, dict[str, typing.Any]] = None) -> None:
    return


def ParameterProcessor(root_parameter_config: dict[str, dict[str, typing.Any]]) -> None:
    return


def PylibConfig():
    return


REST_BASE_URL: str = "https://localhost:8443/rest/"
SENSITIVITY_AMBER: str = "amber"
SENSITIVITY_GREEN: str = "green"
SENSITIVITY_LIST: list = ['red', 'amber', 'green', 'white']
SENSITIVITY_RED: str = "red"
SENSITIVITY_WHITE: str = "white"
SENTENCE_ENDING_PUNCTUATION: tuple = ('.', '!', '?')
SEVERITY_HIGH: str = "high"
SEVERITY_LIST: list = ['low', 'medium', 'high']
SEVERITY_LOW: str = "low"
SEVERITY_MEDIUM: str = "medium"
SOAR_HTTPS_PROXY: str = "SOAR_HTTPS_PROXY"
SOAR_HTTP_PROXY: str = "SOAR_HTTP_PROXY"


def Union(*args, **kwds):
    return


def base_connector_defunct_api(condition=True, message='') -> None:
    return


def base_playbook_api():
    return


def bytes_to_human_readable_size_str(n: int) -> str:
    return


def chunk(s: str, chunk_size: int) -> collections.abc.Iterator[str]:
    return


def cloud_only(func):
    return


def concatenate(*args, **kwargs):
    return


def debug_private_error_(message: Any) -> None:
    return


def debug_private_message_(message: Any) -> None:
    return


def decode_unicode(arg):
    return


def decode_unicode_dict(args) -> None:
    return


def decode_unicode_list(args) -> None:
    return


def decode_unicode_parameters(func):
    return


def decode_unicode_tuple(args):
    return


def deep_copy_dict(d, keys_to_exclude=()):
    return


def defunct_api(condition=True, message='') -> None:
    return


def deprecated_api(condition=True, message='') -> None:
    return


def dump_json(dump_dict, tag=None) -> None:
    return


def encode_proxy_var(val: str) -> str:
    return


def encode_unicode(arg):
    return


def encode_unicode_dict(args) -> None:
    return


def encode_unicode_list(args) -> None:
    return


def encode_unicode_parameters(func):
    return


def encode_unicode_tuple(args):
    return


def escape_db_key(s: str) -> str:
    return


def escape_null_chars_in_json_seq(seq: Union[list, dict], processed_seqs: Optional[set] = None) -> None:
    return


def escape_null_unicode_characters(input_str):
    return


def extract_data_paths(json_object_list, paths):
    return


def generate_uuid_string() -> str:
    return


def get_artifact_ids_from_action_result(named_datapath, action_results=None, trace: bool = False):
    return


def get_asset_names(action=None, tags=None):
    return


def get_cef_data(input_dict, map_dict):
    return


def get_file_name_from_url(url, should_unquote: bool = True):
    return


def get_host_from_url(url: str) -> Optional[str]:
    return


def get_list_from_string(comma_seperated_list: str, drop_blanks: bool = True, remove_duplicates: bool = True) -> list[
    str]:
    return


def get_phantom_strict_tls() -> bool:
    return

def get_random_chars(size: int = 6, chars: str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') -> str:
    return


def get_req_value(in_dict, in_key, strip_it: bool = True) -> str:
    return


def get_request_iter_pages(base_url: str, params=None, page_size: int = 50, verify=None):
    return


def get_str_val(in_dict, in_key, def_val=None, strip_it=True):
    return


def get_succ_or_failure_text(status_code):
    return


def get_valid_file_name(s: str) -> str:
    return


def get_value(in_dict, in_key, def_val=None, strip_it=True):
    return


def get_values_in_events(events, field_name) -> list[str]:
    return


def identity(obj):
    return


def is_cloud_install() -> bool:
    return


def is_domain(hostname: str) -> bool:
    return


def is_email(email_str) -> bool:
    return


def is_fail(status_code) -> bool:
    return


def is_hash(hash_str: str) -> bool:
    return


def is_hostname(hostname: str) -> bool:
    return


def is_ip(ip_str: str) -> bool:
    return


def is_mac(mac_str: str) -> bool:
    return


def is_md5(input_str: str) -> bool:
    return


def is_sha1(input_str: str) -> bool:
    return


def is_sha256(input_str: str) -> bool:
    return


def is_sha512(input_str: str) -> bool:
    return


def is_success(status_code):
    return


def is_url(input_str: str) -> bool:
    return


def is_windows_path(path: str) -> bool:
    return


def isfloat(value) -> bool:
    return


def mission_control_enabled() -> bool:
    return


def mission_control_only(func):
    return


def patched_session_request(self, method, url, **kwargs):
    return


def playbook_api(copy_user_provided_args=True) -> None:
    return


def quote_plus(string, safe='', encoding=None, errors=None):
    return


def remove_none_values(input_dict):
    return


def run_ext_command(command, dump_ouput: bool = False):
    return


def run_ext_command_list(command_list, dump_ouput: bool = False):
    return


def safe_int(obj) -> Optional[int]:
    return


def set_app_file_perms(path: str, recursive: bool = False) -> None:
    return


def should_bypass_proxies(url, no_proxy):
    return


string_types: tuple = (str, bytes)


def to_bool(value):
    return


def trace_(show_message: bool, message: Any) -> None:
    return


def unescape_db_key(s: str) -> str:
    return


def unquote(string, encoding='utf-8', errors='replace'):
    return


def validate_value_presense(obj):
    return


def wraps(wrapped, assigned=('__module__', '__name__', '__qualname__', '__doc__', '__annotations__'),
          updated=('__dict__',)):
    return
