#!/bin/bash -l

# Example script 

# Request Time (format hours:minutes:seconds).
#$ -l h_rt=XX:XX:XX
# Request RAM per core. 
#$ -l tmem=XXG
#$ -l h_vmem=XXG
#$ -R y
#$ -pe smp XX

#$ -o /YOUR/OUTPUT/PATH # folder to store the shell outputs

#Set Name 
#$ -N EXAMPLE

date
hostname

#Setup python 
source /share/apps/source_files/python/python-3.9.5.source

# Loop over arguments looking for -i and -o
args=("$@")
i=0
while [ $i -lt $# ]; do
    #Set npy data 
    if ( [ ${args[i]} = "-message" ] ) ; then
        let i=$i+1
        text_message=${args[i]}
    elif  ( [ ${args[i]} = "-script" ] ) ; then
        let i=$i+1
        script_to_run=${args[i]}
    fi 
    let i=$i+1
done

# Check if user gave correct inputs
if [[ -z "${text_message}" ]] || [[ -z "${script_to_run}" ]]; then
    correct_input=0
else 
    correct_input=1
fi

#Check the user has provided the correct inputs
if ( [[ ${correct_input} -eq 0 ]] ) ; then
  echo ""
  echo "Incorrect input. Please see below for correct use"
  echo ""
  echo "Options:"
  echo " -message:         A simple text message  -- REQUIRED"
  echo " -script:          A python script setup with arsparse  -- REQUIRED"
  echo ""
  echo "${script_name} -script /PATH/TO/argsparse_example.py -message "Hello world""
  echo ""
  exit
fi

echo "Calling Python Script"
python3 ${script_to_run} --message ${text_message}

