import os
import pytest
import time

import databricks
from databricks.sdk import WorkspaceClient

# DBFS data needed for the pipeline
DBFS_TURBINE_DATA = "/demos/manufacturing/iot_turbine/turbine"
DBFS_INCOMING_DATA = "/demos/manufacturing/iot_turbine/incoming_data"
DBFS_HISTORICAL_STATUS_DATA = "/demos/manufacturing/iot_turbine/historical_turbine_status"

# Catalog and schemas
DEV_CATALOG = "dev_catalog_awesome_company"
DEV_SCHEMA = "dev_schema_awesome_company"

PROD_CATALOG = "prod_catalog_awesome_company"
PROD_SCHEMA = "prod_schema_awesome_company"

@pytest.fixture
def ws_conn():
    # return the workspace connection, uses DATABRICKS_HOST and DATABRICKS_TOKEN env variables.
    return WorkspaceClient(host = os.environ['DATABRICKS_HOST'], token = os.environ['DATABRICKS_TOKEN'])

def test_check_dbfs_paths(ws_conn):
    # if all paths exists, test pass
    exists_paths = [ws_conn.dbfs.exists(path) for path in [DBFS_TURBINE_DATA, DBFS_INCOMING_DATA, DBFS_HISTORICAL_STATUS_DATA]]
    assert all(exists_paths)

def test_unity_catalog_objects(ws_conn):
    # assert value, if a catalog or schema does not exists, this value is set to False
    assert_flag = True

    # catalogs we want to check if exists before writting tables in to.
    catalogs = {DEV_CATALOG, PROD_CATALOG}
    schemas = {DEV_SCHEMA, PROD_SCHEMA}

    # iteraterable of (catalog,schema) pairs
    catalog_schema_pairs = tuple(zip(catalogs, schemas))

    for catalog, schema in catalog_schema_pairs:
        try:
            ws_conn.schemas.get(full_name=f'{catalog}.{schema}')
            time.sleep(1)
        except:
            assert_flag = False
            break

    assert assert_flag