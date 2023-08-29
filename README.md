# CI/CD with DAB demo
This is a demo that implements CI/CD using DABs on Databricks platformn

# Commands for DAB

(One time config) When the repo is cloned, run this in projects root:
```console
databricks bundle schema > bundle-settings-schema.json
```

## Validate bundle.yml config file

Before deploying your current project, validate the **bundle.yml** config file using the following command:

```console
databricks bundle validate
```

If a JSON is returned everything is ready to be deployed.

P.D: **This command only validates the host and file syntax**, this does not check the existence of catalogs, schemas, tables or paths in DBFS.

## Deploy the project (locally)

The following command will deploy the pipeline defined on the **bundle.yml** file (*etl-dtl-sensors-pipeline*) in the workspace:

```console
databricks bundle deploy --target dev
```

After this step, you'll be able to see the DLT pipeline on the platform.

Go to the "Data Engineering" section on the left panel, then click on "Delta Live Tables"

## Run the pipeline deployed on the previous step (locally)

The following command runs the pipeline *etl-dtl-sensors-pipeline* on the development environment:

```console
databricks bundle run etl-dtl-sensors-pipeline --target dev 
```



## Automated deployment using CI/CD tools

Now that we learned how deploy a run a workload (in this case, a pipeline). We should do the above command line calls from CI/CD tools such as Github Actions, AWS CodePipeline or any other tool that monitors your repo changes.

In this demo, we created a Github Action file that acts as a build, test and deployment process, check the repo path: ***.github/workflows/prod.yml***

It is recommended to do unit/integration testing before doing deployments on production environments, we encourage to have separate workspaces (dev, qa/staging, prod) for local testing and automated deployments.



