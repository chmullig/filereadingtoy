#Testing file reading speed
Sometimes we want to test how quickly we can read a bunch of numbers. This came
up in a discussion with Alex Gaudio at Sailthru. I've worked on proejcts where
we cached writes in this manner, but thought it could be useful for speeding up
reading files too large to fit in memory. Here's the result....

naive.py is the simplest implementation we discussed

naive_nativebuffer.py uses the builtin open() command's buffer to attempt to 
speed things up

chmullig_buffered.py is an attempt to do some intelligent buffering in python

## Timing on an ec2.micro instance.
Instance has ~600MB of RAM. It's a cloud virtual machine, so who knows what else
 is going on.

Data is several times larger than memory, so we can be sure there isn't too much
 caching. To be safe I reboot the (Virtual) machine after each test run.

### Data File
`generateData.py` to generate about 2GB of integegers. One int between 0 and 1000
per line, 531723486 lines.
	-rw-rw-r-- 1 ec2-user ec2-user 2.0G Nov 16 04:29 data.txt

### Results
`naive.py`
This was all CPU bound, as far as I could tell from glancing at top while this
was running.

	[ec2-user@domU-12-31-39-06-C9-4D iteratortester]$ time python naive.py data.txt 
	The total was... 265595677623

	real	31m57.609s
	user	30m55.456s
	sys	0m14.573s


`naive_buffered.py`
	[ec2-user@domU-12-31-39-06-C9-4D iteratortester]$ time python naive_nativebuffer.py data.txt 
	The total was... 265595677623

	real	31m27.858s
	user	30m21.678s
	sys	0m6.076s

`chmullig_buffered.py`

### System Info
	Linux domU-12-31-39-06-C9-4D 3.2.30-49.59.amzn1.x86_64 #1 SMP Wed Oct 3 19:54:33 UTC 2012 x86_64 x86_64 x86_64 GNU/Linux
	processor	: 0
	vendor_id	: GenuineIntel
	cpu family	: 6
	model		: 23
	model name	: Intel(R) Xeon(R) CPU           E5430  @ 2.66GHz
	stepping	: 10
	microcode	: 0xa07
	cpu MHz		: 2660.000
	cache size	: 6144 KB
	fpu		: yes
	fpu_exception	: yes
	cpuid level	: 13
	wp		: yes
	flags		: fpu de tsc msr pae cx8 sep cmov pat clflush mmx fxsr
	                  sse sse2 ss ht syscall nx lm constant_tsc up rep_good
	                  nopl pni ssse3 cx16 sse4_1 hypervisor lahf_lm
	bogomips	: 5320.00
	clflush size	: 64
	cache_alignment	: 64
	address sizes	: 38 bits physical, 48 bits virtual
	power management:

		     total       used       free     shared    buffers     cached
	Mem:           594        587          6          0          3        549
	-/+ buffers/cache:         34        559
	Swap:            0          0          0

	Python 2.6.8
