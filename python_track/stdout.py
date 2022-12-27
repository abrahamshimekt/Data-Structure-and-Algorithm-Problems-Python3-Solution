# The implementation of print
import sys
stdout_fileno = sys.stdout
sample_input = ['my','name','is','abraham']
for ip in sample_input:
    stdout_fileno.write(str(ip)+' ')
