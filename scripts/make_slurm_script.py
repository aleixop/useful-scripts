#!/usr/bin/env python3

__author__ = "Aleix Obiol"
__email__ = "obiol@icm.csic.es"

import sys
import argparse
import os.path

def get_args():
    """
    Parse and return arguments passed in.
    """
    parser = argparse.ArgumentParser(
        description = "Create a wonderful SLURM script template with the options you wish. The script is written to standard output")
    # Add arguments
    parser.add_argument("-A",
                        "--account",
                        default = 'emm2',
                        type = str,
                        help = "your cluster account")
    parser.add_argument("-J",
                        "--job_name",
                        help = "pretty easy, your job name",
                        type = str,
                        default = 'my_job')
    parser.add_argument("-c",
                        "--cpus_per_task",
                        help = "number of threads/processors to use",
                        type = str,
                        default = '2')
    parser.add_argument("-L",
                        "--logs_dir",
                        help = "directory where your stdout and stderr will be stored",
                        type = str,
                        default = 'data/logs/')
    parser.add_argument("-l",
                        "--logs_name",
                        help = "by default logs have the job name, use this option to change it",
                        type = str)
    parser.add_argument("-a",
                        "--array",
                        help = "is your job an array? specify the range of index values and simultaneously running tasks (e.g. '1-7%%3', jobs from 1 to 7 with 3 simultaneously running jobs). This option also prints a commented line with variable ${SLURM_ARRAY_TASK_ID} already written",
                        type = str)
    parser.add_argument("-m",
                        "--memory",
                        type = str,
                        help = "specify the real memory required per node. Default units are megabytes, different units can be specified using the suffix [K|M|G|T]")
    parser.add_argument("-n",
                        "--ntasks",
                        type = str,
                        help = "number of tasks, not pretty sure what it is, the default is 1",
                        default = '1')
    parser.add_argument("-M",
                        "--modules",
                        type = str,
                        help = "modules that need to be loaded, separated ','")
    # Array for all arguments passed to script
    args = parser.parse_args()
    # Assign args to variables
    account = args.account
    job_name = args.job_name
    cpus_per_task = args.cpus_per_task
    logs_dir = args.logs_dir
    logs_name = args.logs_name
    array = args.array
    memory = args.memory
    ntasks = args.ntasks
    modules = args.modules
    # Return all variable values
    return account, job_name, cpus_per_task, logs_dir, logs_name, array, memory, ntasks, modules

def main():
    """
    Create SLURM script
    """
    account, job_name, cpus_per_task, logs_dir, logs_name, array, memory, ntasks, modules = get_args()
    if logs_dir[-1] != '/':
        logs_dir += '/'
    if not logs_name:
        logs_name = job_name
    print("#!/bin/bash\n")
    print("#SBATCH --account=" + account)
    print("#SBATCH --job-name=" + job_name)
    print("#SBATCH --ntasks=" + ntasks)
    print("#SBATCH --cpus-per-task=" + cpus_per_task)
    if array:
        print("#SBATCH --output=" + logs_dir + logs_name + "_%A_%a.out")
        print("#SBATCH --error=" + logs_dir + logs_name + "_%A_%a.err")
        print("#SBATCH --array=" + array)
    else:
        print("#SBATCH --output=" + logs_dir + logs_name + "_%J.out")
        print("#SBATCH --error=" + logs_dir + logs_name + "_%J.err")
    if memory:
        print("#SBATCH --mem=" + memory)
    if modules:
        print('\n', end = '')
        print('# Load modules\n')
        modules_list = modules.split(',')
        for module in modules_list:
            module = module.strip()
            print("module load " + module)
    if array:
        print("\n# Array\n")
        print('# SAMPLE=$( | awk "NR == ${SLURM_ARRAY_TASK_ID}")')

if __name__ == '__main__':
    main()
