TARGETS = \
	bin/fuzzable1 \

all: $(TARGETS)

bin/%: src/%.c
	$(CC) $< -o $@

clean:
	rm bin/*
