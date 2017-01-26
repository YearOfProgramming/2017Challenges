cmake_minimum_required(VERSION 3.6)
project(newp)

set(CMAKE_CXX_STANDARD 98)

set(SOURCE_FILES main.cpp challenge_16.cpp challenge_16.h)
add_executable(newp ${SOURCE_FILES})