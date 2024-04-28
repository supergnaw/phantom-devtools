# "base64": "(<class 'module'>) <module 'base64' from '/home/phantomuser/phantom/usr/python39/lib/python3.9/base64.py'>",
# "datetime": "uninspectable callable",
# "dateutil": "(<class 'module'>) <module 'dateutil' from '/home/phantomuser/phantom/usr/python39/lib/python3.9/site-packages/dateutil/__init__.py'>",
# "django_settings": "(<class 'django.conf.LazySettings'>) <Settings \"phantom_ui.settings\">",
# "install_info": "(<class 'module'>) <module 'phantom_common.install_info' from '/home/phantomuser/phantom/pycommon3/phantom_common/install_info.pyc'>",
# "ipaddress": "(<class 'module'>) <module 'ipaddress' from '/home/phantomuser/phantom/usr/python39/lib/python3.9/ipaddress.py'>",
# "json": "(<class 'module'>) <module 'simplejson' from '/home/phantomuser/phantom/usr/python39/lib/python3.9/site-packages/simplejson/__init__.py'>",
# "os": "(<class 'module'>) <module 'os' from '/home/phantomuser/phantom/usr/python39/lib/python3.9/os.py'>",
# "ph_engine": "(<class 'module'>) <module 'phantom.ph_engine' from '/home/phantomuser/phantom/lib3/phantom/ph_engine.pyc'>",
# "ph_jsons": "(<class 'module'>) <module 'phantom.json_keys' from '/home/phantomuser/phantom/lib3/phantom/json_keys.pyc'>",
# "ph_status": "(<class 'module'>) <module 'phantom.status' from '/home/phantomuser/phantom/lib3/phantom/status.pyc'>",
# "random": "(<class 'module'>) <module 'random' from '/home/phantomuser/phantom/usr/python39/lib/python3.9/random.py'>",
# "re": "(<class 'module'>) <module 're' from '/home/phantomuser/phantom/usr/python39/lib/python3.9/re.py'>",
# "requests": "(<class 'module'>) <module 'requests' from '/home/phantomuser/phantom/usr/python39/lib/python3.9/site-packages/requests/__init__.py'>",
# "six": "(<class 'module'>) <module 'six' from '/home/phantomuser/phantom/usr/python39/lib/python3.9/site-packages/six.py'>",
# "string": "(<class 'module'>) <module 'string' from '/home/phantomuser/phantom/usr/python39/lib/python3.9/string.py'>",
# "subprocess": "(<class 'module'>) <module 'subprocess' from '/home/phantomuser/phantom/usr/python39/lib/python3.9/subprocess.py'>",
# "sys": "(<class 'module'>) <module 'sys' (built-in)>",
# "timedelta": "uninspectable callable",
# "traceback": "(<class 'module'>) <module 'traceback' from '/home/phantomuser/phantom/usr/python39/lib/python3.9/traceback.py'>",
# "types": "(<class 'module'>) <module 'types' from '/home/phantomuser/phantom/usr/python39/lib/python3.9/types.py'>",
# "urllib": "(<class 'module'>) <module 'urllib' from '/home/phantomuser/phantom/usr/python39/lib/python3.9/urllib/__init__.py'>",
# "urlparse": "(<class 'module'>) <module 'urllib.parse' from '/home/phantomuser/phantom/usr/python39/lib/python3.9/urllib/parse.py'>",
# "utc": "(<class 'pytz.UTC'>) UTC",
# "uuid": "(<class 'module'>) <module 'uuid' from '/home/phantomuser/phantom/usr/python39/lib/python3.9/uuid.py'>",
# "vault": "(<class 'module'>) <module 'phantom.vault' from '/home/phantomuser/phantom/lib3/phantom/vault.pyc'>",
# "xrange": "uninspectable callable"

import collections
import typing
from types import NoneType
from typing import Any, Callable, Optional, Union

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
APP_ERR_LOCK_ACQUIRE_NAMED: str = "Failed to acquire lock named '{lock_name}' for Action: '{action_name}' App: '{app_name}'"
APP_ERR_LOCK_DATA_PATH_INVALID: str = "Data path: {0} value cannot be used as a lock name"
APP_ERR_LOCK_KEY_NOT_FOUND: str = "Key '{key_name}' not found in the {dict_type} JSON sent to the app"
APP_ERR_LOCK_MODULE_UNAVAILABLE: str = "Backend module required to carry out Lock/UnLock operations is unavailable"
APP_ERR_LOCK_OBJECT_ALREADY_USED: str = ("Object already used once multiple uses of object is not allowed")
APP_ERR_LOCK_OBJECT_NAME_NONE: str = "Lock name not set. Please lock first"
APP_ERR_LOCK_OBJECT_UNLOCKED: str = "Object not in locked state. Unlock operation not possible"
APP_ERR_NYI: str = "Not yet implemented"
APP_ERR_UNK_CMD: str = "Unknown Action: {action_identifier}"
APP_INGEST_ACTIONS: list = ["on_poll", "poll_now"]
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
BACKUP_RESTORE_LOCK: str = "1002"
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
CUSTOM_FUNCTION_RESULT_HEADERS: frozenset = frozenset(
    {'message', 'status', 'oid', 'custom_function_run_id', 'custom_function_name', 'name'})

