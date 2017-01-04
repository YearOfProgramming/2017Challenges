SRCS := $(wildcard *.java)
COMPILED := $(wildcard *.class)

#CPATH = "..:$(CLASSPATH):;..;$(CLASSPATH)"

JFLAGS = -g -Xlint:unchecked -Xlint:deprecation

default:
	javac $(JFLAGS) -cp $(CLASSPATH) $(SRCS)
	mv *.class CompiledFiles

check:
	java -ea -cp UnitTest
