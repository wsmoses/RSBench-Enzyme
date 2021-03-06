#===============================================================================
# User Options
#===============================================================================

COMPILER    = nvidia
OPTIMIZE    = yes
DEBUG       = no
PROFILE     = no
SM_VERSION  = 60

#===============================================================================
# Program name & source code list
#===============================================================================

program = rsbench

source = \
main.cu \
simulation.cu\
io.cu \
init.cu \
material.cu \
utils.cu

obj = $(source:.cu=.o)

#===============================================================================
# Sets Flags
#===============================================================================

# Standard Flags
CFLAGS := 

# Regular gcc Compiler
ifeq ($(COMPILER),nvidia)
  # CC = /mnt/sabrent/wmoses/llvm13/buildallfast/bin/clang++
  # -Rpass=enzyme 
  # CFLAGS += -g -ffast-math -mllvm -enable-implements-attr-resolver -mllvm -enzyme-print -Rpass=enzyme -fno-experimental-new-pass-manager --cuda-path=/usr/local/cuda-11.0 -L/usr/local/cuda-11.0/lib64 --cuda-gpu-arch=sm_$(SM_VERSION)  -std=c++11 -Xclang -load -Xclang /home/wmoses/git/Enzyme/enzyme/build13Fast/Enzyme/ClangEnzyme-13.so 

  CC = /mnt/sabrent/wmoses/llvm13/build/bin/clang++
  # -Rpass=enzyme 
  CFLAGS += -g -ffast-math -mllvm -enzyme-print -Rpass=enzyme -fno-experimental-new-pass-manager --cuda-path=/usr/local/cuda-11.0 -L/usr/local/cuda-11.0/lib64 --cuda-gpu-arch=sm_$(SM_VERSION)  -std=c++11 -Xclang -load -Xclang /home/wmoses/git/Enzyme/enzyme/build13D/Enzyme/ClangEnzyme-13.so 

endif

# Linker Flags
LDFLAGS = "-lcudart_static" "-ldl" "-lrt" -lpthread -lm

# Debug Flags
ifeq ($(DEBUG),yes)
  CFLAGS += -g -G
  LDFLAGS += -g -G
endif

# Profiling Flags
ifeq ($(PROFILE),yes)
  CFLAGS += -pg
  LDFLAGS  += -pg
endif

# Optimization Flags
ifeq ($(OPTIMIZE),yes)
  CFLAGS += -O3
endif

#===============================================================================
# Targets to Build
#===============================================================================

$(program): $(obj) rsbench.cuh Makefile
	$(CC) $(CFLAGS) $(obj) -o $@ $(LDFLAGS)

%.o: %.cu rsbench.cuh Makefile
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -rf rsbench $(obj)

edit:
	vim -p $(source) rsbench.cuh

run:
	./rsbench
