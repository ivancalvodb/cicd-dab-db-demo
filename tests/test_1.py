import os
import pytest

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

def test_unity_catalog_objects(ws_conn):
    catalog = True

    # creates 2 sets: test and ws 
    test_catalogs = {DEV_CATALOG, PROD_CATALOG}
    ws_catalogs = {x.name for x in ws_conn.catalogs.list()}

    # computes the intersection
    catalog_intersection = test_catalogs.intersection(ws_catalogs)

    # if all the necessary (test) catalogs are on the ws catalogs, check the schemas
    if test_catalogs == catalog_intersection:
        
        test_schemas = {DEV_SCHEMA, PROD_SCHEMA}
        catalog_schema_pairs = zip(test_catalogs, test_schemas)

        for catalog, schema in catalog_schema_pairs:
            try:
                ws_conn.schemas.get(full_name=f'catalog.schema')
            except:
                catalog = False
                break

    else:
        assert_flag = False   

    assert assert_flag