CUSTOM_FUNCTION_RESULT_KEY_CUSTOM_FUNCTION_NAME: str = "custom_function_name"
CUSTOM_FUNCTION_RESULT_KEY_CUSTOM_FUNCTION_RUN_ID: str = "custom_function_run_id"
CUSTOM_FUNCTION_RESULT_KEY_NAME: str = "name"
CUSTOM_FUNCTION_RESULT_KEY_STATUS: str = "status"
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
ENCRYPTED_DATA_TYPE: list = ['password']
GET_ALL: str = "all"
GET_NEW: str = "new"
INDICATOR_LOCK: str = "1001"
KILL_CHAIN_ACTIONS_ON_OBJECTIVES: str = "actions_on_objectives"
KILL_CHAIN_CNC: str = "cnc"
KILL_CHAIN_DELIVERY: str = "delivery"
KILL_CHAIN_EXPLOITATION: str = "exploitation"
KILL_CHAIN_INSTALLATION: str = "installation"
KILL_CHAIN_LIST: list = ['reconnaissance', 'weaponization', 'delivery', 'exploitation', 'installation', 'cnc',
                         'actions_on_objectives']
KILL_CHAIN_RECON: str = "reconnaissance"
KILL_CHAIN_WEAPONIZATION: str = "weaponization"
NOTE_FORMAT_HTML: str = "html"
NOTE_FORMAT_MARKDOWN: str = "markdown"
PHANTOM_ENCODING: str = "utf-8"
PHANTOM_HOME: str = "/home/phantomuser/phantom"
PHANTOM_SCM_GIT: str = "/home/phantomuser/phantom/scm/git"
PHANTOM_TMP: str = "/tmp"
REST_BASE_URL: str = "https://localhost:8443/rest/"
SENSITIVITY_AMBER: str = "amber"
SENSITIVITY_GREEN: str = "green"
SENSITIVITY_LIST: list = ['red', 'amber', 'green', 'white']
SENSITIVITY_RED: str = "red"
SENSITIVITY_WHITE: str = "white"
SEVERITY_HIGH: str = "high"
SEVERITY_LIST: list = ['low', 'medium', 'high']
SEVERITY_LOW: str = "low"
SEVERITY_MEDIUM: str = "medium"


def _check_at_least_one_param(**kwargs):
    return


def _check_one_and_only_one_param(or_none=False, **kwargs):
    return


def _check_param_in_choices(choices, **kwargs):
    return


def _check_required_params(**kwargs) -> tuple[bool, str]:
    return True, ""


def _clear_data_datastore(key):
    return


def _clear_data_filesystem(key):
    return


def _do_request_delete(endpoint, success_message, error_message, trace=False):
    return


def _do_request_get(endpoint, params=None, success_message='', error_message='', trace=False):
    return


def _do_request_post(endpoint, json_data, success_message='', error_message='', trace=False):
    return


def _dump_shell_returns(out, err, ret_code) -> None:
    return


def _extract_data_path(json_object_list, path, splits=None):
    return


def _get_arity(include_none=False, **kwargs):
    return


def _get_container_id_from_user_input(container=None, trace: bool = False) -> tuple[bool, str, typing.Optional[int]]:
    return True, "success", 0


def _get_data_datastore(key, clear_data=True):
    return


def _get_data_filesystem(key, clear_data=True):
    return


def _get_phase_data_from_user_input(phase=None, container=None, trace: bool = False) -> tuple[
    bool, str, typing.Optional[int], typing.Optional[int]]:
    return True, "success", 0, 0


def _get_statuses_for_status_type(container, status_type, default_only=False, trace=False):
    return


def _get_template_id_from_user_input(template=None, trace: bool = False) -> tuple[bool, str, typing.Optional[int]]:
    return True, "success", 0


def _merge_jsons(default_json, merge_json):
    return


def _rest_list_iterator(endpoint, params=None, success_message=None, error_message=None, trace=False):
    return


def _save_data_datastore(value, key=None):
    return


def _save_data_filesystem(value, key=None):
    return


def _set_status(container=None, status=None, trace=False):
    return


def act(action=None, parameters=None, assets=None, tags=None, callback=None, reviewer=None, handle=None,
        start_time=None, name=None, asset_type=None, app=None, parent_action=None, loop_state=None):
    return


def actions_done(action_names=None, trace=False) -> bool:
    return True


def add_artifact(container: int = None, raw_data=None, cef_data=None, label=None, name=None, severity=None,
                 identifier=None, artifact_type=None, field_mapping=None, trace=False, run_automation=False) -> tuple[
    bool, str, int]:
    """
    Add a new artifact to the specified container. After creating an artifact, this call returns a tuple of a success
    flag (Boolean), any response message (string), and the artifact ID (integer).

    :param container: The container to act on. This parameter can either be a numerical ID or a container object. If no
        container is provided, the currently running container is used.
    :param raw_data: The raw artifact data is stored as-is and is accessible from the artifacts. You can also use an
        empty dictionary.
    :param cef_data: The Common Event Format (CEF) representation of the original data. You can also use an empty
        dictionary.
    :param label: The label expressing the class of artifact. For example, event or netflow.
    :param name: The name of the artifact.
    :param severity: Supported values are `high`, `medium`, `low`, or the name of any active severity on the system.
    :param identifier: The source data identifier for the artifact. Generally this is a unique ID from a data source. A
        value of None generates a GUID for the source data identifier.
    :param artifact_type: The type of the artifact, such as `host` or `network`.
    :param field_mapping: If CEF field names are not specific enough, use this parameter to specify the contains type
        for the field. For example, if you add a playbook with an artifact that has a CEF field named user_hash, this
        parameter can help convey to the platform that user_hash is a hash type of field that can then be used to show
        contextual actions.
    :param trace: Trace is a flag related to the level of logging. If trace is on (True), more logging is enabled. When
    set to True, more detailed output is displayed in debug output.
    :param run_automation: Default is False. If set to True, the parameter causes active playbooks to run when new
    artifacts are added to the container.
    :return: [status, message, id]
    """
    return True, "success", 0


def add_attachment(local_path, container_id, file_name=None, metadata=None):
    """
    Depricated. Use Vault.add()
    """
    return


