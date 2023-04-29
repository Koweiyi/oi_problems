test.o: test.cc
	g++ -o test.o -c -g test.cc 

log.o: log.cc
	g++ -o log.o -c -g log.cc

out: test.o log.o 
	g++ -fdiagnostics-color=always -g test.o log.o -o out

clean:
	rm *.o 
	rm *.exe