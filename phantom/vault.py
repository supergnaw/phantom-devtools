# "compat": "(<class 'module'>) <module 'phantom_common.compat' from '/home/phantomuser/phantom/pycommon3/phantom_common/compat.pyc'>",
# "config": "(<class 'phantom.utils.PylibConfig'>) <phantom.utils.PylibConfig object at 0x7f123bb9eee0>",
# "grp": "(<class 'module'>) <module 'grp' from '/home/phantomuser/phantom/usr/python39/lib/python3.9/lib-dynload/grp.cpython-39-x86_64-linux-gnu.so'>",
# "hashlib": "(<class 'module'>) <module 'hashlib' from '/home/phantomuser/phantom/usr/python39/lib/python3.9/hashlib.py'>",
# "install_info": "(<class 'module'>) <module 'phantom_common.install_info' from '/home/phantomuser/phantom/pycommon3/phantom_common/install_info.pyc'>",
# "json": "(<class 'module'>) <module 'json' from '/home/phantomuser/phantom/usr/python39/lib/python3.9/json/__init__.py'>",
# "logger": "(<class 'logging.Logger'>) <Logger phantom.vault (WARNING)>",
# "logging": "(<class 'module'>) <module 'logging' from '/home/phantomuser/phantom/usr/python39/lib/python3.9/logging/__init__.py'>",
# "magic": "(<class 'module'>) <module 'magic' from '/home/phantomuser/phantom/usr/python39/lib/python3.9/site-packages/magic.py'>",
# "os": "(<class 'module'>) <module 'os' from '/home/phantomuser/phantom/usr/python39/lib/python3.9/os.py'>",
# "re": "(<class 'module'>) <module 're' from '/home/phantomuser/phantom/usr/python39/lib/python3.9/re.py'>",
# "requests": "(<class 'module'>) <module 'requests' from '/home/phantomuser/phantom/usr/python39/lib/python3.9/site-packages/requests/__init__.py'>",
# "shutil": "(<class 'module'>) <module 'shutil' from '/home/phantomuser/phantom/usr/python39/lib/python3.9/shutil.py'>",
# "tempfile": "(<class 'module'>) <module 'tempfile' from '/home/phantomuser/phantom/usr/python39/lib/python3.9/tempfile.py'>",
# "uuid": "(<class 'module'>) <module 'uuid' from '/home/phantomuser/phantom/usr/python39/lib/python3.9/uuid.py'>",

import re
from typing import Optional

def Any(*args, **kwds) -> None:
    return


def ChunkTracker(filename, total_size) -> None:
    return


DOWNLOAD_URL_PATH: str = "https://localhost:8443/rest//download_attachment"
FILE_EXTENSIONS: dict = {'.vmsn': ['os memory dump', 'vm snapshot file'],
                         '.vmss': ['os memory dump', 'vm suspend file'], '.js': ['javascript'], '.doc': ['doc'],
                         '.docx': ['doc']}
MAGIC_FORMATS: list = [(re.compile('^PE.* Windows'), ['pe file', 'hash']),
                       (re.compile('^MS-DOS executable'), ['pe file', 'hash']), (re.compile('^PDF '), ['pdf']),
                       (re.compile('^MDMP crash'), ['process dump']), (re.compile('^Macromedia Flash'), ['flash'])]
NONROOT_INSTALL: bool = True


def Optional(*args, **kwds) -> None:
    return


PHANTOM_BASE_URL: str = ""
PHANTOM_ENCODING: str = "utf-8"
PHANTOM_VAULT: str = "/home/phantomuser/phantom/vault"
PHANTOM_VAULT_TMP: str = "/home/phantomuser/phantom/vault/tmp"
QUERY_URL_PATH: str = "https://localhost:8443/rest//container_attachment"
QUERY_URL_PATH_PHANTOM: str = "https://localhost:8443/rest/container_attachment"
REST_BASE_URL: str = "https://localhost:8443/rest/"
UPLOAD_FINISH_URL_PATH: str = "/upload_chunked_complete"
UPLOAD_URL_PATH: str = "/upload_chunked"


def Union(*args, **kwds) -> None:
    return


VAULT_DOC_URL_PATH: str = "https://localhost:8443/rest//vault_document"


def Vault() -> None:
    return


def _check_at_least_one_param(**kwargs) -> None:
    return


def _check_required_params(**kwargs) -> tuple[bool, str]:
    return


def _chunk_file_upload(file_location, file_name, container_id, metadata=None) -> None:
    return


def _do_request_delete(endpoint, success_message, error_message, trace=False) -> None:
    return


def _download_attachment(url, vault_hash, local_path) -> None:
    return


def _get_automation_broker_path(vault_id, download_file=True) -> None:
    return


def _get_connector_run_dir() -> str:
    return


def _get_container_id_from_user_input(container=None, trace: bool = False) -> tuple[bool, str, Optional[int]]:
    return


def add_attachment(local_path, container_id, file_name=None, metadata=None) -> None:
    return


def build_phantom_rest_url(*args) -> str:
    return


def chown_user_grp(path) -> None:
    return


def contains_from_file(file_path, alt_file_name=None) -> None:
    return


def debug_private_error_(message: Any) -> None:
    return


def debug_private_message_(message: Any) -> None:
    return


def defunct_api(condition=True, message='') -> None:
    return


def delete_attachment(attachment_id) -> None:
    return


def deprecated_api(condition=True, message='') -> None:
    return


def get_default_rest_headers() -> dict[str, str]:
    return


def get_meta_by_hash(container_id, s_hash, calculate=False) -> None:
    return


def get_phantom_vault_tmp_dir() -> None:
    return


def get_request_iter_pages(base_url: str, params=None, page_size: int = 50, verify=None) -> None:
    return


def get_rest_base_url() -> str:
    return


def get_vault_file(s_hash) -> None:
    return


def get_vault_file_path(vault_id) -> None:
    return



def is_nonroot_install() -> bool:
    return


def join(a, *p) -> None:
    return



def playbook_api(copy_user_provided_args=True) -> None:
    return



def safe_int(obj) -> Optional[int]:
    return


def vault_add(container=None, file_location=None, file_name=None, metadata=None, trace=False) -> None:
    return


def vault_delete(vault_id=None, file_name=None, container_id=None, remove_all=False, trace=False) -> None:
    return


def vault_info(vault_id=None, file_name=None, container_id=None, trace=False, download_file=True) -> None:
    return


class Vault:
    def _get_file_info(vault_id: int = None, file_name: str = None, container_id: int = None, method: str = 'or',
                       download_file: bool = True) -> None:
        pass

    def add_attachment(file_location, container_id, file_name=None, metadata=None) -> None:
        pass

    def create_attachment(file_contents, container_id, file_name=None, metadata=None) -> None:
        pass

    def get_file_info(vault_id=None, file_name=None, container_id=None, method='or') -> None:
        pass

    def get_file_path(vault_id) -> None:
        pass

    def get_vault_tmp_dir() -> None:
        pass