def add_comment(container, comment):
    return


def add_list(list_name=None, values=None):
    return


def add_note(container: int | dict = None, note_type=None, trace=False, note_format='html', **kwargs) -> tuple[
    bool, str, int]:
    """
    Use the add_note API to add a note of the specified type to the container. On completion it returns a tuple of a
    success flag, any response messages, and the note ID.

    :param container: The container to act on. This parameter can either be a numerical ID or a container object. If no
        container is provided, the currently running container is used.
    :param note_type: The type of note you want to create. Valid options are "general", "artifact", or "task". For
        "artifact" or "task" types you must supply the artifact_id or task_id as additional parameters.
    :param trace: The format of the note. Valid options are HTML or markdown. If the format is not provided, HTML is the
        default.
    :param note_format: ID of the artifact for which you want notes.
    :param kwargs:
        task_id: ID of the task for which you want notes.
        title: Title for the note.
        content: Content for the note. The content of a note can include a limited set of HTML and Markdown. See Using
            HTML and Markdown in notes in the Splunk SOAR (On-premises) manual for a list of what is and what is not
            supported.
        trace: Trace is a flag related to the level of logging. If trace is on (True), more logging is enabled. When set
            to True, more detailed output is displayed in debug output.
    :return: [status, message, id]
    """


def add_response_plan(container=None, response_template_id=None, trace=False) -> tuple[bool, str, typing.Optional[str]]:
    return True, "", ""


def add_response_plan_task(container=None, name=None, order=None, trace=False, **kwargs):
    return


def add_tags(container: int | dict = None, tags: str | list[str] = None, trace: bool = False) -> tuple[bool, str]:
    """
    Use the add_tags API to add tags to a container. On completion, the call returns a success flag and any response
    messages.

    :param container:The container to act on. This parameter can either be a numerical ID or a container object. If no
        container is provided, the currently running container is used.
    :param tags:The tags to be added.
    :param trace: Trace is a flag related to the level of logging. If trace is on (True), more logging is enabled. When
        set to True, more detailed output is displayed in debug output.
    :return: [status, message]
    """
    return True


def add_task(container: int | dict = None, name: str = None, owner: int | str = None, role: int | str = None,
             trace: bool = False, **kwargs) -> tuple[bool, str, int]:
    """
    Use the add_task API to add a task to a container. It returns a success flag, a success or error message, and the ID
    of the created task.

    :param container: The container to act on. This parameter can either be a numerical ID or a container object.
    :param name: Name of the task to create.
    :param int owner: Identifier you can associate with the task.
    :param dict role: Identifier for the role to associate with the task.
    :param trace: Trace is a flag related to the level of logging. If trace is on (True), more logging is enabled. When
        set to True, more detailed output is displayed in debug output.
    :param kwargs:
    :return: [status, message, id]
    """
    return True, "success", 0


def add_workbook(container: int | dict = None, workbook_id: int = None, trace: bool = False) -> tuple[bool, str]:
    """
    Use the add_workbook API to add a workbook to a container. This API returns a two-tuple of a success flag and a
        message. The success flag is set to true if the workbook was successfully added, otherwise it is set to false.
        The message originates from the HTTP response from your Splunk SOAR (On-premises) web server.
    :param container: The container to act on. This parameter can either be a numerical ID or a container object. If no
        container is provided, the currently running container is used.
    :param workbook_id: The ID of the workbook to be added.
    :param trace: Trace is a flag related to the level of logging. If trace is on (True), more logging is enabled. When
        set to True, more detailed output is displayed in debug output.
    :return: [status, message]
    """
    return True, "success"


def address_in_network(ip: str, net: str) -> bool:
    return True


def artifact_values(events, field_name):
    return


def assign(container=None, user_id_or_name=None, role_id_or_name=None):
    return


def attacker_ips(container, scope=None, filter_artifact_ids=None, events=None) -> list[str]:
    return [""]


def build_phantom_rest_url(*args) -> str:
    return ""


def bytes_to_human_readable_size_str(n: int) -> str:
    return ""


def call_playbook_action_callback(function_object, callable_metadata_json_str, success_int, container_json_str,
                                  result_json_str, handle_json_str, loop_state_json_str):
    return


def call_playbook_custom_function_callback(function_object, callable_metadata_json_str, success_int, container_json_str,
                                           result_json_str, handle_json_str, loop_state_json_str):
    return


def check_list(list_name=None, value=None, case_sensitive=False, substring=False):
    return


def cleanse_filtered_action_results_(filtered_action_results) -> None:
    return


def clear_data(key, use_filesystem=False):
    return


def clear_object(key=None, container_id=None, playbook_name=None, repo_name=None, trace=False) -> None:
    return


def close(container: dict, trace=False) -> tuple[bool, str]:
    """
    The close API allows playbooks to close the specified container by setting its status to the default status of
    Resolved.

    :param container: A container object.
    :param trace:
    :return: [status, message]
    """
    return True, "success"


def collect(container, datapath, scope=None, limit=None, none_if_first=False, filter_artifact_ids=None, trace=False):
    return


def collect2(container=None, action_results=None, action_name=None, datapath=None, filter_artifacts=None, tags=None,
             scope=None, limit=None, trace=False):
    return


def collect_for_condition(container=None, action_results=None, filtered_artifact_ids=None,
                          filtered_action_result_ids=None, datapath=None, scope=None):
    return


def collect_from_action_result(action_result, datapath, trace=False):
    return


def collect_from_container(container, datapath, scope=None, limit=None, none_if_first=False, filter_artifact_ids=None,
                           action_results=None, trace=False):
    return


def collect_from_contains(container=None, action_results=None, contains=None, tags=None, filter_artifacts=None,
                          include_params=True, scope=None, limit=None, trace=False):
    return


