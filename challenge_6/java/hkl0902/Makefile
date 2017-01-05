SRCS := $(wildcard *.java)
COMPILED := $(wildcard *.class)

CPATH = "..:$(CLASSPATH):"

JFLAGS = -Xlint:unchecked -Xlint:deprecation

default:
	javac $(JFLAGS) -g -cp $(CLASSPATH) $(SRCS)

check:
	java -ea -cp $(CLASSPATH) UnitTest
