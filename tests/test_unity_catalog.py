import os
import sys
import pytest
import time

import databricks
from databricks.sdk import WorkspaceClient

# import src.libraries.awesome_lib_1 as awesome_lib_1

@pytest.fixture
def ws_conn():
    # Return the workspace connection, uses DATABRICKS_HOST and DATABRICKS_TOKEN env variables.
    return WorkspaceClient(host = os.environ['DATABRICKS_HOST'], token = os.environ['DATABRICKS_TOKEN'])

def test_dbfs_paths(ws_conn):
    # - DBFS
    # ws_conn.dbfs.exists()
    assert True

def test_unity_catalog_objects(ws_conn):
    # - Catalogs
    # ws_conn.catalogs.list()
    # ws_conn.catalogs.get(name=...)

    # - Schemas
    # ws_conn.schemas.get(full_name=...)
    # ws_conn.schemas.list(catalog_name=...)

    # - Tables
    # ws_conn.tables.get(full_name=table_full_name)
    # ws_conn.tables.list(catalog_name=..., schema_name=...)
    assert True