def collect_from_playbook_results(playbook_results=None, datapath=None, trace=False):
    return


def comment(container: int | dict = None, comment: str = None, trace: bool = False) -> tuple[bool, str]:
    """
    Use the comment API to add a text comment to the container. On completion, the API returns a tuple of a success flag
    and any response messages.

    :param container: The container to act on. This parameter can either be a numerical ID or a container object. If no
        container is provided, the currently running container is used.
    :param comment: The comment to add to the container.
    :param trace: Trace is a flag related to the level of logging. If trace is on (True), more logging is enabled. When
        set to True, more detailed output is displayed in debug output.
    :return: [status, message]
    """
    return True, "success"


def completed(action_names: Optional[collections.abc.Sequence[str]] = None,
              playbook_names: Optional[collections.abc.Sequence[str]] = None,
              cus_names: Optional[collections.abc.Sequence[str]] = None, trace: bool = False) -> bool:
    return True


def concatenate(*args, **kwargs):
    return


def condition(container=None, action_results=None, conditions=None, logical_operator='or', scope=None,
              filtered_artifacts=None, filtered_results=None, limit=None, trace=False, name=None, auto=True,
              case_sensitive=True, handle=None, delimiter: Optional[str] = ','):
    return


def convert_to_unicode(value: 'Any') -> 'str':
    return ""


def create_container(name: str = None, label: str = None, container_type: str = 'default', template: int | str = None,
                     tenant_id: int | str = None, trace: bool = False):
    """
    Use the create_container API to create a new container. It returns a tuple of a success flag, any response message,
    and the numeric ID of the created container. If no container was created, the ID returned is None. Once a container
    is created, it is possible to retrieve container data using get_container by passing the created container_id.

    :param name: The name of the case.
    :param label: The label of the case.
    :param container_type: The type of container to create, either default or case.
    :param template: Applies to containers of type case, and indicates the template to use on creation. If the container
        type is case and no template is provided, the default template is used. If no default template is set, an error
        is returned.
    :param tenant_id: The Splunk SOAR (On-premises) tenant ID as per the /rest/tenant API. This field is required if
        multi-tenancy is enabled.
    :param trace: Trace is a flag related to the level of logging. If trace is on (True), more logging is enabled. When
        set to True, more detailed output is displayed in debug output.
    :return: [status, message, id]
    """
    return True, "success", 0


def cus(cus=None, parameters=None, callback=None, name=None, loop_state=None):
    return


def datastore_add(list_name, values):
    return


def datastore_check(list_name=None, value=None, case_sensitive=False, substring=False):
    return


def datastore_delete(list_name):
    return


def datastore_get(list_name):
    return


def datastore_present(list_name, values, column_index=-1):
    return


def datastore_set(list_name, values_list_of_lists):
    return


def debug(message):
    return


def debug_private_error_(message: Any) -> None:
    return


def debug_private_message_(message: Any) -> None:
    return


def decision(container=None, action_results=None, conditions=None, logical_operator='or', scope=None,
             filtered_artifacts=None, filtered_results=None, limit=None, trace=False, name=None, auto=True,
             case_sensitive=True, delimiter: Optional[str] = ','):
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


def deduplicate_params(parameters):
    return


def deepcopy(x, memo=None, _nil: list = None):
    if _nil is None:
        _nil = []
    return


def delete_artifact(artifact_id: int = None) -> bool:
    """
    The delete_artifact API allows artifacts to be deleted as identified by an artifact ID. On completion, this API
    returns a Boolean value indicating whether the operation was successful.

    :param artifact_id: The numerical ID of the artifact to be removed.
    :return: successful
    """
    return True


def delete_attachment(attachment_id):
    return


def delete_from_list(list_name=None, value=None, column=None, remove_all=False, remove_row=False, trace=False):
    return


def delete_pin(pin_id: int = None) -> tuple[bool, str]:
    """
    The delete_pin API is used to delete an existing pin. On completion, this API returns a success flag and a message.

    :param pin_id: The ID of the pin to be deleted.
    :return: [status, message]
    """
    return True, "success"


def discontinue() -> None:
    return


def does_condition_use_ar_data_(conditions=None, trace=False) -> bool:
    return True


def does_condition_use_filtered_ar_data_(conditions=None, trace=False) -> bool:
    return True


def dump_json(dump_dict, tag=None) -> None:
    return


def encode_proxy_var(val: str) -> str:
    return ""


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


def error(message):
    return


def escape_db_key(s: str) -> str:
    return ""


def expand_datapaths_(container=None, datapaths=None, scope=None, filter_artifact_ids=None, trace=False, separator=None,
                      drop_none=False, csv_list=True):
    return


def extract_data_paths(json_object_list, paths):
    return


def fix_artifact_dp(datapaths):
    return


def fix_datapath(datapath, trace=False):
    return


def format(container=None, template=None, parameters=None, scope=None, filter_artifact_ids=None, name=None, trace=False,
           separator=None, drop_none=False):
    return


def get_URLs(container, scope=None, filter_artifact_ids=None, events=None):
    return


def get_action_info(action=None, action_run_id=0, app_run_id=0, result_data=True):
    return


def get_action_results(action: Union[str, collections.abc.Mapping[str, Any], NoneType] = None, action_run_id=0,
                       app_run_id=0, result_data=True, action_name=None, playbook_run_id=0, flatten=True,
                       trace=False) -> collections.abc.Sequence[collections.abc.Mapping[str, typing.Any]]:
    return []


def get_action_status(action_names=None):
    return


def get_apps(action=None, asset=None, app_type=None):
    return


def get_artifact_ids_from_action_result(named_datapath, action_results=None, trace: bool = False):
    return


