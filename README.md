# MPI Python Basics Using mpi4py
MPI(Massage Passing Interface) using python package mpi4py

## What is MPI in python:
MPI stands for Message Passing Interface. It is a widely-used standard for parallel programming in high-performance computing (HPC). MPI provides a way for a program to communicate with other programs running on the same or other computers. In Python, you can use the mpi4py package to write parallel programs using MPI. This package provides a Python interface to the MPI libraries, allowing you to use MPI in your Python programs to parallelize computations and perform other types of intercrosses communication.

## About mpi4py:

1. mpi4py is a Python wrapper for the Message Passing Interface (MPI) standard, which is a widely-used library for parallel programming in high-performance
computing (HPC). It allows you to use MPI in your Python programs to parallelize computations and perform other types of interprocess communication.

2. The mpi4py package provides a number of functions and classes that you can use to implement parallel algorithms in Python. It provides a Comm class that represents an MPI communicator, which is an object that provides a way for processes to communicate with each other. You can use the Comm class to create new communicators, split existing communicators, and perform various other operations.

3. The mpi4py package also provides a number of functions that you can use to send and receive data between processes. For example, you can use the send() and
recv() functions to send and receive data using point-to-point communication, or the gather() and scatter() functions to perform collective communication.

3. Finally, mpi4py provides a number of utility functions that you can use to perform various operations, such as finding out the size of a communicator, the rank of a
process, or the number of processes in a communicator.

4. Overall, mpi4py is a useful package for writing parallel programs in Python that can take advantage

## How to use mpi4py:
To use mpi4py in your Python programs, you will first need to install the package. You can install mpi4py using pip, the Python package manager:

### pip install mpi4py

Once mpi4py is installed, you can use it in your Python programs by importing the mpi4py module:
### from mpi4py import MPI
The MPI module provides a number of functions and classes that you can use to write parallel programs using MPI.
To get started with mpi4py, you can try running a simple "hello world" program that sends a message from one process to another. 
