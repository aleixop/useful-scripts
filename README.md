# Useful scripts

Scripts that I generally used and make my life easier.

## Create a slurm script

Use [this]('scripts/make_slurm_script.py') Python script to create a slurm script.

Usage:

```
usage: make_slurm_script.py [-h] [-A ACCOUNT] [-J JOB_NAME] [-c CPUS_PER_TASK] [-L LOGS_DIR] [-l LOGS_NAME] [-a ARRAY] [-m MEMORY] [-n NTASKS] [-M MODULES]

Create a wonderful SLURM script template with the options you wish. The script is written to standard output

optional arguments:
  -h, --help            show this help message and exit
  -A ACCOUNT, --account ACCOUNT
                        your cluster account
  -J JOB_NAME, --job_name JOB_NAME
                        pretty easy, your job name
  -c CPUS_PER_TASK, --cpus_per_task CPUS_PER_TASK
                        number of threads/processors to use
  -L LOGS_DIR, --logs_dir LOGS_DIR
                        directory where your stdout and stderr will be stored
  -l LOGS_NAME, --logs_name LOGS_NAME
                        by default logs have the job name, use this option to change it
  -a ARRAY, --array ARRAY
                        is your job an array? specify the range of index values and simultaneously running tasks (e.g. '1-7%3', jobs from 1 to 7 with 3 simultaneously running jobs). This option also prints a commented line with
                        variable ${SLURM_ARRAY_TASK_ID} already written
  -m MEMORY, --memory MEMORY
                        specify the real memory required per node. Default units are megabytes, different units can be specified using the suffix [K|M|G|T]
  -n NTASKS, --ntasks NTASKS
                        number of tasks, not pretty sure what it is, the default is 1
  -M MODULES, --modules MODULES
                        modules that need to be loaded, separated ','
```
