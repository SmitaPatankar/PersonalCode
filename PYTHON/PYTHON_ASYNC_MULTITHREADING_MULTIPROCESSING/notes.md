# GIL
- for memory management
- only one python interpreter instruction can be executed at a time
- problem on computational side
- pandas, numpy etc don't have it

# Concurrency
- not everything can be concurrent, some flows have to be sequential

# Do something else while waiting
- system will free up thread to go do other work until we receive response from say db etc
- asyncio/threading(not exactly parallel bcoz of GIL but does other stuff while waiting on n/w by releasing GIL)

# Do computations together
- multiprocessing(with GIL) - faster with overhead or Cython(no GIL) (python compiled as C code and then as machine instructions)

# I/O driven concurrency
- single thread - slices of work from diff tasks i.e. async event loop  - demarked with await keyword

# Other libraries
- aiohttp
- aiofiles
- uvloop
- unsync - decide async, threads, processes on its own
- trio - cancellation, coordination etc

# sync vs async vs multithreading vs multiprocessing
- sync - 1 process and 1 thread does the work be it computing/waiting for i/o
- multithreading - multiple threads for multiple requests, but uses same resources from main process, hence can cause problems and difficult to make threadsafe, parallel
- asynchronous - single thread non blocking event loop
- multiprocessing - multiple processes with their own resources

# When to use multithreading, multiprocessing and asyncio
- CPU Bound => Multi Processing
- I/O Bound, Fast I/O, Limited Number of Connections => Multi Threading - context switching
- I/O Bound, Slow I/O, Many connections => Asyncio - decide on your own when to switch context