def get_artifacts(container, artifact_label, scope=None, filter_artifact_ids=None, limit=None):
    return


def get_asset_names(action=None, tags=None):
    return


def get_assets(action=None, tags=None, types=None):
    return


def get_attacked_ips(container, events):
    return


def get_base_url() -> Optional[str]:
    return ""


def get_cef_data(input_dict, map_dict):
    return


def get_cef_value(event_id, cef, field_name) -> str:
    return ""


def get_child_playbook_action_results(action_name=None, trace=False):
    return


def get_child_playbook_results(playbook_runs_info=None, playbook_run_name=None, trace=False):
    return


def get_collect_limit_():
    return


def get_container(container_id):
    return


def get_current_container_id_():
    return


def get_current_container_label_():
    return


def get_current_playbook_info():
    return


def get_cus_results(cus_run_id=None, cus_name=None, trace=False):
    return


def get_cus_status(cus_names: Optional[collections.abc.Sequence[str]] = None) -> Optional[
    collections.abc.Mapping[str, Any]]:
    return []


def get_data(key, clear_data=True, use_filesystem=False):
    return


def get_datapaths_for_contains(output, contains, path_prefix=''):
    return


def get_default_rest_headers() -> dict[str, str]:
    return {"": ""}


def get_effective_user():
    return


def get_extra_data(action=None, action_run_id=0, app_run_id=0):
    return


def get_file_name_from_url(url, should_unquote: bool = True):
    return


def get_filter_artifact_ids_(datapath_obj, datapath_is_str, filter_artifact_ids, action_results=None, trace=False):
    return


def get_filtered_data(name=None):
    return


def get_format_data(name=None):
    return


def get_host_from_url(url: str) -> Optional[str]:
    return ""


def get_incident_phase(container=None, trace=False):
    return


def get_incident_task(container=None, task_id=None, trace=False, **kwargs):
    return


def get_incident_tasks(container=None, trace=False) -> tuple[bool, str, typing.Optional[collections.abc.Sequence[str]]]:
    return True, "", ""


def get_json_object(data):
    return


def get_list(list_name=None, values=None, column_index=-1, trace=False):
    return


def get_list_from_string(comma_seperated_list: str, drop_blanks: bool = True, remove_duplicates: bool = True) -> list[
    str]:
    return [""]


def get_notes(container: int | dict = None, artifact_id: int = None, task_id: int = None, trace: bool = False,
              **kwargs) -> list:
    """
    The get_notes API is used to get all the notes for the requested object, either a container, a task, or an artifact.
    On completion, this API returns the requested notes.

    :param container: The container to act on. This container can either be a numerical ID or a container object. If no
        container is provided, the currently running container is used.
    :param artifact_id: ID of the artifact you want notes for.
    :param task_id: ID of the task you want notes for.
    :param trace: Trace is a flag related to the level of logging. If trace is on (True), more logging is enabled. When
        set to True, more detailed output is displayed in debug output.
    :param kwargs:
    :return: [notes]
    """
    return []


def get_object(key=None, clear_data=False, container_id=None, playbook_name=None, repo_name=None, trace=False):
    return


def get_parent_handle():
    return


def get_parent_playbook_run_id():
    return


def get_phantom_home() -> Optional[str]:
    return ""


def get_phase(container: int | dict = None, trace: bool = False) -> tuple[bool, str, int, str]:
    """
    Use the get_phase API to retrieve the current phase of the container. On completion, this API returns a tuple of a
    success flag, any response messages, the phase ID and the phase name.

    :param container: The container to act on. This parameter can either be a numerical ID or a container object. If no
        container is provided, the currently running container is used.
    :param trace: Trace is a flag related to the level of logging. If trace is on (True), more logging is enabled. When
        set to True, more detailed output is displayed in debug output.
    :return: [status, message, phase_id, phase_name]
    """
    return True, "success", 0, "new"


def get_playbook_info(playbook_id=None, playbook_name=None, playbook_repo=None):
    return


def get_playbook_results(playbook_run_id=0, result_data=False, flatten=True):
    return


def get_playbook_run_id_():
    return


def get_playbook_scope_():
    return


def get_playbook_scope_artifacts_():
    return


def get_playbook_status(names=None, playbook_run_ids=None):
    return


