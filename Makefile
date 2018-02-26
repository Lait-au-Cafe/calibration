CXXFLAGS=-std=c++11 -Wall -Wextra -Werror -g
TARGET=calibration

$(TARGET): calibration.cpp
	g++ -o $@ $< $(CXXFLAGS) `pkg-config opencv --libs --cflags`

.PHONY: clean
clean:
	rm -f $(TARGET)
