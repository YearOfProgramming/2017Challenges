SRC := $(wildcard src/*.cpp)
HEADERS := $(wildcard $(addprefix src/include/, *.h))

OBJDIR := obj
BINDIR := bin
OBJECTS := $(addprefix $(OBJDIR)/, $(notdir src/ $(SRC:.cpp=.o)))

EXE := solution.exe
CC := g++ 
CFLAGS := -Wall -c -std=c++11
LFLAGS := -Wall

$(EXE) : $(BINDIR) $(OBJDIR) $(OBJECTS)
	@$(CC) $(LFLAGS) -o $(BINDIR)/$@ $(OBJECTS)

obj/%.o : src/%.cpp $(HEADERS)
	@$(CC) $(CFLAGS) -o $@ $<

.PHONY : clean test $(BINDIR) $(OBJDIR)

clean : 
	@rm -rf $(BINDIR) $(OBJDIR)

test :
	@cd ../../..;\
	./_bin/test 6 cpp manuel;\
	cd challenge_6/cpp/manuel;

$(BINDIR) : 
	@mkdir -p $(BINDIR)

$(OBJDIR) :
	@mkdir -p $(OBJDIR)