def get_random_chars(size: int = 6, chars: str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') -> str:
    return ""


def get_raw_data(container):
    return


def get_req_value(in_dict, in_key, strip_it: bool = True) -> str:
    return ""


def get_request_iter_pages(base_url: str, params=None, page_size: int = 50, verify=None):
    return


def get_response_templates(trace=False) -> tuple[bool, str, typing.Optional[list[str]]]:
    return True, "", []


def get_rest_base_url() -> str:
    return ""


def get_results(name, flatten=False, trace=False):
    return


def get_run_data(key=None):
    return


def get_start_end_from_range_str(ip_range: str = '') -> tuple[typing.Optional[str], typing.Optional[str]]:
    return "", None


def get_str_val(in_dict, in_key, def_val=None, strip_it=True):
    return


def get_succ_or_failure_text(status_code):
    return


def get_successful_action_results_v2(action_results):
    return


def get_summary(playbook_run_id=0):
    return


def get_tagged_artifacts(container, tags, label='*', **kwargs):
    return


def get_tags(container: int | dict = None, trace: bool = False) -> tuple[bool, str, list[str]]:
    """
    Use the get_tags API to retrieve the tags applied to a container. On completion, this API returns a tuple of a
    success flag, a response message, and a list of tags.

    :param container: The container to act on. This parameter can either be a numerical ID or a container object. If no
        container is provided, the currently running container is used.
    :param trace: Trace is a flag related to the level of logging. If trace is on (True), more logging is enabled. When
        set to True, more detailed output is displayed in debug output.
    :return: [status, message, [tags]]
    """
    return True, "success", ["tags"]


def get_task_notes(container=None, task_id=None, trace=False, **kwargs):
    return


def get_tasks(container: int | dict = None, trace: bool = False, **kwargs) -> tuple[bool, str, dict]:
    """
    Use the get_tasks API to get all the tasks associated with a container. Use the get_tasks API to get all the tasks
    associated with a container. This API returns a generator object. Each item in the generator is a dictionary
    containing the following keys: a boolean flag "success", a response message "message" and a dictionary "data".

    :param container: The container to act on. This parameter can either be a numerical ID or a container object.
    :param trace: Trace is a flag related to the level of logging. If trace is on (True), more logging is enabled. When
        set to True, more detailed output is displayed in debug output.
    :param kwargs:
    :return: [status, message, {data}]
    """
    return True, "success", {}


def get_user_session_token():
    return


def get_valid_file_name(s: str) -> str:
    return ""


def get_value(in_dict, in_key, def_val=None, strip_it=True):
    return


def get_values_in_events(events, field_name) -> list[str]:
    return [""]


def get_vault_file(s_hash):
    """
    Depricated. Use Vault.info()
    """
    return


def get_vault_file_path(vault_id):
    return


def get_vault_item_info(vault_id=None, get_hashes=False):
    return


def html_file_to_pdf(source_file_path, output_file_path) -> bool:
    return True


def html_string_to_pdf(source_html_string, output_file_path):
    return


def ip_to_int_(ip: str) -> int:
    return 0


def is_cus_running():
    return


def is_domain(hostname: str) -> bool:
    return True


def is_email(email_str) -> bool:
    return True


def is_fail(status_code) -> bool:
    return True


def is_hash(hash_str: str) -> bool:
    return True


def is_hostname(hostname: str) -> bool:
    return True


def is_ip(ip_str: str) -> bool:
    return True


def is_ip_in_range(ip_to_check: str, ip_range) -> bool:
    return True


def is_ip_in_subnet_(ip: str, network: str, mask_len: int) -> bool:
    return True


def is_mac(mac_str: str) -> bool:
    return True


def is_md5(input_str: str) -> bool:
    return True


def is_sha1(input_str: str) -> bool:
    return True


def is_sha256(input_str: str) -> bool:
    return True


def is_sha512(input_str: str) -> bool:
    return True


def is_success(status_code):
    return


def is_url(input_str: str) -> bool:
    return True


def is_windows_path(path: str) -> bool:
    return True


def isfloat(value) -> bool:
    return True


def join(a, *p):
    return


def merge(case: int | dict = None, container_id: int = None, artifact_id: int = None, ioc_field: str = None,
          playbook_run_id: int = None, action_run_id: int = None, vault_id: int = None, note_title: str = None,
          note_description: str = None, trace: bool = False) -> tuple[bool, str]:
    """
    Use the merge API to add items to a case. The merge API returns a tuple of a success flag and any response messages.
    :param case: The case to add items to. This parameter can either be a numerical ID or a container object. If no case
        is provided, the currently running container is used.
    :param container_id: The numerical ID of a container to add. All artifacts, playbook runs, action runs, vault items,
        notes and comments are copied. Mapping entries are created for each item that is copied, and all copied
        artifacts have their in_case flag set to true on the source artifact. If the container ID has already been added
        to the case, an error is returned. Any playbook or action runs that are running are not copied.
    :param artifact_id: The numerical ID of an artifact to add. This parameter copies the artifact to the case, creates
        a mapping entry and sets the in_case flag to true on the source container. If the artifact ID has already been
        added to the case, an error is returned.
    :param ioc_field: Common Event Format (CEF) key of the indicators of compromise (IOC) to add. Requires artifact ID
        to be specified. Copies a specific IOC from the specified artifact. A new artifact is created in the case
        containing the selected IOC and a mapping entry. If the IOC and artifact pair has already been added to the
        case, an error is returned.
    :param playbook_run_id: The numerical ID of the playbook run to add. Copies the playbook run, playbook run logs and
        all playbook action runs to the case. Mapping entries are created for the playbook runs and action runs. If the
        playbook run has already been added to the case, an error is returned. Playbook runs that are 'running' cannot
        be added to a case.
    :param action_run_id: The numerical ID of an action run, which can be retrieved from an action object or by using
        the get_summary API, which enumerates all the actions that were executed in the playbook. This parameter copies
        the action run to the case and creates a mapping entry. If the action run has already been added to the case, an
        error is returned. Action runs that are running cannot be added to a case.
    :param vault_id: The numerical value of the vault file's ID attribute. Copies a file in the vault to the case. If
        the vault file has already been added, an error is returned.
    :param note_title: The title of the note.
    :param note_description: The description of the note.
    :param trace: Trace is a flag related to the level of logging. If trace is on (True), more logging is enabled. When
        set to True, more detailed output is displayed in debug output.
    :return: [status, message]
    """
    return True, "success"


def non_started_runs(names: frozenset[str], run_names: frozenset[str]) -> frozenset[str]:
    return frozenset([""])


def parse_errors(results):
    return


def parse_results(results):
    return


def parse_success(action_results):
    return


def pin(container: int | dict = None, message: str = None, data: str = None, pin_type: str = "card",
        pin_style: str = "grey", truncate: bool = True, name: str = None, trace: bool = False) -> tuple[bool, str, int]:
    """
     Use the pin API to pin data to a container. Once complete, the API returns a tuple of a success flag, any response
     messages, and the pin ID.

    :param container: The container to act on. This parameter can either be a numerical ID or a container object. If no
        container is provided, the currently running container is used.
    :param message: A message associated with the pinned data.
    :param data: The data to be pinned.
    :param pin_type: The type of pin to create. The default pin type is 'card': card, data.
    :param pin_style: The style of the pin. The default pin style type is 'grey': grey, blue, red.
    :param truncate: If the message or data fields are longer than the character limit, this flag determines if the data
        is automatically truncated or if an error is raised. The default is truncate=True, and the flag automatically
        truncates the message to the allowable character limit. truncate=False raises an error and no pin is created.
    :param name: The name for the pin. If there is a name, it is unique in a container. If you try to create a named pin
        on a container where a pin with that name already exists, it updates that pin instead of creating a new one.
        This parameter lets you use the pin API to create or update a pin without needing to keep track of the pin ID.
    :param trace: Trace is a flag related to the level of logging. If trace is on (True), more logging is enabled. When
        set to True, more detailed output is displayed in debug output.
    :return:
    """
    return True, "success", 0


def playbook(playbook=None, container=None, handle=None, show_debug=True, callback=None, name=None, inherit_scope=True,
             inputs=None, loop_state=None):
    return


def playbook_block(block_name=None, cf_run_id=0):
    return


def playbooks_completed(names: Optional[collections.abc.Sequence[str]], trace: bool) -> bool:
    return True


def print_errors(action_results):
    return


def promote(container: int | dict = None, template: int | str = None, trace: bool = False) -> tuple[bool, str]:
    """
    The promote API is used to promote a container to a case.

    :param container: The container to act on. This parameter can either be a numerical ID or a container object. If no
        container is provided, the currently running container is used.
    :param template: Either a numerical ID or the name of the template to use for the case. If no template is provided,
        the default template is used. If no default is set, an error is returned.
    :param trace: Trace is a flag related to the level of logging. If trace is on (True), more logging is enabled. When
        set to True, more detailed output is displayed in debug output.
    :return: [status, message]
    """
    return True, "success"


def prompt(user=None, message='', respond_in_mins=30, callback=None, name=None, options=None, parameters=None,
           container=None, scope=None, filter_artifact_ids=None, trace=False, separator=None, drop_none=False):
    return


def prompt2(user=None, respond_in_mins=30, callback=None, response_types=None, message='', parameters=None, name=None,
            container=None, scope=None, filter_artifact_ids=None, separator=None, drop_none=False, trace=False,
            role=None):
    return


def quote_plus(string, safe='', encoding=None, errors=None):
    return


def remove_list(list_name=None, empty_list: bool = False, trace=False):
    return


def remove_none_values(input_dict):
    return


def remove_tags(container: int | dict = None, tags: str | list[str] = None, trace: bool = False) -> tuple[bool, str]:
    """
    The remove_tags API is used to remove tags from a container. Upon completion, the API returns a success flag and any
    response messages.

    :param container: The container to act on. This parameter can either be a numerical ID or a container object. If no
        container is provided, the currently running container is used.
    :param tags: A string or list of strings that contains the tags to be removed.
    :param trace: Trace is a flag related to the level of logging. If trace is on (True), more logging is enabled. When
        set to True, more detailed output is displayed in debug output.
    :return: [status, message]
    """
    return True, "success"


def render_template(template, context):
    return


def reset_python_path_(paths) -> None:
    return


def run_ext_command(command, dump_ouput: bool = False):
    return


def run_ext_command_list(command_list, dump_ouput: bool = False):
    return


def runs_completed(names: Optional[collections.abc.Sequence[str]], get_status: Callable[
    [Optional[collections.abc.Sequence[str]]], Optional[collections.abc.Mapping[str, Any]]], trace: bool) -> bool:
    return True


def safe_int(obj) -> Optional[int]:
    return 0


def save_artifact(container, raw_data, cef_data, label, name, severity, identifier, artifact_type, field_mapping=None,
                  run_automation=False):
    return


def save_data(value, key=None, use_filesystem=False):
    return


def save_object(key=None, value=None, auto_delete=True, container_id=None, playbook_name=None, repo_name=None,
                trace=False):
    return


def save_playbook_output_data(output=None, trace=False):
    return


def save_run_data(value=None, key=None, auto=True, trace=False):
    return


def session_delete(uri, *args, **kwargs):
    return


def session_get(uri, *args, **kwargs):
    return


def session_post(uri, *args, **kwargs):
    return


def set_action_limit(limit):
    return


def set_collect_limit_(limit=None) -> None:
    return


# todo: get formatting for duetime
def set_duetime(container: int | dict = None, operation: str = '+', minutes: int = None, trace: bool = None) -> tuple[
    bool, str, str]:
    """
    Use the set_duetime API to modify the due time of a container. This parameter returns a tuple of a success flag, a
    message if available, and the new due time.

    :param container: The container to act on. This parameter can either be a numerical ID or a container object. If no
        container is provided, the currently running container is used.
    :param operation: A choice of add or + or subtract -, defaults to +.
    :param minutes: The number of minutes to add or subtract.
    :param trace: Trace is a flag related to the level of logging. If trace is on (True), more logging is enabled. When
        set to True, more detailed output is displayed in debug output.
    :return: [status, message, duetime]
    """
    return True, "success", ""


def set_git_repo_path_(repo_name):
    return


def set_incident_owner(user=None, container=None, trace=False) -> tuple[bool, str]:
    return True, ""


def set_incident_phase(response_plan_id, phase_id, container=None, trace=False):
    return


def set_label(container: int | dict = None, label: str = None, trace: bool = False) -> tuple[bool, str]:
    """
    The set_label API allows users to dynamically change the label of a container. The label must already exist in
    system settings to be applied to a container. Upon completion, the API returns a tuple of a success flag and any
    response messages.

    :param container: The container to act on. It can either be a numerical ID or a container object. If no container is
        provided, the currently running container is used.
    :param label: A string containing the label to apply.
    :param trace: Trace is a flag related to the level of logging. If trace is on (True), more logging is enabled. When
        set to True, more detailed output is displayed in debug output.
    :return: [status, message]
    """
    return True, "success"


def set_list(list_name=None, values=None):
    return


def set_owner(container: int | dict = None, user: str | int = None, trace: bool = False, task_id: int = None,
              role: str | int = None) -> tuple[bool, str]:
    """
    Use the set_owner API to dynamically assign a container or task to a user or role. Upon completion, the API returns
    a tuple of a success flag and a message, if available.

    :param container: The ID of the container assigned ownership. If no container is provided, the currently running
        container is used.
    :param user: Valid Splunk SOAR (On-premises) username or ID assigned, or an empty string to remove assignments on
        the container. If you don't set a user, or you send an empty string, you remove assignments from the container.
    :param trace: Trace is a flag related to the level of logging. If trace is on (True), more logging is enabled. When
        set to True, more detailed output is displayed in debug output.
    :param task_id: The task ID of the task assigned ownership. If an empty string is sent, this API removes any owners
        from the task.
    :param role: The name or ID of the role. If no user or role values are set or if empty strings are sent, role
        assignments are removed from the container or task.
    :return:
    """
    return True, "success"


def set_parent_handle(handle):
    return


def set_phase(container:int|dict=None, phase:str|int=None, trace:bool=False) -> tuple[bool, str]:
    """
    Use the set_owner API to dynamically assign a container or task to a user or role. Upon completion, the API returns
    a tuple of a success flag and a message, if available.

    :param container: The container to act on. This parameter can either be a numerical ID or a container object. If no
        container is provided, the currently running container is used.
    :param phase: Use either a phase name or a numerical ID for the phase to apply.
    :param trace: Trace is a flag related to the level of logging. If trace is on (True), more logging is enabled. When
        set to True, more detailed output is displayed in debug output.
    :return: [status, message]
    """
    return True, "success"


def set_python_path_(path_val):
    return


# todo: figure out the return type of this function
def set_sensitivity(container: dict, sensitivity: str):
    """
    Use the set_sensitivity API to dynamically change the sensitivity of a container while it is being processed. The
    system supports four levels of sensitivity in accordance to the US-CERT Traffic Light Protocol. The levels supported
    are red, amber, green, and white.

    :param container: The current container object.
    :param sensitivity: The name of your desired severity level.
    :return: Unknown
    """
    return


# todo: figure out the return type of this function
def set_severity(container: dict, severity: str):
    """
    Use the set_severity API to dynamically change the severity of a container while it is being processed.

    :param container: The current container object.
    :param severity: The name of your desired severity level.
    :return: Unknown
    """
    return


def set_status(container:int|dict=None, status:str=None, trace:bool=False) -> tuple[bool, str]:
    """
    Use the set_status API to update the status of a container. Returns a tuple of a success flag and a message, if
    available. 
    
    :param container: The container to act on. This parameter can either be a numerical ID or a container object. If no 
        container is provided, the currently running container is used. 
    :param status: Set the status of either new, open, resolved, closed, or a custom status defined by an administrator. 
    :param trace: Trace is a flag related to the level of logging. If trace is on (True), more logging is enabled. When
        set to True, more detailed output is displayed in debug output. 
    :return: [status, message]
    """
    return True, "success"


def set_task_owner(container, task_id, owner, trace=False) -> tuple[
    bool, str, typing.Optional[collections.abc.Sequence[str]]]:
    return True, "", [""]


def task(user=None, message=None, respond_in_mins=0, callback=None, name=None):
    return


def trace_(show_message: bool, message: Any) -> None:
    return


def txfrm_collected_ar_data_(tmp_operand_data, trace=False):
    return


def type_correct_(value_to_correct=None, reference_value=None):
    return


def unescape_db_key(s: str) -> str:
    return ""


def unquote(string, encoding='utf-8', errors='replace'):
    return


def update(container: dict, update: dict, unify_datetime_format: bool=False) -> tuple[bool, str]:
    """
    Use the update API to make an update to a container. It returns a tuple of a success flag and any response messages.

    :param container: The container object to be updated.
    :param update: A JSON serializable Python dictionary which contains updates to the container. Include only the
        fields that you want to change.
    :param unify_datetime_format:
    :return: [status, message]
    """
    return True, "success"


def update_pin(pin_id:int=None, message:str=None, data:str=None, pin_type:str=None, pin_style:str=None, trace:bool=False) -> tuple[bool, str]:
    """
    Use the update_pin API to update an existing pin. Upon completion, this API returns a success flag and a message.

    :param pin_id: The ID of the pin to be updated.
    :param message: A new message string for the pin.
    :param data: A new data string for the pin.
    :param pin_type: A new type for the pin.
    :param pin_style: A new style for the pin.
    :param trace:
    :return: [status, message]
    """
    return True, "success"


def valid_ip(address: Union[str, bytes]) -> bool:
    return True


def valid_net(net) -> bool:
    return True


def validate_value_presense(obj):
    return


def vault_add(container=None, file_location=None, file_name=None, metadata=None, trace=False):
    return


def vault_delete(vault_id=None, file_name=None, container_id=None, remove_all=False, trace=False):
    return


def vault_info(vault_id=None, file_name=None, container_id=None, trace=False, download_file=True):
    return


def victim_ips(container, scope=None, filter_artifact_ids=None, events=None) -> list[str]:
    return [""]


def wraps(wrapped, assigned=('__module__', '__name__', '__qualname__', '__doc__', '__annotations__'),
          updated=('__dict__',)):
    return
