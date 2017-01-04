SRCS := $(wildcard *.java)
COMPILED := $(wildcard *.class)

CPATH = "..:$(CLASSPATH):"

JFLAGS = -g -Xlint:unchecked -Xlint:deprecation

default:
	javac $(JFLAGS) -cp $(CLASSPATH) $(SRCS)

check:
	java -ea -cp $(CLASSPATH) UnitTest
