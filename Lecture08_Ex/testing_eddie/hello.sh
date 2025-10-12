#!/bin/sh
#$ -cwd
#$ -N Hello
#$ -l h_rt=00:01:00
#$ -l h_vmem=1G

echo 'hello world'

#$ -o hello.o
#$ -e hello.e

