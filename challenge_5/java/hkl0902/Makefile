SRCS := $(wildcard *.java)
COMPILED := $(wildcard *.class)

JFLAGS = -g -Xlint:unchecked -Xlint:deprecation

default:
	javac $(JFLAGS) -cp $(SRCS)
	mv $(COMPILED) CompiledFiles

check:
	java -ea -cp UnitTest
