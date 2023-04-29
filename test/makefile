out: test.o log.o 
	g++ -g test.o log.o -o out

test.o: test.cc
	g++ -o test.o -c -g test.cc 

log.o: log.cc
	g++ -o log.o -c -g log.cc

clean:
	rm *.o 
	rm *.exe